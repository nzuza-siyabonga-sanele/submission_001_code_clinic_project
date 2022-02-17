from api_services import calendar_service
import webbrowser




def book_volunteer_slot(start_time, endtime, email,campus, expertise,username):

    service = calendar_service.get_calendar_service()

    # details for the event to be created
    event = {                                                                              
    'summary': f"Code Clinic - {username}",
    'location': f'{campus}',
    'description': f'{expertise}',
    'start': {
        'dateTime': f"{start_time}",
        'timeZone': 'Africa/Johannesburg',
    },
    'end': {
        'dateTime': f"{endtime}",
        'timeZone': 'Africa/Johannesburg',
    },
    'attendees':[
        {'email': f"{email}",}
    ]
    }

    # call API to create event
    event = service.events().insert(calendarId="c_t2chai1o082hgvkck0r8nhfa00@group.calendar.google.com", body=event, \
            sendUpdates = 'all').execute()
    
    webbrowser.open('https://calendar.google.com/calendar/u/0/r',new=0,autoraise=True)
