from flask import Flask, jsonify, render_template
from config import username, password
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.pool import StaticPool
import datetime as dt
from datetime import date

# ################################################
#  Database Setup
# ################################################

# connection_string = (f"{username}:{password}@127.0.0.1:3306/craftbeerDB")

# engine = create_engine(f'mysql://{connection_string}',encoding='utf-8',connect_args={'check_same_thread':False},
#     poolclass=StaticPool)

# Base= automap_base()
# Base.prepare(engine, reflect=True)

# Beer = Base.classes.beer
# Breweries = base.classes.breweries

# session. Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
@app.route("/home")
def home():
    """ home page of site """
    return render_template("index.html")

@app.route("/ABV_vs_style")
def abv_vs_style(): 
    """ abv vs style page"""
    return render_template("ABV_vs_style.html")

@app.route("/data")
def data(): 
    """ data page"""
    return render_template("data.html")

@app.route("/ETL_work")
def ETL_work(): 
    """ ETL page"""
    return render_template("ETL_work.html")

@app.route("/locations")
def locations(): 
    """ locations page"""
    return render_template("locations.html")

@app.route("/popular_styles")
def popular_styles(): 
    """ popular_styles page"""
    return render_template("popular_styles.html")

@app.route("/api")
def api(): 
    """ returns api.html and list of api routes """
    api_routes = [
        "/api/v1.0/beer",
        "/api/v1.0/breweries",
        "/api/v1.0/topStyles"
    ]
    return render_template("api.html", api_routes = api_routes)

@app.route("/api/v1.0/beer")
def beer():
    """json of all beer in dataset"""
    return("beer")

@app.route("/api/v1.0/breweries")
def breweries():
    """json of all breweries in dataset"""
    return("breweries")

@app.route("/api/v1.0/topStyles")
def topStyles():
    """ json of top 10 beer styles"""
    return("topStyles")

if __name__ == '__main__':
    app.run(debug=False)