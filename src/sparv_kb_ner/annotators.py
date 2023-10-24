from typing import Any, Iterable, Optional, Tuple
import itertools

from sparv.api import (
    Config,
    SparvErrorMessage,
    annotator,
    get_logger,
    Output,
    Annotation,
)

# from transformers import AutoTokenizer, AutoModelForTokenClassification
from sparv_kb_ner import huggingface_ner_pipeline, custom_ner_pipeline
from sparv_kb_ner.ner_pipeline import NerPipeline

logger = get_logger(__name__)


SENT_SEP = "\n"
TOK_SEP = " "


# tokenizer = AutoTokenizer.from_pretrained(
#     "KBLab/bert-base-swedish-lowermix-reallysimple-ner"
# )

# model = AutoModelForTokenClassification.from_pretrained(
#     "KBLab/bert-base-swedish-lowermix-reallysimple-ner"
# )
# nlp = pipeline(
#     "ner",
#     model="KBLab/bert-base-swedish-cased-ner",
#     tokenizer="KBLab/bert-base-swedish-cased-ner",
# )
def ner_pipeline_preloader(
    pipeline: str, model_name: Optional[str], tokenizer_name: Optional[str]
) -> NerPipeline:
    if not model_name:
        raise SparvErrorMessage("You must set 'sparv_kb_ner.model' in your config.")

    if not tokenizer_name:
        raise SparvErrorMessage("You must set 'sparv_kb_ner.tokenizer' in your config.")

    if pipeline == "huggingface_ner":
        return huggingface_ner_pipeline.load_model(model_name, tokenizer_name)
    elif pipeline == "custom_ner":
        return custom_ner_pipeline.load_model(model_name, tokenizer_name)
    else:
        raise SparvErrorMessage(f"Unknown pipeline '{pipeline}'")


@annotator(
    "Named entity tagging with KB-BERT-NER",
    language=["swe"],
    preloader=ner_pipeline_preloader,
    preloader_params=["pipeline", "model_name", "tokenizer_name"],
    preloader_target="model_preloaded",
)
def annotate_ner(
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
    pipeline: str = Config("sparv_kb_ner.pipeline", default="huggingface_ner"),
    model_name: Optional[str] = Config("sparv_kb_ner.model"),
    tokenizer_name: Optional[str] = Config("sparv_kb_ner.tokenizer"),
    model_preloaded: Optional[Any] = None,
):
    logger.info("huggingface_ner_pipeline")

    if model_preloaded:
        ner_pipeline = model_preloaded
    else:
        logger.info(
            "loading ner pipeline(pipeline=%s, model=%s, tokenizer=%s)",
            pipeline,
            model_name,
            tokenizer_name,
        )
        ner_pipeline = ner_pipeline_preloader(pipeline, model_name, tokenizer_name)

    ner_pipeline.run(sentence, word, out_ne_type, out_ne_score)


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
