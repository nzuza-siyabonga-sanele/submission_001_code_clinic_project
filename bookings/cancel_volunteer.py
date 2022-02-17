from api_services import calendar_service

# THIS FUNCTION HELP TO 'CANCEL' VOLUNTEER BOOKINGS
def cancel_event(email, eventId):
    
    service = calendar_service.get_calendar_service()
    event = service.events().get(calendarId="c_t2chai1o082hgvkck0r8nhfa00@group.calendar.google.com", eventId=eventId).execute()
    
    # check if event is booked
    booked = len(event['attendees'])     
    if booked < 2:
        event = service.events().delete(calendarId='c_t2chai1o082hgvkck0r8nhfa00@group.calendar.google.com', eventId= eventId).execute()
    else:
        print("Student already booked ")
    
   