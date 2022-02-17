import unittest
import booking_system


class TestBookingSystem(unittest.TestCase):


    def test_help_commands(self):
        return_value = booking_system.get_help_commands()
        self.assertEqual("""These are all valid commands:
h or help      - outputs a list of available commands
q or quit      - quits and exits booking system
v or volunteer - books a volunteer slot in the code clinics calendar
b or book      - books a available slot for student in the code clinics calendar
c or cancel    - cancels a volunteer slot or student booking
vc or view     - diplays code clinic slots
""", return_value)



    
  