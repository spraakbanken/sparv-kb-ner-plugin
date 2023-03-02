from sparv_kb_ner.core import Token, find_word_ending, interleave_tags_and_sentence
import pytest


SENTENCES = [
    "Ikea ( namnet är bildat av initialerna för Ingvar Kamprad Elmtaryd Agunnaryd ) är ett multinationellt möbelföretag som grundades 1943 av Ingvar Kamprad .",  # noqa: E501
    "Under verksamhetsåret 2012 omsatte Ikeakoncernen 241 miljarder kronor .",
]


@pytest.mark.parametrize(
    "tokens, sentence_index, expected",
    [
        (
            [
                Token(
                    word="Ikea", entity="ORG", start=0, end=4, score=0.9993444, index=1
                ),
                Token(
                    word="Ingvar",
                    entity="PER",
                    start=43,
                    end=49,
                    score=0.9993979,
                    index=10,
                ),
                Token(
                    word="Kamprad",
                    entity="PER",
                    start=50,
                    end=57,
                    score=0.99831116,
                    index=11,
                ),
                Token(
                    word="Elmtaryd",
                    entity="PER",
                    start=58,
                    end=66,
                    score=0.7953129,
                    index=12,
                ),
                Token(
                    word="Agunnaryd",
                    entity="LOC",
                    start=67,
                    end=76,
                    score=0.9898454,
                    index=15,
                ),
                Token(
                    word="1943",
                    entity="TME",
                    start=129,
                    end=133,
                    score=0.9958897,
                    index=28,
                ),
                Token(
                    word="Ingvar",
                    entity="PER",
                    start=137,
                    end=143,
                    score=0.99676883,
                    index=30,
                ),
                Token(
                    word="Kamprad",
                    entity="PER",
                    start=144,
                    end=151,
                    score=0.9973974,
                    index=31,
                ),
            ],
            0,
            [
                "ORG",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "PRS",
                "PRS",
                "PRS",
                "LOC",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "TME",
                "",
                "PRS",
                "PRS",
                "",
            ],
        ),
        (
            [
                Token(
                    word="verksamhetsåret",
                    entity="TME",
                    start=6,
                    end=21,
                    score=0.9601936,
                    index=2,
                ),
                Token(
                    word="2012",
                    entity="TME",
                    start=22,
                    end=26,
                    score=0.99914443,
                    index=4,
                ),
                Token(
                    word="Ikea",
                    entity="ORG",
                    start=35,
                    end=39,
                    score=0.99542964,
                    index=6,
                ),
                Token(
                    word="241",
                    entity="MSR",
                    start=49,
                    end=52,
                    score=0.99984705,
                    index=8,
                ),
                Token(
                    word="miljarder",
                    entity="MSR",
                    start=53,
                    end=62,
                    score=0.9998272,
                    index=9,
                ),
                Token(
                    word="kronor",
                    entity="MSR",
                    start=63,
                    end=69,
                    score=0.99974865,
                    index=10,
                ),
            ],
            1,
            ["", "TME", "TME", "", "ORG", "MSR", "MSR", "MSR", ""],
        ),
    ],
)
def test_interleave_tags_and_sentence(
    tokens: list[Token], sentence_index: int, expected: list[str]
):
    tags = [
        t.tag or ""
        for t in interleave_tags_and_sentence(tokens, SENTENCES[sentence_index])
    ]
    assert tags == expected


@pytest.mark.parametrize(
    "sentence_index, token_end, expected", [(1, 21, 21), (1, 39, 48)]
)
def test_find_word_ending(sentence_index: int, token_end: int, expected: int) -> None:
    sentence = SENTENCES[sentence_index]

    assert find_word_ending(sentence, token_end) == expected
    assert sentence[find_word_ending(sentence, token_end)] == " "
