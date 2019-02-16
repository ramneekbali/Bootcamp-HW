import numpy as np
import pandas as pd
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from datetime import datetime,timedelta
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def welcome():
    """ List all routes that are available"""
    return (
        f"Welcome to the weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date_and_end_date>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    start_time = datetime(2017,8,23)
    last_12months = start_time - timedelta(days=365)
    print(last_12months)
    prcp_df= session.query(Measurement.date,Measurement.prcp).filter(Measurement.date > last_12months).all()
    precp=[]
    for x in prcp_df:
        row={}
        row['date']=prcp_df[0]
        row['prcp']=prcp_df[1]
        precp.append(row)

    return jsonify(precp)

@app.route("/api/v1.0/stations")
def station():
    result=session.query(Station.name,Station.station).all()
    station_list=list(np.ravel(result))
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    start_time = datetime(2017,8,23)
    last_12months = start_time - timedelta(days=365)
   
    temp=session.query(Measurement.date, Measurement.tobs).group_by(Measurement.date).filter(Measurement.date >last_12months).all()
    t_obs=[]
    for x in temp:
        row={}
        row['date']=temp[0]
        row['tobs']=temp[1]
        t_obs.append(row)
    return jsonify(t_obs)

@app.route("/api/v1.0/<start>")
def start_date(start):

    start_time = datetime.strptime(start, '%Y-%m-%d')
    start = start_time - timedelta(days=365)
    temp1=session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >start).all()
    temp_list=list(np.ravel(temp1))
    return jsonify(temp_list)

@app.route("/api/v1.0/<start>/<end>")
def date_between(start,end):

    start_time = datetime.strptime(start, '%Y-%m-%d')
    end_time= datetime.strptime(end, '%Y-%m-%d')
    start = start_time - timedelta(days=365)
    end= end_time- timedelta(days=365)
    temp2=session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >start).filter(Measurement.date <end).all()
    temp_l=list(np.ravel(temp2))
    return jsonify(temp_l)

if __name__ == "__main__":
    app.run(debug=True)