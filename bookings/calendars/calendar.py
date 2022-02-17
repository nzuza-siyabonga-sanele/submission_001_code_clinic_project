#TNT PUSH
from authentication import authentication
# get wethinkcode code clinics calendar
from tabulate import tabulate
import datetime
from api_services import calendar_service
from dateutil.parser import parse as dtparse
from datetime import datetime as dt


service= calendar_service.get_calendar_service()

index = 0
#date and time coverter
def convert_to_RFC_datetime(year,month,day,hour,minute):
    dt =datetime.datetime(year,month,day,hour-2,minute,0).isoformat()+'Z'
    return dt


#retrieves code clinic available slots
def get_code_clinic_calendar():
    global index
    now = convert_to_RFC_datetime(2022,2,7,8,0)
    #takes the start time and name of the next 20 events 
    results = service.events().list(
        calendarId= 'c_tlmtjbid6ddj0pj0sa5lgb98ms@group.calendar.google.com', timeMin=now,
                    maxResults = 20, singleEvents=True,
                    orderBy= 'startTime').execute()
    events = results.get('items',[])

    Calendars= [['number','Date','summary','status', 'eventId']]

    for event in events:
        if "code" in event['summary'].lower():
            start=event['start'].get('dateTime',event['start'].get('date'))
            tmfmt = '%d %B, %H:%M %p'
            stime = dt.strftime(dtparse(start),format=tmfmt)
            booked = len(event['attendees'])
            index+=1
            if booked > 1:
                Calendars.append([index,stime, event['summary'],"BOOKED", event['id']])
            else:
                Calendars.append([index,stime,event['summary'], "Available slot",event['id']])
    Calendars = Calendars + get_user_calendar()
    print(tabulate(Calendars,headers='firstrow'))
    return Calendars
  
    
#retirieves user calendar
def get_user_calendar():
    global index
    now = convert_to_RFC_datetime(2022,2,7,8,0)
    
    #takes the start time and name of the next 7 events
    results = service.events().list(calendarId= 'c_t2chai1o082hgvkck0r8nhfa00@group.calendar.google.com', timeMin=now,
                                                maxResults = 20, singleEvents=True,
                                                orderBy= 'startTime').execute()
    events = results.get('items',[])
    calendars=[]
    for event in events:
        if "code" in event['summary'].lower():
            start=event['start'].get('dateTime',event['start'].get('date'))
        
            tmfmt = '%d %B, %H:%M %p'
            stime = dt.strftime(dtparse(start),format=tmfmt)
            booked = len(event['attendees'])
            index+=1
            if booked > 1:
                calendars.append([index,stime, event['summary'],"BOOKED",event['id']])
            else:
                calendars.append([index,stime,event['summary'], "Available slot",event['id']])
    return calendars


def validate_date(date):
    format = "%Y-%m-%d"
    correct_date = False
    while not correct_date:
        try:
            datetime.datetime.strptime(date, format)
            if check_date_range(date):
                return date
            print("Current year required")
            date = authentication.get_user_input("Date (YYYY-MM-DD):", str)
        except ValueError:
            date = authentication.get_user_input("Date (YYYY-MM-DD):", str)


def validate_time(time):
    timeformat = ("%H:%M")
    correct_time = False
    while not correct_time:
        try:
            datetime.datetime.strptime(time, timeformat)
            if check_time_range(time):
                return time
            print("30 minutes  intervals only")
            time = authentication.get_user_input("Time (H:M):", str)
            
        except ValueError:
            time = authentication.get_user_input("Time (H:M):", str)


def check_date_range(date):
    year = int(date.split('-')[0])
    if year >=2022:
        return  True
    return False


def check_time_range(time):
    time = int(time.split(':')[1])
    if time == 30 or time ==00 or time ==0:
        return True
    return False


def get_end_time(format_time):
    
    if  format_time[4] ==30:
        format_time[3] =format_time[3]+1
        format_time[4] =0

        return format_time      
    format_time[4] = format_time[4]+30
    return  format_time
    

            

