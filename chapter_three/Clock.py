class Clock:

    def __init__(self, hour, second, minute):
        self._hour = hour
        self._second = second
        self._minute = minute

    def set_minute(self, minute):
        if minute < 60:
            self._minute = minute

    def get_minute(self):
        return self._minute

    def set_hour(self, hour):
        if hour < 24:
            self._hour = hour

    def get_hour(self):
        return self._hour

    def set_second(self, second):
        if second < 60:
            self._second = second

    def get_second(self):
        return self._second

    def display(self):
        return f"{self._hour}:{self._minute}:{self._second}"

