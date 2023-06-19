from sklearn.metrics import mean_absolute_error, classification_report


class Benchmark:
    def __init__(self, cat: str = 'c', X=None, y=None, val_X=None, val_y=None, models: list[any] = None):
        self._X = X
        self._y = y
        self._val_X = val_X
        self._val_y = val_y
        self._models = models
        self._scores: dict = {}

        if cat.lower() == 'c' or cat.lower() == 'r':
            self._cat = cat.lower()
        else:
            raise ValueError
        # use c for classification and r for regression problems

    def calculate(self):
        self._scores = {}
        if self._cat == 'c':
            self._classification()
        else:
            self._regression()
        return self._scores

    def _classification(self):
        for i in self._models:
            i.fit(self._X, self._y)
            pred = i.predict(self._val_X)
            self._scores[i.__class__.__name__] = classification_report(self._val_y, pred)

    def _regression(self):
        for i in self._models:
            i.fit(self._X, self._y)
            pred = i.predict(self._val_X)
            self._scores[i.__class__.__name__] = mean_absolute_error(self._val_y, pred)
