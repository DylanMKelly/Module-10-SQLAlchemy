# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii,sqlite")

# reflect an existing database into a new model
Base = automap_base
# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
measure = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """All API routes."""
    return(
        f"Available Routes:<br/>"
        f"Precipitation Analysis: /api/v.10/precipitation<br/>"
        f"Stations: /api/v.10/stations<br/>"
        f"Temperature Observation: /api/v.10/tobs<br/>"
        f"Start: /api/v.10/<start>"
        f"Close: /api/v.10/<start>/<end>"
    )

@app.route("/api/v.10/precipitation")
def precipitation():
    #Create our session link
    session = Session(engine)
    year_from_current = (dt.date(2017,8,23)) - (dt.timedelta(days = 365))
    results = session.query(measure.date,measure.prcp).filter(measure.date >= year_from_current)
    #Close session
    session.close()

    precipitation = []
    for date, prcp in results
        precipitation_dict = {}
        precipitation_dict["Name"] = date
        precipitation_dict["Precipitation"] = prcp
        precipitation.append(precipitation_dict)
    return jsonify(precipitation)


@app.route("/api/v.10/stations")
def stations():
    #Create our session link
    session = Session(engine)
    results = session.query(station.station, station.id).all()
    #Close session
    session.close()

    all_stations = []
    for station, id in results
        stations_dict = {}
        stations_dict["Station"] = station
        stations_dict["ID"] = id
        all_stations.append(stations_dict)
    return jsonify(all_stations)


@app.route("/api/v.10/tobs")
def tobs():
    #Create our session link
    session = Session(engine)



@app.route("api/v.10/<starts>")
def start():
    #Create our session link
    session = Session(engine)


@app.route("/api/v.10/<starts>/<end>")
def start_end():
