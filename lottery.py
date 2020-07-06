# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

import pytz
from dateutil.parser import parse


class NationalLottery:
    current_date = None
    lottery_date = None

    def __init__(self, force_date=None):
        """
        Init method to set up initial variables.
        :param force_date: (str) Optional. Date in string format assuming date is in Canada/Central timezone.
        """
        if force_date:
            self.current_date = parse(force_date).astimezone(pytz.utc)
        else:
            # Set now in Canada/Central as default date.
            self.current_date = datetime.now(pytz.timezone("Canada/Central")).astimezone(pytz.utc)

        # Calculate the next lottery date.
        self.next_lottery_date()

    def __str__(self):
        return f"Next lottery day: {self.lottery_date.strftime('%Y-%m-%d %H:%M:%S')}"

    def next_lottery_date(self):
        """
        Method to calculate the next lottery day based on the provided date.
        """
        edge_time = datetime.now().replace(hour=21, minute=30, second=0, microsecond=0).time()

        if self.current_date.weekday() < 1 or self.current_date.weekday() > 6 or (
                self.current_date.weekday() == 1 and self.current_date.time() <= edge_time):
            self.lottery_date = self.current_date + timedelta((1 - self.current_date.weekday()) % 7)

        else:
            self.lottery_date = self.current_date + timedelta((6 - self.current_date.weekday()) % 7)

        self.lottery_date = self.lottery_date.replace(hour=21, minute=30, second=0, microsecond=0)


# Define the test cases.
tests = [None, "2020-07-06T09:50:00", "2020-07-07T09:50:00", "2020-07-10T09:50:00", "2020-07-10T21:30:01"]

# Run the tests.
for i, test in enumerate(tests):
    print(f"Running test {i + 1}...")
    nt = NationalLottery(test)
    print(nt)
