# Hawaii Weather Analysis and API

This project includes a Jupyter Notebook for weather analysis in Hawaii and a Flask API to serve temperature-related data.

## Jupyter Notebook

### Introduction

The Jupyter Notebook (`climate_starter.ipynb`) performs exploratory analysis on weather data in Hawaii. It includes visualizations of precipitation trends and temperature observations.

### Dependencies

Ensure you have the following dependencies installed:

- Matplotlib
- NumPy
- Pandas
- SQLAlchemy

Install dependencies using:

```bash
pip install matplotlib numpy pandas sqlalchemy

```

## How to run

. Open the Jupyter Notebook in a Jupyter environment.
. Run each cell sequentially to perform


# Hawaii Weather Flask API

This Flask API serves temperature-related data for weather analysis in Hawaii.

## Flask Setup

### Dependencies

Ensure you have Flask installed:

```bash
pip install Flask
```

## How to Run

. Navigate to the directory containing app.py.
. Run the Flask application using:
    ```bash
    python app.py
    ```

    The API will be accessible at http://localhost:5000.

### API Endpoints

    Root Endpoint
    URL: /
    Description: Lists all available API routes.
    Example: http://localhost:5000/

### Precipitation Endpoint
    URL: /api/v1.0/precipitation
    Description: Returns a list of all precipitation data.
    Example: http://localhost:5000/api/v1.0/precipitation

### Stations Endpoint
    URL: /api/v1.0/stations
    Description: Returns a list of all weather stations.
    Example: http://localhost:5000/api/v1.0/stations

### TOBS (Temperature Observations) Endpoint
    URL: /api/v1.0/tobs
    Description: Returns a list of all temperature observations.
    Example: http://localhost:5000/api/v1.0/tobs

### Start Endpoint
    URL: /api/v1.0/<start>
    Description: Returns TMIN, TAVG, and TMAX for dates greater than or equal to the specified start date.
    Example: http://localhost:5000/api/v1.0/2016-08-24

### Start/End Endpoint
    URL: /api/v1.0/<start>/<end>
    Description: Returns TMIN, TAVG, and TMAX for dates from start to end (inclusive).
    Example: http://localhost:5000/api/v1.0/2016-08-24/2016-08-30
