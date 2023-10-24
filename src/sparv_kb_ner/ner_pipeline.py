import abc

from sparv.api import Output, Annotation


class NerPipeline(abc.ABC):
    @abc.abstractmethod
    def run(
        self,
        sentence: Annotation,
        word: Annotation,
        out_ne_type: Output,
        out_ne_score: Output,
    ) -> None:
        ...
