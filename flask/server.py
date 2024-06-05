#!/usr/bin/env python
import os

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

db_name = 'ems'
collection_name = 'powermeter'

client = MongoClient("mongo:27017")
mydb = client[db_name]
collection = mydb[collection_name]

@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return "Hello from the MongoDB client!\n"

@app.route('/insert')
def insert():
    #power = {'timestamp':1717056022,'device':'ABCDEF','power':100,'voltage':110.1,'current':0.9,'wh':1234}
    #collection.insert_one(power)
    return "insert data ok!"

@app.route('/show')
def show():
    #rows = collection.find({'device':'ABCDEF'})
    rows = collection.find()
    response=""
    for row in rows:
       response = response+"_id:"+str(row['_id'])+' ,'+'power='+str(row['active_power'])+' ,dt:'+row['datetime']+"<br>"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)

