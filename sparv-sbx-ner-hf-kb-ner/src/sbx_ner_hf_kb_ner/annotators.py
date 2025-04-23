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

from sbx_ner_hf_kb_ner import huggingface_ner_pipeline

logger = get_logger(__name__)


SENT_SEP = "\n"
TOK_SEP = " "

@annotator(
    "Named entity tagging with KB-BERT-NER",
    language=["swe"],
    preloader=huggingface_ner_pipeline.load_model,
    # preloader_params=["pipeline", "model_name", "tokenizer_name"],
    preloader_target="model_preloaded",
)
def annotate_sbx_ner_hf_kb_ner(
    out_ne_type: Output = Output(
        "<token>:sbx_ner_hf_kb_ner.ne-type--hf-kb-ner",
        cls="named_entity",
        description="Named entity segment types from KB-BERT-NER",
    ),
    out_ne_score: Output = Output(
        "<token>:sbx_ner_hf_kb_ner.ne-score--hf-kb-ner",
        cls="named_entity",
        description="Named entity segment types from KB-BERT-NER",
    ),
    word: Annotation = Annotation("<token:word>"),
    sentence: Annotation = Annotation("<sentence>"),
    model_preloaded: Optional[Any] = None,
):
    logger.info("huggingface_ner_pipeline")

    if model_preloaded:
        ner_pipeline = model_preloaded
    else:
        logger.info(
            "loading huggingface_ner_pipeline"
        )
        ner_pipeline = huggingface_ner_pipeline.load_model()

    ner_pipeline.run(sentence, word, out_ne_type, out_ne_score)


