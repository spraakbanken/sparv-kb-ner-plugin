from typing import Optional, Tuple
from sparv_kb_ner.core import (
    # Token,
    find_word_ending,
    # interleave_tags_and_sentence,
    interleave_tags_and_tokens,
    run_nlp_on_sentence,
    # run_nlp_on_tokens,
)
import pytest


SENTENCES = {
    "ikea": "Ikea ( namnet är bildat av initialerna för Ingvar Kamprad Elmtaryd Agunnaryd ) är ett multinationellt möbelföretag som grundades 1943 av Ingvar Kamprad .",  # noqa: E501
    "verksamhetsåret": "Under verksamhetsåret 2012 omsatte Ikeakoncernen 241 miljarder kronor .",  # noqa: E501
    "kammerling": "– Jag tycker att Sveriges landslag ska vara nöjda , säger experten Anna-Karin Kammerling till Sveriges Radio .",  # noqa: E501
    "gruppen": "Gruppen föreslår ändringar i reglerna för 2,7 miljarder kronor .",
    "belarusen": "Poliser grep sedan två personer på flygplanet , belarusen Roman Protasevitj och hans flickvän Sofia Sapega .",  # noqa: E501
    "det-börjar": "Den börjar klockan 19.15 .",
    "encrochat": "Det programmet heter Encrochat .",
    "artisterna": "Det är till exempel artisterna Tusse , Dotter och Kikki Danielsson .",  # noqa: E501
    "street-race": "Filmerna handlar bland annat om olagliga tävlingar med bilar som kallas street-race .",  # noqa: E501
    "kvinnolobby": "Det säger Clara Berglund som är ledare för gruppen Sveriges kvinnolobby .",  # noqa: E501
    "internet": "Det går också att kolla klockan på internet på sajten 90510.se .",
}


# @pytest.mark.parametrize(
#     "tokens, sentence_name, expected",
#     [
#         (
#             [
#                 Token(
#                     word="Ikea", entity="ORG", start=0, end=4, score=0.9993444, index=1
#                 ),
#                 Token(
#                     word="Ingvar",
#                     entity="PER",
#                     start=43,
#                     end=49,
#                     score=0.9993979,
#                     index=10,
#                 ),
#                 Token(
#                     word="Kamprad",
#                     entity="PER",
#                     start=50,
#                     end=57,
#                     score=0.99831116,
#                     index=11,
#                 ),
#                 Token(
#                     word="Elmtaryd",
#                     entity="PER",
#                     start=58,
#                     end=66,
#                     score=0.7953129,
#                     index=12,
#                 ),
#                 Token(
#                     word="Agunnaryd",
#                     entity="LOC",
#                     start=67,
#                     end=76,
#                     score=0.9898454,
#                     index=15,
#                 ),
#                 Token(
#                     word="1943",
#                     entity="TME",
#                     start=129,
#                     end=133,
#                     score=0.9958897,
#                     index=28,
#                 ),
#                 Token(
#                     word="Ingvar",
#                     entity="PER",
#                     start=137,
#                     end=143,
#                     score=0.99676883,
#                     index=30,
#                 ),
#                 Token(
#                     word="Kamprad",
#                     entity="PER",
#                     start=144,
#                     end=151,
#                     score=0.9973974,
#                     index=31,
#                 ),
#             ],
#             "ikea",
#             [
#                 "ORG",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "PRS",
#                 "PRS",
#                 "PRS",
#                 "LOC",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "TME",
#                 "",
#                 "PRS",
#                 "PRS",
#                 "",
#             ],
#         ),
#         (
#             [
#                 Token(
#                     word="verksamhetsåret",
#                     entity="TME",
#                     start=6,
#                     end=21,
#                     score=0.9601936,
#                     index=2,
#                 ),
#                 Token(
#                     word="2012",
#                     entity="TME",
#                     start=22,
#                     end=26,
#                     score=0.99914443,
#                     index=4,
#                 ),
#                 Token(
#                     word="Ikea",
#                     entity="ORG",
#                     start=35,
#                     end=39,
#                     score=0.99542964,
#                     index=6,
#                 ),
#                 Token(
#                     word="241",
#                     entity="MSR",
#                     start=49,
#                     end=52,
#                     score=0.99984705,
#                     index=8,
#                 ),
#                 Token(
#                     word="miljarder",
#                     entity="MSR",
#                     start=53,
#                     end=62,
#                     score=0.9998272,
#                     index=9,
#                 ),
#                 Token(
#                     word="kronor",
#                     entity="MSR",
#                     start=63,
#                     end=69,
#                     score=0.99974865,
#                     index=10,
#                 ),
#             ],
#             "verksamhetsåret",
#             ["", "TME", "TME", "", "ORG", "MSR", "MSR", "MSR", ""],
#         ),
#         (
#             [
#                 Token(
#                     word="Sveriges",
#                     entity="LOC",
#                     start=17,
#                     end=25,
#                     score=0.6952171,
#                     index=5,
#                 ),
#                 Token(
#                     word="landslag",
#                     entity="ORG",
#                     start=26,
#                     end=34,
#                     score=0.5673877,
#                     index=6,
#                 ),
#                 Token(
#                     word="Anna-Karin",
#                     entity="PER",
#                     start=67,
#                     end=77,
#                     score=0.99983525,
#                     index=13,
#                 ),
#                 Token(
#                     word="Kammerling",
#                     entity="PER",
#                     start=78,
#                     end=88,
#                     score=0.99981195,
#                     index=16,
#                 ),
#                 Token(
#                     word="Sveriges",
#                     entity="ORG",
#                     start=94,
#                     end=102,
#                     score=0.9979777,
#                     index=20,
#                 ),
#                 Token(
#                     word="Radio",
#                     entity="ORG",
#                     start=103,
#                     end=108,
#                     score=0.9971181,
#                     index=21,
#                 ),
#             ],
#             "kammerling",
#             [
#                 "",
#                 "",
#                 "",
#                 "",
#                 "LOC",
#                 "ORG",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "PRS",
#                 "PRS",
#                 "",
#                 "ORG",
#                 "ORG",
#                 "",
#             ],
#         ),
#         (
#             [
#                 Token(
#                     word="2,7", entity="MSR", start=42, end=45, score=0.9998472, index=7
#                 ),
#                 Token(
#                     word="miljarder",
#                     entity="MSR",
#                     start=46,
#                     end=55,
#                     score=0.99979943,
#                     index=10,
#                 ),
#                 Token(
#                     word="kronor",
#                     entity="MSR",
#                     start=56,
#                     end=62,
#                     score=0.9997632,
#                     index=11,
#                 ),
#             ],
#             "gruppen",
#             ["", "", "", "", "", "", "MSR", "MSR", "MSR", ""],
#         ),
#         (
#             [
#                 Token(
#                     word="Roman",
#                     entity="PER",
#                     start=58,
#                     end=63,
#                     score=0.99971503,
#                     index=13,
#                 ),
#                 Token(
#                     word="Protasevitj",
#                     entity="PER",
#                     start=64,
#                     end=75,
#                     score=0.9995414,
#                     index=14,
#                 ),
#                 Token(
#                     word="Sofia",
#                     entity="PER",
#                     start=94,
#                     end=99,
#                     score=0.99979895,
#                     index=21,
#                 ),
#                 Token(
#                     word="Sapega",
#                     entity="PER",
#                     start=100,
#                     end=106,
#                     score=0.9995235,
#                     index=22,
#                 ),
#             ],
#             "belarusen",
#             [
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "",
#                 "PRS",
#                 "PRS",
#                 "",
#                 "",
#                 "",
#                 "PRS",
#                 "PRS",
#                 "",
#             ],
#         ),
#         (
#             [
#                 Token(
#                     word="klockan",
#                     entity="TME",
#                     start=11,
#                     end=18,
#                     score=0.9978672,
#                     index=3,
#                 ),
#                 Token(
#                     word="19.15",
#                     entity="TME",
#                     start=19,
#                     end=24,
#                     score=0.99645376,
#                     index=4,
#                 ),
#             ],
#             "det-börjar",
#             ["", "", "TME", "TME", ""],
#         ),
#     ],
# )
# def test_interleave_tags_and_sentence(
#     tokens: list[Token], sentence_name: str, expected: list[str]
# ):
#     tags = [
#         t.tag or ""
#         for t in interleave_tags_and_sentence(tokens, SENTENCES[sentence_name])
#     ]
#     assert tags == expected


@pytest.mark.parametrize(
    "sentence_name, token_end, expected",
    [("verksamhetsåret", 21, 21), ("verksamhetsåret", 39, 48), ("encrochat", 28, 30)],
)
def test_find_word_ending(sentence_name: str, token_end: int, expected: int) -> None:
    sentence = SENTENCES[sentence_name]

    assert find_word_ending(sentence, token_end) == expected
    assert sentence[find_word_ending(sentence, token_end)] == " "


# @pytest.mark.parametrize(
#     "sentence_name, expected_tags",
#     [
#         (
#             "belarusen",
#             [
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 "PRS",
#                 "PRS",
#                 None,
#                 None,
#                 None,
#                 "PRS",
#                 "PRS",
#                 None,
#             ],
#         ),
#         ("det-börjar", [None, None, "TME", "TME", None]),
#         # ("encrochat", [None, None, None, "PRS", None]),
#         (
#             "artisterna",
#             [
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 "PRS",
#                 "PRS",  # TODO Should this be None?,
#                 "PRS",
#                 "PRS",  # TODO Should this be None?,
#                 "PRS",
#                 "PRS",
#                 None,
#             ],
#         ),
#         (
#             "street-race",
#             [
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 "EVN",
#                 None,
#             ],
#         ),
#         (
#             "kvinnolobby",
#             [None, None, "PRS", "PRS", None, None, None, None, None, "LOC", None, None],
#         ),
#         (
#             "internet",
#             [
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 None,
#                 "WRK",
#                 None,
#             ],
#         ),
#     ],
# )
# def test_interleave_tags_and_sentence_run_nlp_on_sentence(
#     sentence_name: str, expected_tags: list[Optional[str]]
# ) -> None:
#     sentence = SENTENCES[sentence_name]

#     result = interleave_tags_and_sentence(run_nlp_on_sentence(sentence), sentence)
#     tags = [t.tag for t in result]
#     assert tags == expected_tags


@pytest.mark.parametrize(
    "sentence_name, expected_tags",
    [
        (
            "belarusen",
            [
                (9, "PRS"),
                (10, "PRS"),
                (14, "PRS"),
                (15, "PRS"),
            ],
        ),
        ("det-börjar", [(2, "TME"), (3, "TME")]),
        # ("encrochat", [None, None, None, "PRS", None]),
        (
            "artisterna",
            [
                (5, "PRS"),
                (6, "PRS"),  # TODO Should this be None?,
                (7, "PRS"),
                (8, "PRS"),  # TODO Should this be None?,
                (9, "PRS"),
                (10, "PRS"),
            ],
        ),
        (
            "street-race",
            [
                (
                    11,
                    "EVN",
                )
            ],
        ),
        (
            "kvinnolobby",
            [(2, "PRS"), (3, "PRS"), (9, "LOC")],
        ),
        (
            "internet",
            [
                (10, "WRK"),
            ],
        ),
    ],
)
def test_interleave_tags_and_tokens_run_nlp_on_sentence(
    sentence_name: str, expected_tags: list[Tuple[int, str]]
) -> None:
    sentence = SENTENCES[sentence_name]
    token_word = sentence.split(" ")
    sent = list(range(len(token_word)))
    result = interleave_tags_and_tokens(
        run_nlp_on_sentence(sentence), token_word, sent, sentence
    )
    tags = [(t[0], t[1]) for t in result]
    assert tags == expected_tags
