from flask import Flask, request, url_for, redirect, render_template, json, jsonify
import random
import os
import sqlite3
import base64
import datetime

cwd = str(os.path.dirname(os.path.realpath(__file__))) + "\\userLocationDB.db"

###START DB CREATION###
locationDB = sqlite3.connect(cwd)
DBCursor = locationDB.cursor()
DBCursor.execute('''CREATE TABLE IF NOT EXISTS UserLocation
        (ID                 INT PRIMARY KEY     NOT NULL,
        UUID                TEXT                NOT NULL,
        TIME                TEXT                NOT NULL,
        DATE                INT                 NOT NULL,
        COORDS              TEXT                NOT NULL);''')
locationDB.commit()
locationDB.close()


def addCoord(uuid, coords, time, date):
        locationDB = sqlite3.connect(cwd)
        DBCursor = locationDB.cursor()
        DBCursor.execute("select * from UserLocation")

        ID =  (len(DBCursor.fetchall()) + 1)
        locationDB.execute("INSERT INTO UserLocation(ID, UUID, TIME, DATE, COORDS) \
                VALUES(?, ?, ?, ?, ?)", (ID, uuid, time, date, coords))

        locationDB.commit()
        locationDB.close()

def getCoords(uuid):
        locationDB = sqlite3.connect(cwd)
        DBCursor = locationDB.cursor()
        DBCursor.execute(("select COORDS from UserLocation where UUID=" + "\'" + uuid + "\'"))

        coordList =  DBCursor.fetchall()

        locationDB.commit()
        locationDB.close()
        return coordList

###START PAGE ROUTING###
app = Flask(__name__) 

#INDEX PAGE ROUTE
@app.route('/')
def index():
        return render_template('index.html')
                

#ADD Coords ROUTE
@app.route('/append', methods=['POST'])
def append():
        coords = request.form["coordinates"]
        time = request.form["time"]
        uuid = request.form["uuid"]
        date = datetime.datetime.today()

        addCoord(uuid, coords, time, date)
        return json.dumps({'status':'OK'})


#VIEWING COORDS ROUTE
@app.route('/v/<UUID>')
def viewLoc(UUID):
        #gets a list of coords that have a matching UUID
        coords = getCoords(UUID)
        print(coords)
        #redirects to viewing page & updates every 2 minutes
        return render_template('viewing.html', coordList=coords)

###START SERVER###
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)