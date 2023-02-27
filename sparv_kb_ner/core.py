from dataclasses import dataclass

from sparv.api import annotator, get_logger, Output, Annotation

from transformers import pipeline


logger = get_logger(__name__)


SENT_SEP = "\n"
TOK_SEP = " "


nlp = pipeline(
    "ner",
    model="KBLab/bert-base-swedish-cased-ner",
    tokenizer="KBLab/bert-base-swedish-cased-ner",
)


@annotator("Named entity tagging with KB-BERT-NER", language=["swe"])
def annotate(
    out_ne: Output = Output(
        "<token>:sparv_kb_ner.kb-ne",
        cls="named_entity",
        description="Named entity segments from KB-BERT-NER",
    ),
    word: Annotation = Annotation("<token:word>"),
    sentence: Annotation = Annotation("<sentence>"),
):
    print("sparv_kb_ner")
    logger.debug("word: %s", word)
    # out_ne.write(["hello"])
    parse_kb_ner_output(sentence=sentence, word=word, out_ne=out_ne)
    # raise RuntimeError("impl")


def parse_kb_ner_output(sentence: Annotation, word: Annotation, out_ne: Output):
    sentences, _orphans = sentence.get_children(word)
    token_word = list(word.read())
    sentences_to_tag = [
        TOK_SEP.join(token_word[token_index] for token_index in sent)
        for sent in sentences
    ]
    # stdout = run_nlp(stdin)
    out_annotation = word.create_empty_attribute()
    for sent, sent_to_tag in zip(sentences, sentences_to_tag):
        tagged_tokens = run_nlp_on_sentence(sent_to_tag)
        logger.debug("tagged_tokens = %s", tagged_tokens)
        for token_index, tagged_token in zip(sent, tagged_tokens):
            logger.debug(
                "token_index = %d, tagged_token = %s", token_index, tagged_token
            )
            # tag = tagged_token.strip().split(TAG_SEP)[TAG_COLUMN]
            # tag = tag_mapping.get(tag, tag)
            out_annotation[token_index] = tagged_token

    out_ne.write(out_annotation)


@dataclass
class Token:
    word: str
    entity: str
    start: int
    end: int
    score: float
    index: int


def run_nlp_on_sentence(sentence: str) -> list[str]:
    tokens = []
    for token in nlp(sentence):
        if token["word"].startswith("##"):
            tokens[-1].word += token["word"][2:]
            tokens[-1].end = token["end"]
        else:
            tokens.append(Token(**token))
    return interleave_tags_and_sentence(tokens, sentence)


def interleave_tags_and_sentence(tokens: list[Token], sentence: str) -> list[str]:
    tags = []
    end = len(sentence)
    curr: int = 0
    curr_token = 0
    while curr < end:
        # print(f"{curr=}, {end=}, {curr_token=}")
        if curr_token < len(tokens) and tokens[curr_token].start == curr:
            logger.debug(
                "word = %s, tag = %s",
                tokens[curr_token].word,
                tokens[curr_token].entity,
            )
            tags.append(tokens[curr_token].entity)
            curr = tokens[curr_token].end
            curr_token += 1
        else:
            part_end = tokens[curr_token].start if curr_token < len(tokens) else end
            part = sentence[curr:part_end]
            logger.debug("part='%s'", part)
            parts = part.strip()
            if parts:
                parts = parts.split(" ")
                logger.debug("parts=%s", parts)
                # print(f"{parts=}")
                for word in parts:
                    logger.debug("word = %s", word)
                    tags.append("")
            curr = part_end
    return tags
