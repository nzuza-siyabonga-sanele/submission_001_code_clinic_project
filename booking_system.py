from asyncio import events
import email
from itertools import count
import sys
from unittest.util import strclass
from authentication import authentication
from bookings.calendars  import calendar
from bookings import *
import datetime
from bookings.student_booking import book_a_slot
from bookings.volunteer_booking import book_volunteer_slot
from bookings.cancel_volunteer import cancel_event
from bookings.cancel_booking import cancel_booking

email_list = {}
date_list = []

running = True


valid_commands = ['cb','h', 'help', 'q','quit', 'v','volunteer', 'b', 
'book', 'cv', 'u', 'update', 'vc', 'view']

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
    elif command in ['cv', 'cancel']:
        get_volunter_data_to_cancel()
    elif command in ['cb', 'cancel']:
        get_booked_data_to_cancel()
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
    
    
def get_booked_data_to_cancel():
   
    email = authentication.get_user_input('email:', str)   
    time = authentication.get_user_input("Time (H:M):", str)
    valid_time =  calendar.validate_time(time)
    date = authentication.get_user_input("Date (YYYY-MM-DD):", str)
    valid_date = calendar.validate_date(date)
    calendars =  calendar.get_code_clinic_calendar()
    eventId = ""
    for event in calendars:
        if event[0] == valid_time and valid_date == calendar.new_date1:
            eventId = event[calendar.index][2]
            break
            
    cancel_booking(email, eventId)
    
def get_volunter_data_to_cancel():
    email = authentication.get_user_input('email:', str)   
    time = authentication.get_user_input("Time (H:M):", str)
    valid_time =  calendar.validate_time(time)
    date = authentication.get_user_input("Date (YYYY-MM-DD):", str)
    valid_date = calendar.validate_date(date)
    calendars =  calendar.get_code_clinic_calendar()
    eventId = ""
    for event in calendars:
        if event[0] == valid_time and valid_date == calendar.new_date1:
            eventId = event[calendar.index][2]
            break
            
    cancel_event(email,eventId)
  
   
    
    
def get_student_data():
    email = authentication.get_user_input('email:', str)   
    help_info = authentication.get_user_input('help infor:', str)
    calendars =  calendar.get_code_clinic_calendar()
    eventId = ""
    time = authentication.get_user_input("Time (H:M):", str)
    valid_time =  calendar.validate_time(time)
    date = authentication.get_user_input("Date (YYYY-MM-DD):", str)
    valid_date = calendar.validate_date(date)
    for event in calendars:
        if event[0] == valid_time and valid_date == calendar.new_date1:
            eventId = event[calendar.index][2]
            break
            
    book_a_slot(email,help_info, eventId)
    return email
  
  
def get_volunteer_data():
  
    email = authentication.User_Data[0]
    campus = authentication.User_Data[1]
    username =authentication.User_Data[2]
    expertise =  authentication.get_user_input("Description:", str)
    date = authentication.get_user_input("Date (YYYY-MM-DD):", str)
    valid_date = calendar.validate_date(date)
    time = authentication.get_user_input("Time (H:M):", str)
    valid_time =  calendar.validate_time(time)
    calendar.new_time1  =  valid_time
    calendar.new_date1 = valid_date
    format_time =  list(map(int, valid_date.split('-') +valid_time.split(':')))
    start_time = calendar.convert_to_RFC_datetime(
        format_time[0], format_time[1],format_time[2], format_time[3], format_time[4] )
    format_time = calendar.get_end_time(format_time)
    end_time =  calendar.convert_to_RFC_datetime(
        format_time[0], format_time[1],format_time[2], format_time[3], format_time[4] )
    book_volunteer_slot(start_time, end_time, email,campus, expertise, username )
    date_list.append(date)
  
    


#TODO call all functions here
def start_booking_system():
    setup_account()

    while running:
        response= get_command(input("How may I help you:"))
   
       
if __name__ =="__main__":
    start_booking_system()