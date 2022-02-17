import email
import sys
from unittest.util import strclass
from authentication import authentication
from bookings.calendars  import calendar
from bookings import *
import datetime
from bookings.student_booking import book_a_slot
from bookings.volunteer_booking import book_volunteer_slot
from authentication.authentication import emails

email_list = {}

running = True

valid_commands = ['h', 'help', 'q','quit', 'v','volunteer', 'b', 
'book', 'c','cancel', 'u', 'update', 'vc', 'view']

WELCOME = "***Welcome To Code Clinics Booking System***"
#TODO list all available commands



def get_help_commands():
    commands ="""These are all valid commands:
h or help      - shows a list of available commands
q or quit      - quits and exits booking system
v or volunteer - books a volunteer slot in the code clinics calendar
b or book      - books a available slot for student in the code clinics calendar
c or cancel    - cancels a volunteer slot or student booking
vc or view     - shows code clinic calendar slots
"""
    return commands




#TODO get commands from user here
def get_command(command):

    if type(command) != int:
        command = command.strip().lower()
        if command in valid_commands:
            process_command(command)
        else:
            print(f"'{command}' is an invalid command. type 'h' or 'help' to view valid commands")
    else: 
        print("Invalid command. Type 'h' or 'help' to view valid commands")
    

def process_command(command):
    global running
    if command in ['h', 'help']:
        print(get_help_commands())
    elif command in ['b', 'book']:
        get_student_data()
    elif command in ['v', 'volunteer']:
        get_volunteer_data()
    elif command in ['c', 'cancel']:
        print("cancelling in progress")
    elif command in ['vc', 'view']:
        calendar.get_code_clinic_calendar()
    elif command in ['q','quit']:
        running =False


def setup_account():
    print(f"{WELCOME}\n")
    print("Let's setup a few things first\n")
    authentication.register_user()
    print("All setup!\n")
    print("Code Clinic Calendar:")
    calendar.get_code_clinic_calendar()
 

def get_student_data():
    slot_number = authentication.get_user_input("Enter slot number:", int)
    calendar.index =0
    calendars = calendar.get_code_clinic_calendar()
    eventId = ''
    for event in calendars:
        if event[0] == int(slot_number):
            eventId = event[4]
            break
    # email = authentication.get_user_input('email:', str)   
    email = "siynzua021@student.wethinkcode.co.za"
    help_info = authentication.get_user_input('help infor:', str)
    print(eventId)
    book_a_slot(email,help_info, eventId)
    print("Successfully booked")
    email_list[emails[0]]= eventId
    emails.clear()

    # return email



<<<<<<< HEAD
=======

    
def get_volunteer_data():
    email = authentication.User_Data[0]
    campus = authentication.User_Data[1]
    username =authentication.User_Data[2]
    expertise =  authentication.get_user_input("Description:", str)
    date= authentication.get_user_input("Date (YYYY-MM-DD):", str)
    valid_date = calendar.validate_date(date)
    time = authentication.get_user_input("Time (H:M):", str)
    valid_time =  calendar.validate_time(time)
    format_time =  list(map(int, valid_date.split('-') +valid_time.split(':')))
    start_time = calendar.convert_to_RFC_datetime(
        format_time[0], format_time[1],format_time[2], format_time[3], format_time[4] )
    format_time = calendar.get_end_time(format_time)
    end_time =  calendar.convert_to_RFC_datetime(
        format_time[0], format_time[1],format_time[2], format_time[3], format_time[4] )
    book_volunteer_slot(start_time, end_time, email,campus, expertise, username )









>>>>>>> CodeClinic_Tests
#TODO call all functions here
def start_booking_system():
    setup_account()
    while running:
        response= get_command(input("How may I help you:"))
   
       

if __name__ =="__main__":
<<<<<<< HEAD
    start_booking_system()
=======
    start_booking_system()
>>>>>>> CodeClinic_Tests
