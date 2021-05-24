class Clock:
    def __init__(self, hour, minute):
        # Parses hours to (hours, minutes).
        parsed_minutes = self.__parse_minutes(minute)
        hour += parsed_minutes[0]

        # Sets minute.
        self.__minute(parsed_minutes[1])

        # Sets hour.
        self.__hour(self.__parse_hours(hour))

    def __repr__(self, hour=None, minute=None):
        # Returns given hour:minute.
        if hour != None and minute != None:
            return "{:02}:{:02}".format(hour, minute)

        # Returns clock hour:minute.
        return "{:02}:{:02}".format(self.hour, self.minute)

    def __eq__(self, other):
        # Compares against other clock.
        return self.__repr__() == other.__repr__()

    def __add__(self, minutes):
        # Adds minutes to clock.
        parsed_minutes = self.__parse_minutes(self.__minute() + minutes)
        new_minute = parsed_minutes[1]
        new_hour = self.__parse_hours(self.__hour() + parsed_minutes[0])

        return self.__repr__(new_hour, new_minute)

    def __sub__(self, minutes):
        # Substracts minutes to clock.
        parsed_minutes = self.__parse_minutes(self.__minute() - minutes)
        new_minute = parsed_minutes[1]
        new_hour = self.__parse_hours(self.hour + parsed_minutes[0])

        return self.__repr__(new_hour, new_minute)

    def __minute(self, minute=None):
        # Minute setter/getter.
        if minute != None:
            self.minute = minute
            return
        return self.minute

    def __hour(self, hour=None):
        # Hour setter/getter.
        if hour != None:
            self.hour = hour
            return
        return self.hour

    def __parse_minutes(self, minutes):
        # Minutes parser.
        h = minutes // 60
        m = minutes % 60
        if minutes < 0:
            if minutes > 60 and m != 0:
                h -= 1
                minutes = 60 - m
        else:
            minutes = minutes % 60
        return (h, m)

    def __parse_hours(self, hours):
        # Hours parser.
        if hours < 0:
            while hours < 0:
                hours += 24
            return hours

        while hours > 0:
            hours -= 24

        if hours == 0:
            return hours

        return 24 - (hours * -1)
