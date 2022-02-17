#TNT PUSH
from operator import indexOf
import re
from authentication import authentication
# get wethinkcode code clinics calendar
from tabulate import tabulate
import datetime
from api_services import calendar_service
from dateutil.parser import parse as dtparse
from datetime import datetime as dt
from datetime import timedelta
from datetime import date as my_date
import booking_system

now = dt.now() # current date and time

year = int(now.strftime("%Y"))
month = int(now.strftime("%m"))
day = int(now.strftime("%d"))
hour = int(now.strftime("%H"))
min = int(now.strftime("%M"))

fd7 = str(now + timedelta(days=7))
date  = fd7.split(" ")[0]
time = fd7.split(" ")[1]
new_time =  time.split(".")[0]

year_end = int(date.split("-")[0])
month_end =int(date.split("-")[1])
day_end = int(date.split("-")[2])
hour_end  = int(new_time.split(":")[0])
min_end  = int(new_time.split(":")[1])

print(year_end, month_end, day_end, hour_end, min_end)

slot = ['avalable slot','avalable slot','avalable slot','avalable slot','Available slot','avalable slot','avalable slot']
service= calendar_service.get_calendar_service()

index = 0

new_time1 = ""
new_date1 = ""
#date and time coverter
def convert_to_RFC_datetime(year,month,day,hour,minute):
    dt =datetime.datetime(year,month,day,hour-2,minute,0).isoformat()+'Z'
    return dt



#retrieves code clinic available slots
def get_code_clinic_calendar():
    global index, slot , new_date1
    
    my_slot_time = []
    a = []

    times = get_slots_time()
    
    for i in range(len(times[0])):
        try:
            time = times[0][i] + ' - ' + times[1][i+1]
            my_slot_time.append(time)
        except IndexError:
            pass
    
    now = convert_to_RFC_datetime(year,month,day,hour,min)
    end = convert_to_RFC_datetime(year_end, month_end, day_end, hour_end, min_end)
    #takes the start time and name of the next 20 events 
    results = service.events().list(
        calendarId= 'c_t2chai1o082hgvkck0r8nhfa00@group.calendar.google.com', timeMin=now, timeMax=end,
                    maxResults = len(my_slot_time)+1, singleEvents=True,
                    orderBy= 'startTime').execute()
    events = results.get('items',[])

    days = get_slots()
    
    for i in days:
        a.append(i.split("-"))
    
    Calendars= [[f'Time         ',
    f'{datetime.date(int(a[0][0]),int(a[0][1]),int(a[0][2])).strftime("%A")} {days[0]}',
    f'{datetime.date(int(a[1][0]),int(a[1][1]),int(a[1][2])).strftime("%A")} {days[1]}',
    f'{datetime.date(int(a[2][0]),int(a[2][1]),int(a[2][2])).strftime("%A")} {days[2]}',
    f'{datetime.date(int(a[3][0]),int(a[3][1]),int(a[3][2])).strftime("%A")} {days[3]}', 
    f'{datetime.date(int(a[4][0]),int(a[4][1]),int(a[4][2])).strftime("%A")} {days[4]}', 
    f'{datetime.date(int(a[5][0]),int(a[5][1]),int(a[5][2])).strftime("%A")} {days[5]}', 
    f'{datetime.date(int(a[6][0]),int(a[6][1]),int(a[6][2])).strftime("%A")} {days[6]}']]
    
    
    for event in events:
        start_time  = event["start"]["dateTime"]
        start_date =  start_time.split("T")[0]
        new_date1 = start_date
        time = start_time.split("T")[1]
        time_one =   time.split(":")[0]
        time_two =   time.split(":")[1]
        f_time = time_one +":"+ time_two
        for ti in times[0]:   
            if ti ==  f_time:
                for date_day in days:
                    if  date_day == start_date:
                        for event in events:
                            booked = len(event['attendees'])
                            if booked ==2:
                                slot[days.index(date_day)]   =  (event['summary'], "booked", event['id'])
                                index = days.index(date_day)+1
                            elif booked == 1:
                                slot[days.index(date_day)]   =  (event['summary'], "available", event['id'])
                                index = days.index(date_day)+1
                            Calendars.append([ti,slot[0],slot[1],slot[2],slot[3],slot[4],slot[5],slot[6]])
            else: 
           
                Calendars.append([ti,"Available slot","Available slot","Available slot","Available slot","Available slot","Available slot","Available slot"])
       
                    
                   
            
                    # if booked > 1:
                    #     Calendars.append([times,index,stime, event['summary'],"BOOKED", event['id'], slot,slot])
                    # else:
                    #     Calendars.append([times,index,stime,event['summary'], "Available slot",event['id'],slot,slot])
                            

    print(tabulate(Calendars,headers='firstrow',tablefmt='grid'))
    return Calendars
  
    
def assign_time(time):
    global new_time
    if new_time !="":
        new_time = time
 


#retirieves user calendar



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
    

            
def get_slots():
    
    current_date=my_date.today()
    current_year=my_date.today().year
    current_day=my_date.today().day
    month_before=my_date.today().month
    date_before=current_date.replace(current_year,month_before,current_day)
    month_list=[date_before]
    # print(month_list)
    month_list=[(date_before+timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]
    print(month_list)
    return month_list

def get_slots_time():
    
    gf = []
    gh = []
    for i in range(1,25):
        if i == 24:
            gf.append("00:00")
            a = ("00:30")
            gf.append(a)
        else:
            gf.append(str(i)+":00")
            a = (str(i)+":30")
            gf.append(a)
            
    for i in range(1,25):
        if i == 24:
            gh.append("00:00")
            a = ("00:30")
            gh.append(a)
        else:
            gh.append(str(i)+":00")
            a = (str(i)+":30")
            gh.append(a)
                  
    return (gf,gh)
