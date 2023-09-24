class HealthRecords:

    def __init__(self, first_name, last_name, year_of_birth, month_of_birth, day_of_birth, height, weight, gender):
        self._first_name = first_name
        self._last_name = last_name
        self._year_of_birth = year_of_birth
        self._month_of_birth = month_of_birth
        self._day_of_birth = day_of_birth
        self._height = height
        self._weight = weight
        self._gender = gender

    def set_first_name(self, name):
        self._first_name = name

    def get_first_name(self):
        return self._first_name

    def set_last_name(self, name):
        self._last_name = name

    def get_last_name(self):
        return self._last_name

    def set_year_of_birth(self, year):
        self._year_of_birth = year

    def get_year_birth(self):
        return self._year_of_birth

    def set_month_of_birth(self, month_of_the_year):
        self._month_of_birth = month_of_the_year

    def get_month_birth(self):
        return self._month_of_birth

    def set_day_of_birth(self, day_of_birth):
        self._day_of_birth = day_of_birth

    def get_day_of_birth(self):
        return self._day_of_birth

    def set_height(self, height):
        self._height = height

    def get_height(self):
        return self._height

    def set_weight(self, weight):
        self._weight = weight

    def get_weight(self):
        return self._weight

    def set_gender(self, gender):
        self._gender = gender

    def get_gender(self):
        return self._gender

    def calculate_age(self):
        return 2023 - self._year_of_birth

    def maximum_heart_rate(self):
        return 220 - self.calculate_age()

    def calculate_target_heart_rate(self, percentage, percentage2):
        range1 = 0
        range2 = 0
        if percentage == 50 and percentage <= 55:
            range1 = self.maximum_heart_rate() * (percentage / 100)
        elif percentage <= 65:
            range1 = self.maximum_heart_rate() * (percentage / 100)

        if percentage2 <= 75:
            range2 = self.maximum_heart_rate() * (percentage2 / 100)
        elif percentage2 <= 85:
            range2 = self.maximum_heart_rate() * (percentage2 / 100)

        return f"{range1:.2f} - {range2:.2f}"

    def calculate_body_mass_index(self):
        result = (self._weight * 703) / (self._height * self._height)
        return f"{result:.2f}"
