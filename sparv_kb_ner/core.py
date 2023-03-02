from dataclasses import dataclass
from typing import Optional

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
    out_ne_type: Output = Output(
        "<token>:sparv_kb_ner.ne_type",
        cls="named_entity",
        description="Named entity segment types from KB-BERT-NER",
    ),
    out_ne_score: Output = Output(
        "<token>:sparv_kb_ner.ne_score",
        cls="named_entity",
        description="Named entity segment types from KB-BERT-NER",
    ),
    word: Annotation = Annotation("<token:word>"),
    sentence: Annotation = Annotation("<sentence>"),
):
    print("sparv_kb_ner")
    logger.debug("word: %s", word)
    # out_ne.write(["hello"])
    parse_kb_ner_output(
        sentence=sentence, word=word, out_ne_type=out_ne_type, out_ne_score=out_ne_score
    )
    # raise RuntimeError("impl")


def parse_kb_ner_output(
    sentence: Annotation, word: Annotation, out_ne_type: Output, out_ne_score: Output
):
    sentences, _orphans = sentence.get_children(word)
    token_word = list(word.read())
    sentences_to_tag = [
        TOK_SEP.join(token_word[token_index] for token_index in sent)
        for sent in sentences
    ]
    # stdout = run_nlp(stdin)
    out_type_annotation = word.create_empty_attribute()
    out_score_annotation = word.create_empty_attribute()
    for sent, sent_to_tag in zip(sentences, sentences_to_tag, strict=True):
        tagged_tokens = run_nlp_on_sentence(sent_to_tag)
        logger.debug("tagged_tokens = %s", tagged_tokens)
        logger.debug("sent = %s", sent)
        for token_index, tagged_token in zip(sent, tagged_tokens, strict=True):
            logger.debug(
                "token_index = %d, tagged_token = %s, token_work = %s",
                token_index,
                tagged_token,
                token_word[token_index],
            )
            # tag = tagged_token.strip().split(TAG_SEP)[TAG_COLUMN]
            # tag = tag_mapping.get(tag, tag)
            out_type_annotation[token_index] = tagged_token.tag or ""
            out_score_annotation[token_index] = tagged_token.score or ""

    out_ne_type.write(out_type_annotation)
    out_ne_score.write(out_score_annotation)


@dataclass
class TaggedToken:
    tag: Optional[str]
    score: Optional[float]


@dataclass
class Token:
    word: str
    entity: str
    start: int
    end: int
    score: float
    index: int


def run_nlp_on_sentence(sentence: str) -> list[TaggedToken]:
    tokens = []
    for token in nlp(sentence):
        logger.debug("nlp: token = %s", token)
        if token["word"].startswith("##"):
            logger.debug("found ## in %s", token["word"])
            tokens[-1].word += token["word"][2:]
            tokens[-1].end = token["end"]
        else:
            tokens.append(Token(**token))
        logger.debug("tokens[-1].word = %s", tokens[-1].word)
        logger.debug("tokens = %s", tokens)
    return interleave_tags_and_sentence(tokens, sentence)


def interleave_tags_and_sentence(
    tokens: list[Token], sentence: str
) -> list[TaggedToken]:
    logger.debug("tokens = %s", tokens)
    logger.debug("sentence = %s", sentence)
    tags = []
    end = len(sentence)
    curr: int = 0
    curr_token = 0
    while curr < end:
        if curr_token < len(tokens) and tokens[curr_token].start == curr:
            logger.debug(
                "word = %s, tag = %s",
                tokens[curr_token].word,
                tokens[curr_token].entity,
            )
            tags.append(
                TaggedToken(
                    tag=translate_tag(tokens[curr_token].entity),
                    score=tokens[curr_token].score,
                )
            )
            curr = find_word_ending(sentence, tokens[curr_token].end)
            curr_token += 1
        else:
            part_end = tokens[curr_token].start if curr_token < len(tokens) else end
            part = sentence[curr:part_end]
            logger.debug("part='%s'", part)
            if parts := part.strip():
                parts = parts.split(" ")
                logger.debug("parts=%s", parts)
                # print(f"{parts=}")
                for word in parts:
                    logger.debug("word = %s", word)
                    tags.append(TaggedToken(tag=None, score=None))
            curr = part_end
    return tags


def find_word_ending(sentence: str, token_end: int) -> int:
    """Find first whitespace from token_end or above."""
    while token_end < len(sentence) and sentence[token_end] != " ":
        token_end += 1
    return token_end


TAGS = {"PER": "PRS"}


def translate_tag(tag: str) -> str:
    return TAGS.get(tag) or tag
