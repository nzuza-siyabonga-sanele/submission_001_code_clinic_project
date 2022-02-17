from api_services import calendar_service
<<<<<<< HEAD
import webbrowser
=======
>>>>>>> CodeClinic_Tests

#TODO book a slot for student
def book_a_slot(email, support_info, eventId):
    service = calendar_service.get_calendar_service()
    # First retrieve the event from the API.
    event = service.events().get(calendarId="c_t2chai1o082hgvkck0r8nhfa00@group.calendar.google.com", eventId=eventId).execute()

<<<<<<< HEAD
    

    # update attendee
    event['attendees'] = [
        event['attendees'][0],
        {'email': f"{email}"}
=======
    # update attendee
    event['attendees'] = [
        event['attendees'][0],
        {'email': f"{email}"},
>>>>>>> CodeClinic_Tests
    ]

    # update description
    event['description'] = f"{event['description']} - {support_info}"

    # API call to send updated information
    service.events().update(calendarId="c_t2chai1o082hgvkck0r8nhfa00@group.calendar.google.com", eventId=eventId, \
    body=event, sendUpdates = 'all').execute()
<<<<<<< HEAD
    # print(event)
    webbrowser.open('https://calendar.google.com/calendar/u/0/r',new=0,autoraise=True)
    
    return "Successfully booked"
=======
>>>>>>> CodeClinic_Tests
