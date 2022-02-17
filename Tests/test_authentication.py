# from cgi import test
import unittest
import sys
from io import StringIO
from unittest.mock import patch
import authentication.authentication


class AuthenticationTestCase(unittest.TestCase):
    

    def test_is_campus_valid(self):
        campus = authentication.authentication.is_campus_valid("dbn")
        self.assertEqual("dbn", campus)
        

    @patch("sys.stdin", StringIO("abc@gmail.com\nnonhlong021@student.wethinkcode.co.za"))
    def test_is_email_valid(self):    
        email = authentication.authentication.is_email_valid("abc@gmail.com\nnonhlong021@student.wethinkcode.co.za")
        self.assertTrue("""please enter a valid email address""", email)
        self.assertEqual("nonhlong021@student.wethinkcode.co.za", email)

    
    @patch("sys.stdin", StringIO("nonhlong021@student.wethinkcode.co.za\ndbn"))
    def test_register_user(self):
        User_Data = authentication.authentication.register_user()

        self.assertEqual(User_Data[0], "nonhlong021@student.wethinkcode.co.za")
        self.assertEqual(User_Data[1], "dbn")
        self.assertEqual(User_Data[2], "nonhlong021")

