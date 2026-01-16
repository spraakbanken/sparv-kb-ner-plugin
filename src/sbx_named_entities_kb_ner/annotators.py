import typing as t

from sparv.api import (
    Annotation,
    Config,
    Output,
    SparvErrorMessage,
    annotator,
    get_logger,
)
from transformers import NerPipeline

from sbx_named_entities_kb_ner.constants import PROJECT_NAME

logger = get_logger(__name__)


SENT_SEP = "\n"
TOK_SEP = " "


def ner_pipeline_preloader(pipeline: str) -> NerPipeline:
    from sbx_named_entities_kb_ner.custom_ner_pipeline import CustomNerPipeline
    from sbx_named_entities_kb_ner.huggingface_ner_pipeline import (
        HuggingFaceNerPipeline,
    )

    if pipeline == "huggingface_ner":
        return t.cast(NerPipeline, HuggingFaceNerPipeline())
    elif pipeline == "custom_ner":
        return t.cast(NerPipeline, CustomNerPipeline())
    else:
        raise SparvErrorMessage(f"Unknown pipeline '{pipeline}'")


@annotator(
    "Named entity tagging with KB-BERT-NER",
    language=["swe"],
    preloader=ner_pipeline_preloader,
    preloader_params=["pipeline"],
    preloader_target="model_preloaded",
    config=[
        Config(f"{PROJECT_NAME}.pipeline", description="HuggingFace pipeline to use"),
    ],
)
def annotate(
    out_ne_type: Output = Output(
        f"<token>:{PROJECT_NAME}.ne_type",
        cls="named_entity",
        description="Named entity segment types from KB-BERT-NER",
    ),
    out_ne_score: Output = Output(
        f"<token>:{PROJECT_NAME}.ne_score",
        cls="named_entity",
        description="Named entity segment types from KB-BERT-NER",
    ),
    word: Annotation = Annotation("<token:word>"),
    sentence: Annotation = Annotation("<sentence>"),
    pipeline: str = Config(f"{PROJECT_NAME}.pipeline", default="huggingface_ner"),
    model_preloaded: t.Any | None = None,
):
    logger.info("huggingface_ner_pipeline")

    if model_preloaded is not None:
        ner_pipeline: NerPipeline = t.cast(NerPipeline, model_preloaded)
    else:
        logger.info(
            "loading ner pipeline(pipeline=%s)",
            pipeline,
        )
        ner_pipeline: NerPipeline = ner_pipeline_preloader(pipeline)

    ner_pipeline.run(sentence, word, out_ne_type, out_ne_score)  # type: ignore[unresolved-attribute]


# @annotator("Named entity tagging with KB-BERT-NER", language=["swe"])
# def huggingface_ner_custom(
#     out_ne_type: Output = Output(
#         "<token>:huggingface_ner_custom.ne_type",
#         cls="named_entity",
#         description="Named entity segment types from KB-BERT-NER",
#     ),
#     out_ne_score: Output = Output(
#         "<token>:huggingface_ner_custom.ne_score",
#         cls="named_entity",
#         description="Named entity segment types from KB-BERT-NER",
#     ),
#     word: Annotation = Annotation("<token:word>"),
#     sentence: Annotation = Annotation("<sentence>"),
# ):
#     logger.info("huggingface_ner_custom")
#     logger.debug("word: %s", word)
