from sparv.api import annotator, get_logger, Output, Annotation


logger = get_logger(__name__)


@annotator("Named entity tagging with KB-BERT-NER", language=["swe"])
def annotate(
    out_ne: Output = Output(
        "sbx_ner.ne",
        cls="named_entity",
        description="Named entity segments from KB-BERT-NER",
    ),
    word: Annotation = Annotation("<token:word>"),
    sentence: Annotation = Annotation("<sentence>"),
    token: Annotation = Annotation("<token>"),
):
    print("sparv_kb_ner")
    logger.debug("msg")
    # out_ne.write(["hello"])
    sentences, _orphans = sentence.get_children(token, orphan_alert=True)
    parse_kb_ner_output(sentences=sentences, token=token, out_ne=out_ne)
    # raise RuntimeError("impl")


def parse_kb_ner_output(sentences: list, token: Annotation, out_ne):
    _token_spans = list(token.read_spans())
    out_ne.write([(0, 1)])
