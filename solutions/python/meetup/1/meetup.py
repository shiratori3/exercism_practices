import calendar
from datetime import date


cal = calendar.Calendar()
teenthdays = (13, 14, 15, 16, 17, 18, 19)
monthweekindex = {
    "first": 0,
    "second": 1,
    "third": 2,
    "fourth": 3,
    "fifth": 4,
    "last": -1,
}
weekdayindex = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}


# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    calmonth = cal.monthdays2calendar(year, month)
    weekindex = monthweekindex.get(week)
    dayindex = weekdayindex.get(day_of_week)
    # drop first weekday and last weekday not in this month
    for index in (0, -1):
        for d in calmonth[index]:
            if d[0] == 0 and d[1] == dayindex:
                calmonth.pop(0 if index == 0 else len(calmonth) - 1)
                break
    if week == "teenth":
        for w in calmonth:
            for d in w:
                if d[0] in teenthdays and d[1] == dayindex:
                    return date(year, month, d[0])
    else:
        if weekindex == 4:
            if len(calmonth) < 5:
                raise MeetupDayException("That day does not exist.")
        for d in calmonth[weekindex]:
            if d[1] == dayindex:
                if not d[0]:
                    raise MeetupDayException("That day does not exist.")
                return date(year, month, d[0])
