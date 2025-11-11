from sparv.api import Config
from sparv_kb_ner import (
    custom_ner_pipeline,
    annotators,
    ner_pipeline,
    huggingface_ner_pipeline,
)


__all__ = [
    "custom_ner_pipeline",
    "annotators",
    "ner_pipeline",
    "huggingface_ner_pipeline",
]

__description__ = "Using KB NER"

__config__ = [
    Config("sparv_kb_ner.model", description="huggingface NER model"),
    Config("sparv_kb_ner.tokenizer", description="HuggingFace NER tokenizer"),
    Config("sparv_kb_ner.pipeline", description="HuggingFace pipeline to use"),
]
