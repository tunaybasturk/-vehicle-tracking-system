import sys
sys.path.append("../")

from models.models import *

from controller.controller3 import *

new_login_time=login_time
def is_user_exist(username,password):
    data=query_user(username,password)
    if(len(data)!=0):
        return True      
    else:
        return False
def go_to_last_30_min(now):
    global new_login_time
    
    return last_30_min(now.hour,now.minute),last_30_min(now.hour,now.minute),last_30_min(now.hour,now.minute),last_30_min(now.hour,now.minute),last_30_min(now.hour,now.minute),last_30_min(now.hour,now.minute),last_30_min(now.hour,now.minute),last_30_min(now.hour,now.minute),last_30_min(now.hour,now.minute)

def warning(warning_counter):
        warning_counter+=1
        return warning_counter

def bridge_for_online_sessions(username):
    online_sessions(username)
def bridge_for_offline_sesions(username):
    offline_sessions(username)

def get_person_id():
    return send_person_id()




