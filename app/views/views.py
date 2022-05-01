from glob import glob
from flask import Flask,render_template,redirect,session,url_for,request,jsonify
import sys

sys.path.append("../")
from controller.controller import *
from controller.controller3 import *
from unicodedata import name
from datetime import datetime
import json

hour_24=[]
warning_counter=0
hour_minute_list=[]
username=str
lat_24=str
lng_24=str
now_time_hour_minute_=str
hour_1_ago_=str

app =Flask(__name__,template_folder='../templates',static_folder='../static')
last_30_min_data,person_1_car_1_lat,person_1_car_1_lng,person_1_car_2_lat,person_1_car_2_lng,person_2_car_1_lat,person_2_car_1_lng,person_2_car_2_lat,person_2_car_2_lng=go_to_last_30_min(datetime.now())

@app.route("/home/<name>")
def Home(name):
    return render_template("home.html",username=name)

@app.route("/get_data",methods=['POST'])
def get_data():
    last_30_min_data,person_1_car_1_lat,person_1_car_1_lng,person_1_car_2_lat,person_1_car_2_lng,person_2_car_1_lat,person_2_car_1_lng,person_2_car_2_lat,person_1_car_2_lng=go_to_last_30_min(datetime.now())
    return jsonify('',render_template("data.html",x=last_30_min_data,a=person_1_car_1_lat,b=person_1_car_1_lng,c=person_1_car_2_lat,d=person_1_car_2_lng,e=person_2_car_1_lat,f=person_2_car_1_lng,g=person_2_car_2_lat,h=person_2_car_2_lng))

@app.route('/test', methods=['GET', 'POST'])
def test(): 
    data_get_list=request.get_json(force=True)
    
    car_id_holder(data_get_list)
    return render_template("home.html")
    
@app.route('/test1', methods=['GET', 'POST'])
def test1():  
    data_get_list1=request.get_json(force=True)
   
    start_time_holder(data_get_list1)
    return render_template("home.html") 

@app.route('/test2', methods=['GET', 'POST'])
def test2():
    global hour_24,lat_24,lng_24
    data_get_list2=request.get_json(force=True)
    
    end_time_holder(data_get_list2)
    hour_24,lat_24,lng_24=algoritma()
    return render_template("home.html")


@app.route("/",methods=['POST','GET'])
def Login():
   
    global warning_counter,username,hour_minute_list,username,hour_1_ago
    if request.method=='POST':    
        username=request.form["username"]
        password=request.form["password"] 
        if(is_user_exist(username,password)):
           
            bridge_for_online_sessions(username)
            person_id=get_person_id()
            mongodb()
            hour_minute_list=all_hours_24()
            hour_1_ago_=hour_1_ago()
            now_time_hour_minute_=now_time_hour_minute()
            
            return render_template("home.html",name=username,id=person_id,x=last_30_min_data,a=person_1_car_1_lat,c=person_1_car_2_lat,d=person_1_car_2_lng,h_m=hour_minute_list,h_1_a=hour_1_ago_,h_m_now=now_time_hour_minute_)
        else:
            warning_counter=warning(warning_counter)
            return render_template("login.html",warning_counter=warning_counter)                   
    else:
        return render_template("login.html")
@app.route("/logout")
def Logout():
    global warning_counter
    bridge_for_offline_sesions(username)
    warning_counter=0
    return redirect(url_for("Login"))       

@app.route("/hour_24")
def Hour24():
    global username,hour_24,lat_24,lng_24
    hour_24=[]
    lat_24=[]
    lng_24=[]
    hour_24,lat_24,lng_24=algoritma()
   
    return render_template("hour_24.html",name=username,hour_24=json.dumps(hour_24),lat_24=json.dumps(lat_24),lng_24=json.dumps(lng_24))

if __name__ == '__main__':
   app.run(debug=True)
