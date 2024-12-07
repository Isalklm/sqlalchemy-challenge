<<<<<<< HEAD
# sqlalchemy-challenge

## Project Overview
This project focuses on analyzing climate data stored in a SQLite database using Flask and SQLAlchemy. The challenge involves creating an API with dynamic and static routes, querying the database, and visualizing the data. The project is divided into the following key tasks:

1. **Database Setup**: Setting up and reflecting the database tables using SQLAlchemy.
2. **API Development**: Building a Flask API with multiple routes to serve JSON responses.
3. **Data Analysis and Visualization**: Querying precipitation and station data and visualizing temperature observations.

---

## Files Included
The project contains the following files and directories:
- **climate_analysis.py**: The main Python script for creating the Flask API and performing data analysis.
- **README.md**: This documentation file.
- **Resources/**: Contains all supporting data files:
  - **hawaii.sqlite**: The SQLite database file containing climate data.
  - **hawaii_measurements.csv**: The CSV file with measurement data.
  - **hawaii_stations.csv**: The CSV file with station data.

---

## Instructions for Running the Project
1. **Install Dependencies**:
   - Ensure Python is installed on your system.
   - Install the required Python libraries:
     ```bash
     pip install flask sqlalchemy pandas matplotlib
     ```

2. **Set Up the Database**:
   - Ensure the `hawaii.sqlite` file is in the `Resources` directory.

3. **Run the Flask App**:
   - Start the Flask application by running the following command:
     ```bash
     python climate_analysis.py
     ```
   - Open your browser and navigate to `http://127.0.0.1:5000/` to view the available routes.

4. 4. **Access API Routes**:
   - `/api/v1.0/precipitation`: Returns precipitation data for the last 12 months.
   - `/api/v1.0/stations`: Returns a list of weather stations.
   - `/api/v1.0/tobs`: Returns temperature observations for the most active station.
   - `/api/v1.0/<start>`: Replace `<start>` with a date in the format `YYYY-MM-DD` (e.g., `/api/v1.0/2017-01-01`) to get TMIN, TAVG, and TMAX from the specified start date onward.
   - `/api/v1.0/<start>/<end>`: Replace `<start>` and `<end>` with dates in the format `YYYY-MM-DD` (e.g., `/api/v1.0/2017-01-01/2017-01-15`) to get TMIN, TAVG, and TMAX for the specified date range.

5. **Visualize Data**:
   - Run the Python script to generate precipitation and temperature visualizations.
   - The graphs will display in a pop-up window during execution.

---

## Breakdown of Tasks

### Static Routes:
- `/api/v1.0/precipitation`: Queries precipitation data and returns a JSON dictionary with date and precipitation values.
- `/api/v1.0/stations`: Retrieves all weather station IDs and returns them as a JSON list.
- `/api/v1.0/tobs`: Fetches temperature observations for the most active station in the last 12 months.

### Dynamic Routes:
- `/api/v1.0/<start>`: Accepts a start date in the format `YYYY-MM-DD` and calculates TMIN, TAVG, and TMAX from the start date onward.
- `/api/v1.0/<start>/<end>`: Accepts a start and end date and calculates TMIN, TAVG, and TMAX for the given date range.

---

## Attribution and Code Sources
- This project was developed as part of a bootcamp program.
- All code and visualizations were created independently unless explicitly mentioned.
- Class resources and support were used to complete this challenge.

---


=======
# sqlalchemy-challenge
>>>>>>> da34df60aaf00eccea98702aa05fde60d0698e7c
