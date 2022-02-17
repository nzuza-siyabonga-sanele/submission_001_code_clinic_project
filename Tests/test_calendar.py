from datetime import date, datetime
from time import time
# from authentication import authentication
import unittest
from tabulate import tabulate
import sys
from io import StringIO
from unittest.mock import patch
from bookings.calendars import calendar

class CalendarTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO('2022-02-22\n8:30'))
    def test_convert_to_RFC_datetime(self):
        dt = calendar.convert_to_RFC_datetime(2022,2,22,8,0)
        self.assertEqual("""2022-02-22T06:00:00Z""",dt)


    def test_get_code_clinic_calendar(self):
        pass

    
    def test_get_user_calendar(self):
        pass


    def test_validate_date(self):
        date = calendar.validate_date('2022-2-22') 
        self.assertEqual("2022-2-22", date)


    def test_validate_time(self):
        time = calendar.validate_time("8:00")
        self.assertEqual("8:00", time)
