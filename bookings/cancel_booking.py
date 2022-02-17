from array import array
from api_services import calendar_service
import webbrowser

# THIS FUNCTION HELP TO 'CANCEL' STUDENT BOOKINGS
def cancel_booking(email,eventId):
    
    service = calendar_service.get_calendar_service()
    # First retrieve the event from the API.
    event = service.events().get(calendarId="c_t2chai1o082hgvkck0r8nhfa00@group.calendar.google.com", eventId=eventId).execute()

    
    # check if event is booked
    booked = len(event['attendees'])
    if booked < 2:
        print("You have not booked the slot")
    else:
        
        # update attendee
        event['attendees'] = [
            event['attendees'][0]
            ]

        # API call to send updated information
        service.events().update(calendarId="c_t2chai1o082hgvkck0r8nhfa00@group.calendar.google.com", eventId=eventId, \
        body=event, sendUpdates = 'all').execute()
        # print(event)
        webbrowser.open('https://calendar.google.com/calendar/u/0/r',new=0,autoraise=True)
    
        return "Successfully booked"