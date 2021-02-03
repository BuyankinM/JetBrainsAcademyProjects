class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @classmethod
    def from_string(cls, time_string):
        hour, minute = time_string.split(":")
        return cls(hour, minute)
