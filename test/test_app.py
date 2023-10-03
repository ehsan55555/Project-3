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
crashes = Base.classes.crashes_table
persons = Base.classes.persons_table  

@app.route('/')
def welcome():
    # Render the 'your_template.html' file located in the 'templates' folder
    return render_template('test_html.html')


# Define a route to serve the dashboard page
# Define a route to serve the dashboard page
@app.route('/api/data')
def get_data():
    # Create a session to interact with the database
    session = Session(engine)

    # Query the database to retrieve the data you want
    results = session.query(crashes).all()

    session.close()

    # Convert query results to a list of dictionaries
    data_results = []
    for row in results:
        row_dict = {column.name: getattr(row, column.name) for column in crashes.__table__.columns}
        data_results.append(row_dict)

    return jsonify(data_results)

if __name__ == '__main__':
    app.run(debug=True)
