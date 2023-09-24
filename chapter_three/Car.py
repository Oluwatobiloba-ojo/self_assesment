class Car:
    def __init__(self, model, year, price):
        self._model = model
        self._year = year
        self._price = price

    def set_model(self, model):
        self._model = model

    def get_model(self):
        return self._model

    def set_year(self, year):
        self._year = year

    def get_year(self):
        return self._year

    def set_price(self, price):
        if price > 0:
            self._price = price

    def get_price(self):
        return self._price

    def discount(self, percentage):
        ROI = self._price * (percentage / 100)
        self._price = self._price - ROI

