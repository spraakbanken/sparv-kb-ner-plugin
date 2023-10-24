from typing import Iterable, Tuple
import itertools

from sparv.api import annotator, get_logger, Output, Annotation

from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

from sparv_kb_ner.ner_pipeline import NerPipeline


logger = get_logger(__name__)


SENT_SEP = "\n"
TOK_SEP = " "


def load_model(model_name: str, tokenizer_name: str) -> NerPipeline:
    logger.info(
        "preloading CustomNerPipeline(model=%s, tokenizer=%s)",
        model_name,
        tokenizer_name,
    )
    tokenizer = AutoTokenizer.from_pretrained(
        tokenizer_name
        # "KBLab/bert-base-swedish-lowermix-reallysimple-ner"
    )

    model = AutoModelForTokenClassification.from_pretrained(
        model_name,
        # "KBLab/bert-base-swedish-lowermix-reallysimple-ner"
    )
    return CustomNerPipeline(
        model=model,
        tokenizer=tokenizer,
    )


class CustomNerPipeline(NerPipeline):
    def __init__(self, model, tokenizer) -> None:
        self.model = model
        self.tokenizer = tokenizer

    def run(
        self,
        sentence: Annotation,
        word: Annotation,
        out_ne_type: Output,
        out_ne_score: Output,
    ) -> None:

        sentences, _orphans = sentence.get_children(word)
        token_word = list(word.read())
        # sentences_to_tag = [
        #     TOK_SEP.join(token_word[token_index] for token_index in sent)
        #     for sent in sentences
        # ]
        sentences_to_tag = [
            [token_word[token_index] for token_index in sent] for sent in sentences
        ]

        # Escape <, > and &
        # sentences_to_tag = xml.sax.saxutils.escape(sentences_to_tag)
        # stdout = run_nlp(stdin)
        out_type_annotation = word.create_empty_attribute()
        out_score_annotation = word.create_empty_attribute()

        logger.info("running model")
        pred = []
        for sent_to_tag in sentences_to_tag:
            pred.extend(
                (
                    self.model.config.id2label[t.item()]
                    for t in torch.argmax(
                        self.model(
                            **self.tokenizer(
                                sent_to_tag,
                                is_split_into_words=True,
                                return_tensors="pt",
                            )
                        ).logits,
                        dim=2,
                    )[0]
                )
            )
        logger.debug("len(pred)=%d", len(pred))
        # for sent, sent_to_tag in zip(sentences, sentences_to_tag, strict=True):
        # sentences_to_tag = [
        #     [token_word[token_index] for token_index in sent] for sent in sentences
        # ]
        logger.info("aligning tokens")
        tokens = self.tokenize_and_align_labels(sentences_to_tag)
        logger.debug("len(tokens['labels'])=%d", len(tokens["labels"]))
        # logger.debug("tokens = %s", tokens)
        aligned_tokens = itertools.chain.from_iterable(tokens["labels"])
        token_indices_and_predictions = (
            (t, p) for t, p in zip(aligned_tokens, pred, strict=True) if t != -100
        )
        for t, p in token_indices_and_predictions:
            # logger.debug("p=%s,t=%s", p, t)
            if p == "O":
                continue
            out_type_annotation[t[0]] = p

        logger.info("writing annotations")
        out_ne_type.write(out_type_annotation)
        out_ne_score.write(out_score_annotation)

    def tokenize_and_align_labels(self, examples):
        logger.debug("type(examples)=%s", type(examples))
        logger.debug("type(examples[0])=%s", type(examples[0]))
        logger.debug("type(examples[0][0])=%s", type(examples[0][0]))
        tokenized_inputs = self.tokenizer(
            examples, truncation=True, is_split_into_words=True
        )

        labels = []
        for i, label in enumerate(examples):
            # logger.debug("i=%d, label=%s, len(labels)=%d", i, label, len(labels))
            word_ids = tokenized_inputs.word_ids(
                batch_index=i
            )  # Map tokens to their respective word.
            previous_word_idx = None
            label_ids = []
            for word_idx in word_ids:  # Set the special tokens to -100.
                # logger.debug("word_idx = %s", word_idx)
                if word_idx is None:
                    label_ids.append(-100)
                elif (
                    word_idx != previous_word_idx
                ):  # Only label the first token of a given word.
                    # logger.debug("FIRST TOKEN: label[word_idx]=%s", label[word_idx])
                    label_ids.append((word_idx, label[word_idx]))
                else:
                    # logger.debug("      TOKEN: label[word_idx]=%s", label[word_idx])

                    label_ids.append(-100)
                previous_word_idx = word_idx
            labels.append(label_ids)

        tokenized_inputs["labels"] = labels
        return tokenized_inputs


TAGS = {"PER": "PRS"}


def translate_tag(tag: str) -> str:
    return TAGS.get(tag) or tag
