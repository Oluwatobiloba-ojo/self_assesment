class Petrol:

    def __init__(self, location, types, quantity, price_per_litre, percentage_discount):
        self._location = location
        self._types = types
        self._quantity = quantity
        self._price_per_litre = price_per_litre
        self._percentage_discount = percentage_discount

    def set_location(self, location: str):
        self._location = location

    def get_location(self):
        return self._location

    def set_types(self, types):
        self._types = types

    def get_types(self):
        return self._types

    def calculate_quantity(self, quantity):
        self._quantity = quantity

    def get_quantity(self):
        return self._quantity

    def set_price_per_litre(self, price):
        self._price_per_litre = price

    def get_price(self):
        return self._price_per_litre

    def percentage_discount(self, discount):
        self._percentage_discount = discount

    def get_discount(self):
        return self._percentage_discount

    def get_purchase_amount(self):
        return (self._quantity * self._price_per_litre) - (self._percentage_discount / 100)
