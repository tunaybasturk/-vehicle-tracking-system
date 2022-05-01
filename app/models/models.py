import sqlite3
from datetime import datetime
import sys
sys.path.append("../")
import pymongo
from controller.controller3 import *

cars_id_list=[]
person_id_list=[]
login_time =0
vehicle_id=[]
person_id=[]

from flask import session

def query_user(username,password):
    con=sqlite3.connect("customer.db")
    cursor=con.cursor()
    cursor.execute("SELECT username FROM customer WHERE username=? AND password=?",(username,password))
    data=cursor.fetchall()
    con.commit()
    con.close()
    return data
    
    
    
def online_sessions(username):
    global login_time,person_id_list,cars_id_list,person_id,vehicle_id
    login_time = datetime.now()
    
    zaman = datetime.ctime(login_time)
    
    con=sqlite3.connect("customer.db")
    cursor=con.cursor()
    cursor.execute("UPDATE customer SET online=? WHERE username= ?",("True",username,))
    cursor.execute("UPDATE customer SET system_in=? WHERE username= ?",(zaman,username,))
    person_id=cursor.execute("SELECT rowid FROM customer WHERE username= ?",(username,))
    person_id=person_id.fetchall()
    person_id_list.append(person_id[0][0])
    vehicle_id=cursor.execute("SELECT cars_id FROM cars WHERE customer_id= ?",(person_id[0][0],))
    vehicle_id=vehicle_id.fetchall()
    cars_id_list.append(vehicle_id[0][0])
    cars_id_list.append(vehicle_id[1][0])
  
    get_latlng_last_30_min(cars_id_list,person_id_list)
    cars_id_list=[]
    person_id_list=[]
    con.commit()
    con.close()
    

def offline_sessions(usersname):
    global logout_time,cars_id_list,person_id_list
    logout_time = datetime.now()
    session=str(logout_time-login_time)
    cars_id_list=[]
    person_id_list=[]
    zaman = datetime.ctime(logout_time)
    con=sqlite3.connect("customer.db")
    cursor=con.cursor()
    cursor.execute("UPDATE customer SET online=? WHERE username= ?",("False",usersname,))
    cursor.execute("UPDATE customer SET system_out=? WHERE username= ?",(zaman,usersname,))
    cursor.execute("UPDATE customer SET session=? WHERE username= ?",(session,usersname,))

    con.commit()
    con.close()


def mongodb():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["project"]
    mycol = mydb["cars"]
    liste=[[]]

    for x in mycol.find():
        liste.append(x)
    get_lat_lng(liste)

def send_person_id():
    return person_id[0][0]