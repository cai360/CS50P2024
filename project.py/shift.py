from calendar import Calendar
from calendar import TextCalendar
import csv
from tabulate import tabulate


c = Calendar()
f = TextCalendar()

class Shift:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.empty_calendar = c.monthdayscalendar(year, month)


def main():

    shift = Shift(2024, 11)


if __name__ == "__main__":
    main()



