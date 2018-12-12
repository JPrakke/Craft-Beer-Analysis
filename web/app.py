from flask import Flask, jsonify, render_template
# import numpy as np
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func, MetaData
# from sqlalchemy.pool import StaticPool
# import datetime as dt
# from datetime import date

#################################################
# Database Setup
#################################################

# engine = create_engine("sqlite:///Resources/hawaii.sqlite",
#     connect_args={'check_same_thread':False},
#     poolclass=StaticPool)



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
    """ api page"""
    return render_template("api.html")



if __name__ == '__main__':
    app.run(debug=False)