# Base class for Classification and Regression Benchmarks
class _BaseBenchmark:
    def __init__(self, X=None, y=None, val_X=None, val_y=None, models: list[any] = None):
        self._X = X
        self._y = y
        self._val_X = val_X
        self._val_y = val_y
        self._models = models
        self._scores: dict = {}

    def benchmark(self, metric: callable) -> dict:
        pass

    def fit(self, X, y):
        self._X = X
        self._y = y
        for i in self._models:
            i.fit(self._X, self._y)

    def predict(self, X) -> dict:
        d: dict = {}
        for i in self._models:
            pred = i.predict(X)
            d[i.__class__.__name__] = pred
        return d
