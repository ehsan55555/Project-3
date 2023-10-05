import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template


app = Flask(__name__)

# Connect to the PostgreSQL database (replace placeholders with your database info)
engine = create_engine("postgresql://postgres:postgres@localhost:5432/used_car_data")

Base = automap_base()
Base.prepare(autoload_with=engine)

# Map the appropriate class to your PostgreSQL table
borough = Base.classes.brgh_collisions
percentages = Base.classes.death_per_table
numbers = Base.classes.num_death_per_table
injuries = Base.classes.total_injuries

@app.route('/')
def welcome():
    # Render the 'your_template.html' file located in the 'templates' folder
    return render_template('test_html.html')


# Define a route to serve the dashboard page

@app.route('/api/collision')
def borough_collision_data():
    # Create a session to interact with the database
    session = Session(engine)

    # Query the database to retrieve the data you want
    results = session.query(borough).all()

    session.close()

    # Convert query results to a list of dictionaries
    borough_collisions_results = []
    for row in results:
        row_dict = {column.name: getattr(row, column.name) for column in borough.__table__.columns}
        borough_collisions_results.append(row_dict)

    return jsonify(borough_collisions_results)

@app.route('/api/collision_deaths')
def percentage_data():
    # Create a session to interact with the database
    session = Session(engine)

    # Query the database to retrieve the data you want
    results = session.query(percentages).all()

    session.close()

    # Convert query results to a list of dictionaries
    percentages_results = []
    for row in results:
        row_dict = {column.name: getattr(row, column.name) for column in percentages.__table__.columns}
        percentages_results.append(row_dict)

    return jsonify(percentages_results)

@app.route('/api/collision_deaths_num')
def num_data():
    # Create a session to interact with the database
    session = Session(engine)

    # Query the database to retrieve the data you want
    results = session.query(numbers).all()

    session.close()

    # Convert query results to a list of dictionaries
    numbers_results = []
    for row in results:
        row_dict = {column.name: getattr(row, column.name) for column in numbers.__table__.columns}
        numbers_results.append(row_dict)

    return jsonify(numbers_results)

@app.route('/api/injuries')
def injuries_data():
    # Create a session to interact with the database
    session = Session(engine)

    # Query the database to retrieve the data you want
    results = session.query(injuries).all()

    session.close()

    # Convert query results to a list of dictionaries
    injuries_results = []
    for row in results:
        row_dict = {column.name: getattr(row, column.name) for column in injuries.__table__.columns}
        injuries_results.append(row_dict)

    return jsonify(injuries_results)

if __name__ == '__main__':
    app.run(debug=True)
