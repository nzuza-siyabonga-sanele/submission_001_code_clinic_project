from asyncore import read
from distutils import text_file
import os
import json

student_info = { 
    'email': "", 
    'campus':"",
    "calendar":"c_t2chai1o082hgvkck0r8nhfa00@group.calendar.google.com"  
}

def store_user_info():

    data_file = os.path.expanduser('~/.calendar_data/student.json')

    with open(data_file, 'a') as student:
            json.dump(student_info, student,)
            
def get_user_info():
     
    data_file = os.path.expanduser('~/.calendar_data/student.json')           
    my_file = open(data_file)
    content = my_file.read()
    my_file.close()
    
    return content

