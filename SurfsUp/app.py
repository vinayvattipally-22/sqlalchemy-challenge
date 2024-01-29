# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables 'measurement' and 'station'
Base.prepare(autoload_with=engine)

# Save reference to the table 'measurement' and 'station'
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################


# craete the root route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"api/v1.0/stations<br/>"
        f"api/v1.0/tobs<br/>"
        f"api/v1.0/<start><br/>"
        f"api/v1.0/<start>/<end>"
    )

# create the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of all precipitation"""
    # Query all precipitation
    results = session.query(Measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    all_precipitation = list(np.ravel(results))

    return jsonify(all_precipitation)

# create the stations route
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of all stations"""
    # Query all stations
    results = session.query(Measurement.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

# create the tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of all tobs"""
    # Query all tobs
    results = session.query(Measurement.tobs).all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(results))

    return jsonify(all_tobs)

# create the start route where the user can enter a start date
@app.route("/api/v1.0/<start>")
def get_temperature_stats_start(start):
    """Return TMIN, TAVG, and TMAX for the dates greater than or equal to the start date."""
    # Open a session
    session = Session(engine)

    # Query TMIN, TAVG, and TMAX
    results = session.query(func.min(Measurement.tobs).label("TMIN"),
                            func.avg(Measurement.tobs).label("TAVG"),
                            func.max(Measurement.tobs).label("TMAX")) \
                    .filter(Measurement.date >= start).all()

    session.close()

    # Convert the result to a dictionary
    result_dict = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    return jsonify(result_dict)

# create the start/end route where the user can enter a start and end date
@app.route("/api/v1.0/<start>/<end>")
def get_temperature_stats_start_end(start, end):
    """Return TMIN, TAVG, and TMAX for the dates from start to end."""
    # Open a session
    session = Session(engine)

    # Query TMIN, TAVG, and TMAX
    results = session.query(func.min(Measurement.tobs).label("TMIN"),
                            func.avg(Measurement.tobs).label("TAVG"),
                            func.max(Measurement.tobs).label("TMAX")) \
                    .filter(Measurement.date >= start, Measurement.date <= end).all()

    session.close()

    # Convert the result to a dictionary
    result_dict = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    return jsonify(result_dict)



if __name__ == '__main__':
    app.run(debug=True)

