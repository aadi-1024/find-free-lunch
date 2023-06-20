from ffl.BaseBenchmark import _BaseBenchmark
from sklearn.metrics import f1_score


class ClassificationBenchmark(_BaseBenchmark):
    def __init__(self, X=None, y=None, val_X=None, val_y=None, models=None):
        super().__init__(X, y, val_X, val_y, models)

    def benchmark(self, metric: callable = f1_score, **kwargs) -> dict:
        for i in self._models:
            self._scores[i.__class__.__name__] = metric(self._val_y, i.predict(self._val_X), **kwargs)

        return self._scores
