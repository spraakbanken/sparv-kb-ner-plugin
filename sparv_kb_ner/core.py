from dataclasses import dataclass
from typing import Iterable, Optional, Tuple
import xml.sax.saxutils

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
    # sentences_to_tag = [
    #     TOK_SEP.join(token_word[token_index] for token_index in sent)
    #     for sent in sentences
    # ]
    # Escape <, > and &
    # sentences_to_tag = xml.sax.saxutils.escape(sentences_to_tag)
    # stdout = run_nlp(stdin)
    out_type_annotation = word.create_empty_attribute()
    out_score_annotation = word.create_empty_attribute()
    # for sent, sent_to_tag in zip(sentences, sentences_to_tag, strict=True):
    for sent in sentences:
        sent_to_tag = TOK_SEP.join(token_word[token_index] for token_index in sent)
        # tagged_tokens = interleave_tags_and_tokens(
        #     run_nlp_on_sentence(sent_to_tag), token_word, sent, sent_to_tag
        # )
        # tagged_tokens = run_nlp_on_tokens(token_word, sent)
        # logger.debug("tagged_tokens = %s", tagged_tokens)
        # logger.debug("sent = %s", sent)
        # for token_index, tagged_token in zip(sent, tagged_tokens, strict=True):
        for token_index, tag, score in interleave_tags_and_tokens(
            run_nlp_on_sentence(sent_to_tag), token_word, sent, sent_to_tag
        ):
            # logger.debug(
            #     "token_index = %d, tagged_token = (%s,%s), token_word = %s",
            #     token_index,
            #     tag,
            #     score,
            #     token_word[token_index],
            # )
            # tag = tagged_token.strip().split(TAG_SEP)[TAG_COLUMN]
            # tag = tag_mapping.get(tag, tag)
            out_type_annotation[token_index] = tag
            out_score_annotation[token_index] = score

    logger.info("writing annotations")
    out_ne_type.write(out_type_annotation)
    out_ne_score.write(out_score_annotation)


# @dataclass
# class TaggedToken:
#     tag: Optional[str]
#     score: Optional[float]

#     @classmethod
#     def default(cls) -> "TaggedToken":
#         return cls(tag=None, score=None)


# @dataclass
# class Token:
#     word: str
#     entity: str
#     start: int
#     end: int
#     score: float
#     index: int


def run_nlp_on_sentence(sentence: str) -> list[dict]:
    logger.info("run_nlp_on_sentence(len(sentence)='%d') called", len(sentence))
    tokens = []
    # linking_token = ""
    found_link = False
    for token in nlp(sentence):
        # logger.debug("nlp: token = %s", token)
        if token["word"].startswith("##"):
            # logger.debug("found ## in %s", token["word"])
            if tokens and token["start"] == tokens[-1]["end"]:
                tokens[-1]["word"] += token["word"][2:]
                tokens[-1]["end"] = token["end"]
            # else:
            #     logger.info(
            #         "found ## in '%s' (start=%d, end=%d) but no prev token, skipping ... ",
            #         token["word"],
            #         token["start"],
            #         token["end"],
            #     )
            # tokens.append(Token(**token))
        elif found_link:
            # logger.debug("found '%s' before word '%s'", linking_token, token["word"])
            found_link = False
            if token["start"] == tokens[-1]["end"]:
                tokens[-1]["word"] += token["word"]
                tokens[-1]["end"] = token["end"]
                # amend_token_to_last(token, tokens)
            else:
                tokens.append(token)
        elif token["word"] in [",", ".", "-"]:
            # linking_token = token["word"]
            # logger.debug("found '%s'", linking_token)
            found_link = True
            if token["start"] == tokens[-1]["end"]:
                tokens[-1]["word"] += token["word"]
                tokens[-1]["end"] = token["end"]
                # amend_token_to_last(token, tokens)
            else:
                tokens.append(token)
        else:
            tokens.append(token)
        # logger.debug("tokens[-1].word = %s", tokens[-1].word)
        # logger.debug("tokens = %s", tokens)
    return tokens


def amend_token_to_last(token, tokens):
    # logger.debug("adding '%s' to last word %s", token["word"], tokens[-1]["word"])
    tokens[-1]["word"] += token["word"]
    tokens[-1]["end"] = token["end"]


def interleave_tags_and_tokens(
    tokens: list[dict], token_word: list[str], sent: list[int], sentence: str
) -> Iterable[Tuple[int, str, str]]:
    # ) -> Iterable[TaggedToken]:
    logger.info("interleave_tags_and_tokens.tokens = %s", tokens)
    # logger.debug("interleave_tags_and_tokens.sentence = %s", sentence)
    curr_token = 0
    if curr_token >= len(tokens):
        return
    end = len(sentence)
    curr_sent = 0
    curr_word_start = 0
    curr_word_end = len(sentence)
    token_start = tokens[curr_token]["start"]
    for curr_sent in sent:
        curr_word_end = curr_word_start + len(token_word[curr_sent])

        # logger.debug(
        #     "curr_word = '%s' [%d:%d] (%s), curr_token = '%s' [%d:%d]",
        #     curr_word,
        #     curr_word_start,
        #     curr_word_end,
        #     sentence[curr_word_start:curr_word_end],
        #     tokens[curr_token]["word"] if curr_token < len(tokens) else "",
        #     token_start,
        #     token_end,
        # )
        # have we found curr_token?
        if curr_word_start <= token_start < curr_word_end:
            # if curr_word_start == token_start:
            #     logger.debug(
            #         "Matched token '%s' <%s> starting at %d",
            #         curr_word,
            #         tokens[curr_token]["entity"],
            #         curr_word_start,
            #     )
            # else:
            #     logger.info(
            #         "Partial matched of token '%s' [%d:%d] <%s> in word '%s'",
            #         tokens[curr_token]["word"],
            #         token_start,
            #         token_end,
            #         tokens[curr_token]["entity"],
            #         curr_word,
            #     )
            yield (
                curr_sent,
                translate_tag(tokens[curr_token]["entity"]),
                str(tokens[curr_token]["score"]),
            )
            # yield TaggedToken(
            #     tag=translate_tag(tokens[curr_token].entity),
            #     score=tokens[curr_token].score,
            # )
            curr_token += 1
            if curr_token >= len(tokens):
                break
            token_start = tokens[curr_token]["start"]
        # else:
        #     yield ("", "")
        # yield TaggedToken.default()
        # update curr_word
        curr_word_start += len(token_word[curr_sent]) + 1
        # curr_sent += 1


# def interleave_tags_and_sentence(
#     tokens: list[Token], sentence: str
# ) -> list[TaggedToken]:
#     logger.info("tokens = %s", tokens)
#     logger.debug("sentence = %s", sentence)
#     tags = []
#     end = len(sentence)
#     curr: int = 0
#     curr_token = 0
#     while curr < end:
#         if curr_token < len(tokens) and tokens[curr_token].start == curr:
#             logger.debug(
#                 "word = %s, tag = %s",
#                 tokens[curr_token].word,
#                 tokens[curr_token].entity,
#             )
#             tags.append(
#                 TaggedToken(
#                     tag=translate_tag(tokens[curr_token].entity),
#                     score=tokens[curr_token].score,
#                 )
#             )
#             curr = find_word_ending(sentence, tokens[curr_token].end)
#             curr_token = find_next_token(tokens, curr_token, curr)

#         else:
#             # logger.debug(
#             #     "last_token=%d, last_token.end=%s, curr=%d, sentence[curr]=%s",
#             #     curr_token - 1,
#             #     tokens[curr_token - 1].end if curr_token > 0 else "NO",
#             #     curr,
#             #     sentence[curr],
#             # )
#             part_end = tokens[curr_token].start if curr_token < len(tokens) else end
#             part = sentence[curr:part_end]
#             logger.debug("part='%s'", part)
#             if parts := part.strip():
#                 parts = parts.split(" ")
#                 logger.debug("parts=%s", parts)
#                 # print(f"{parts=}")
#                 for word in parts:
#                     logger.debug("word = %s", word)
#                     tags.append(TaggedToken(tag=None, score=None))
#             curr = part_end
#     return tags


def find_word_ending(sentence: str, token_end: int) -> int:
    """Find first whitespace from token_end or above."""
    while token_end < len(sentence) and sentence[token_end] != " ":
        token_end += 1
    return token_end


def find_next_token(tokens: list, curr_token: int, curr: int) -> int:
    next_token = curr_token + 1
    while next_token < len(tokens) and tokens[next_token].start < curr:
        next_token += 1
    return next_token


TAGS = {"PER": "PRS"}


def translate_tag(tag: str) -> str:
    return TAGS.get(tag) or tag
