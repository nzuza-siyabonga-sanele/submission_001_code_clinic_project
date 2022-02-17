from __future__ import print_function
from asyncio import events
<<<<<<< HEAD
from bookings.calendars import calendar
=======
# from bookings.calendars import calendar
>>>>>>> CodeClinic_Tests
import json
import datetime
from api_services import calendar_service

User_Data = []


def register_user():
    global User_Data
<<<<<<< HEAD
    # email =  get_user_input("Email Address: ",str).strip().lower()
    email =  "mxomagub021@student.wethinkcode.co.za"
    # email = is_email_valid(email)
    # campus  = get_user_input("Campus -(DBN/CPT/JHB): ",str).strip().lower()
    # if campus == "cape town":
    #     campus =  "capetown"
    # campus =is_campus_valid(campus)
    # at_pos= email.find('@')
    # username = email[:at_pos].strip()
    User_Data = [ email, "dbn", "mxomagub021"]
=======
    email =  get_user_input("Email Address: ",str).strip().lower()
    # email =  "mxomagub021@student.wethinkcode.co.za"
    email = is_email_valid(email)
    campus  = get_user_input("Campus -(dbn/cpt/jhb): ",str).strip().lower()
    # if campus == "cape town":
    #     campus =  "capetown"
    campus =is_campus_valid(campus)
    at_pos= email.find('@')
    username = email[:at_pos].strip()
    User_Data = [ email, campus, username]
>>>>>>> CodeClinic_Tests

    return User_Data


def is_email_valid(email):
    at_pos= email.find('@')
    wtc = email[at_pos+1:].strip()

    while wtc != "student.wethinkcode.co.za":
<<<<<<< HEAD
       print("please enter a valid email address")
=======
       print("Please enter a valid email address")
>>>>>>> CodeClinic_Tests
       email = get_user_input("Email Address: ",str)
       at_pos= email.find('@')
       wtc = email[at_pos+1:].strip()
    return email


def is_campus_valid(campus):
    while campus not in ["dbn", "cpt", "jhb", 'durban', 'johannesburg', 'capetown']:
<<<<<<< HEAD
        campus  = get_user_input("Campus -(DBN/CPT/JHB): ",str).strip().lower()
=======
        campus  = get_user_input("Campus -(dbn/cpt/jhb): ",str).strip().lower()
>>>>>>> CodeClinic_Tests
    return campus


def get_user_input(question, return_type):
    if return_type is int:

        response = input(question)
        while not response.isnumeric():
            response = input(question)
        return response

    return input(question)


#TODO store user information
def store_user_info():
    pass





    