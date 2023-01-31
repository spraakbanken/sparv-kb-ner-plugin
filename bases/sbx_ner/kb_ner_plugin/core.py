from sparv.api import annotator, get_logger, Output, Annotation


logger = get_logger(__name__)


@annotator("Named entity tagging with KB-BERT-NER", language=["swe"])
def annotate(
    out_ne: Output = Output(
        "sbx_ner.ne",
        cls="named_entity",
        description="Named entity segments from KB-BERT-NER",
    ),
    sentence: Annotation = Annotation("<sentence>"),
):
    logger.error("msg")
    raise NotImplementedError("impl")
