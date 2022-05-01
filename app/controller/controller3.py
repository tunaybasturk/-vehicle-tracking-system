import sys

from numpy import integer
sys.path.append("../")
from datetime import datetime
last_30_min_list=[]
data=[]
cars_id_holder_1=[]
cars_id_holder_2=[]
liste=[]

lat_holder_1_1_30_min=[]
lng_holder_1_1_30_min=[]
lat_holder_2_1_30_min=[]
lng_holder_2_1_30_min=[]

lat_holder_1_2_30_min=[]
lng_holder_1_2_30_min=[]
lat_holder_2_2_30_min=[]
lng_holder_2_2_30_min=[]

data_start_time=str
data_end_time=str
data_car_id=str
person_id_1=[]
person_id_2=[]

hour_minute_list=[]
def last_30_min(hour,minute):
    global data,person_id_1,person_id_2 ,lat_holder_1_1_30_min,lng_holder_1_1_30_min,lat_holder_2_1_30_min,lng_holder_2_1_30_min,lat_holder_1_2_30_min,lng_holder_1_2_30_min,lat_holder_2_2_30_min,lng_holder_2_2_30_min
    log_time=hour*60+minute
    log_last_30_minute=log_time-30
    global last_30_min_list
    last_30_min_list=[]
    for i in range(log_last_30_minute+1,log_time+1):
        hour_holder=int(i/60)
        minute_holder=(i%60)
        if(minute_holder<10):
            minute_holder="0"+str(minute_holder)
        if(hour_holder<10):
            hour_holder=str(hour_holder)+"0"
        hour_minute_holder=str(str(hour_holder)+":"+str(minute_holder))
        last_30_min_list.append(hour_minute_holder)
    
    
    if(person_id_1==1):
        for i in range(1,len(data)):
            if data[i].get("Car_ID") in cars_id_holder_1[0]:
                if data[i].get("Time") in last_30_min_list:
                    lat_holder_1_1_30_min.append(data[i].get("Latitude"))
                    lng_holder_1_1_30_min.append(data[i].get("Longitude"))
            if data[i].get("Car_ID") in cars_id_holder_1[1]:
                if data[i].get("Time") in last_30_min_list:
                    lat_holder_2_1_30_min.append(data[i].get("Latitude"))
                    lng_holder_2_1_30_min.append(data[i].get("Longitude"))
    if(person_id_2==2):
        for i in range(1,len(data)):
            if data[i].get("Car_ID") in cars_id_holder_2[0]:
                if data[i].get("Time") in last_30_min_list:
                    lat_holder_1_2_30_min.append(data[i].get("Latitude"))
                    lng_holder_1_2_30_min.append(data[i].get("Longitude"))
            if data[i].get("Car_ID") in cars_id_holder_2[1]:
                if data[i].get("Time") in last_30_min_list:
                    lat_holder_2_2_30_min.append(data[i].get("Latitude"))
                    lng_holder_2_2_30_min.append(data[i].get("Longitude"))
    

    lat_holder_1_1_30_min=[]
    lng_holder_1_1_30_min=[]
    lat_holder_2_1_30_min=[]
    lng_holder_2_1_30_min=[]
 
    lat_holder_1_2_30_min=[]
    lng_holder_1_2_30_min=[]
    lat_holder_2_2_30_min=[]
    lng_holder_2_2_30_min=[]
    
    return last_30_min_list,lat_holder_1_1_30_min,lng_holder_1_1_30_min,lat_holder_2_1_30_min,lng_holder_2_1_30_min,lat_holder_1_2_30_min,lng_holder_1_2_30_min,lat_holder_2_2_30_min,lng_holder_2_2_30_min





def get_lat_lng(data_):
    global data
    data=data_

def all_hours_24():
    global hour_minute_list
    hour_minute_list=[]
    for i in range(1,24*60+1):
        new_hour = int(i / 60)
        new_minute = i % 60

        if (new_hour < 10):
            new_hour = str("0" + str(new_hour))
        if (new_hour == 24):
            new_hour = str("0" + "0")
        if (new_minute < 10):
            new_minute = str("0" + str(new_minute))
        new_hour_minute = str(str(new_hour) + ":" + str(new_minute))
        hour_minute_list.append(new_hour_minute)
    return hour_minute_list

def get_latlng_last_30_min(cars_id,person_id):
    
    global cars_id_holder_1,person_id_1,cars_id_holder_2,person_id_2
    
    
    
          
    if person_id[0]==1:      
        person_id_1=person_id[0]
        cars_id_holder_1=cars_id
        
    if person_id[0]==2:
        person_id_2=person_id[0]
        cars_id_holder_2=cars_id
   

def start_time_holder(start_time):
    global data_start_time
    data_start_time=start_time
def end_time_holder(end_time):
    global data_end_time
    data_end_time=end_time
def car_id_holder(car_id):
    global data_car_id
    data_car_id=car_id



hour_minute_1_24_list=[]
lat_holder_1_24_list=[]
lng_holder_1_24_list=[]
new1_hour_minute=0
def hour_1_ago():
    global new1_hour_minute
    now_time=datetime.now()
    now_time_hour=now_time.hour
    now_time_minute=now_time.minute
    now_time_hour=int(now_time_hour)
    now_time_minute=int(now_time_minute)
    now_time_total_minute=now_time_hour*60+now_time_minute
    hour_1=60
    if(now_time_total_minute-hour_1>0):
        minus_the_minute = now_time_total_minute-hour_1
        

        new_1_hour=int(minus_the_minute/60)
        new_1_minute=int(minus_the_minute%60)

        if(new_1_hour<10):
            new_1_hour="0"+str(new_1_hour)
        if(new_1_minute<10):
            new_1_minute="0"+str(new_1_minute)
        new1_hour_minute=str(str(new_1_hour) + ":" + str(new_1_minute))
        
        
    if(now_time_total_minute-hour_1<0):
        minus_the_minute = (24*60+now_time_total_minute)-hour_1
        new_1_hour=int(minus_the_minute/60)
        new_1_minute=int(minus_the_minute%60)
        if (new_1_hour<10 < 10):
                new_1_hour = str("0" + str(new_1_hour))
        if(new_1_hour==24):
                new_1_hour=str("0"+"0")
        if (new_1_minute < 10):
                new_1_minute = str("0" + str(new_1_minute))
        new1_hour_minute=str(str(new_1_hour) + ":" + str(new_1_minute))
              
    return new1_hour_minute
def now_time_hour_minute():
    now_time2=datetime.now()
    now_time_h=now_time2.hour
    now_time_m=now_time2.minute
    if (now_time_h<10 < 10):
        now_time_h = str("0" + str(now_time_h))
    if(now_time_h==24):
        now_time_h=str("0"+"0")
    if (now_time_m < 10):
        now_time_m = str("0" + str(now_time_m))
    now_time_h_m=str(str(now_time_h)+":"+str(now_time_m))
    return now_time_h_m

def algoritma():
    global data_start_time,data_end_time,hour_minute_1_24_list,lat_holder_1_24_list,lng_holder_1_24_list,data,data_car_id
    hour_minute_1_24_list=[]
    lat_holder_1_24_list=[]
    lng_holder_1_24_list=[]
    data_car_id=str(data_car_id)
    hour_minute_start=data_start_time.split(":")
    start_hour=hour_minute_start[0]
    start_minute=hour_minute_start[1]
    start_hour=int(start_hour)
    start_minute=int(start_minute)


    hour_minute_end=data_end_time.split(":")
    end_hour=hour_minute_end[0]
    end_minute=hour_minute_end[1]
    end_hour=int(end_hour)
    end_minute=int(end_minute)



    start_sum_time=start_hour*60+start_minute
    end_sum_time=end_hour*60+end_minute
   
    
    
    for i in range(start_sum_time,end_sum_time+1):

            new_hour=int(i/60)
            new_minute=i%60

            if(new_hour<10):
                new_hour="0"+str(new_hour)
            if(new_minute<10):
                new_minute="0"+str(new_minute)
            new_hour_minute = str(str(new_hour) + ":" + str(new_minute))
            hour_minute_1_24_list.append(new_hour_minute)

    for i in range(1,len(data)):
            if data[i].get("Car_ID") in data_car_id:
                if data[i].get("Time") in hour_minute_1_24_list:
                    lat_holder_1_24_list.append(data[i].get("Latitude"))
                    lng_holder_1_24_list.append(data[i].get("Longitude"))

    

    return hour_minute_1_24_list,lat_holder_1_24_list,lng_holder_1_24_list




