################################################
# Climate Analysis API
# This Flask application provides routes to analyze climate data stored in a SQLite database.
################################################

# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

#################################################
# Database Setup
#################################################

# Create engine to connect to the SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

# Initialize the Flask app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Homepage route
@app.route("/")
def home():
    """List all available API routes."""
    return (
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a JSON representation of precipitation data for the last year."""
    # Find the most recent date in the data
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    # Calculate the date one year ago
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)
    # Query for date and precipitation
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    # Convert to dictionary
    precipitation_dict = {date: prcp for date, prcp in results}
    return jsonify(precipitation_dict)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    results = session.query(Station.station).all()
    stations_list = list(np.ravel(results))
    return jsonify(stations_list)

# Temperature observations route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of temperature observations for the previous year."""
    # Find the most active station
    most_active_station = session.query(Measurement.station).group_by(Measurement.station)\
        .order_by(func.count(Measurement.station).desc()).first()[0]
    # Find the most recent date in the data
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    # Calculate the date one year ago
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)
    # Query for the temperature observations
    results = session.query(Measurement.date, Measurement.tobs)\
        .filter(Measurement.station == most_active_station)\
        .filter(Measurement.date >= one_year_ago).all()
    # Convert to list of dictionaries
    temperature_dict = {date: tobs for date, tobs in results}
    return jsonify(temperature_dict)

# Start and End range route
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_range(start, end=None):

    """Return TMIN, TAVG, and TMAX for a given start or start-end range."""
    
    # Define the selection (TMIN, TAVG, TMAX)
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    if not end:
        # Query when only `start` is provided
        results = session.query(*sel).filter(Measurement.date >= start).all()
    else:
        # Query when both `start` and `end` are provided
        results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    # Check if results are empty
    if not results or not results[0][0]:
        return jsonify({"error": f"No data found for date range {start} to {end if end else 'latest'}."}), 404

    # Convert the results into a dictionary for JSON response
    temperature_stats = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    return jsonify(temperature_stats)

########################################
# Main Application Entry
########################################

if __name__ == "__main__":
    app.run(debug=True)
