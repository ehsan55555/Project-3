
# Import the dependencies.
#import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
import numpy as np
import pandas as pd
import datetime as dt
import sqlite3
con = sqlite3.connect("accidents.sqlite")
cur = con.cursor()
cur.execute("SELECT * FROM 'Motor_Vehicle_Collisions_-_Crashes' LIMIT 0,30").fetchall()


app = Flask(__name__)

# Define a route to serve the HTML page
@app.route('/')
def index():
    return render_template('test_html.html')

@app.route("/api/v1.0/accident_barchart")

def accident_barchart():
    cur = con.cursor()
    results=cur.execute("SELECT BOROUGH, count(BOROUGH) as ACCIDENTS FROM 'Motor_Vehicle_Collisions_-_Crashes' WHERE BOROUGH != '' group by BOROUGH").fetchall()
    
 
    return jsonify(results)


@app.route("/api/v1.0/distracted_driver")
def distracted_driver():
    cur = con.cursor()
    distracted_drivers = cur.execute("SELECT BOROUGH, count(BOROUGH) as ACCIDENTS FROM 'Motor_Vehicle_Collisions_-_Crashes' Where `CONTRIBUTING FACTOR VEHICLE 1` = 'Driver Inattention/Distraction' and BOROUGH != '' group by BOROUGH").fetchall()
    total_accidents_distracted_drivers = 0
    percentage_dd = []
    for d in distracted_drivers:
        total_accidents_distracted_drivers += (int(d[1]))
    for d in distracted_drivers:
        percentage_dd.append((int(d[1])) / total_accidents_distracted_drivers * 100)


    return jsonify(percentage_dd)

if __name__ == '__main__':
    app.run(debug=True)