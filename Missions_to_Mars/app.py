from flask import Flask 
from flask import render_template
from flask import redirect
from flask import request
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pymongo
import scrape_mars

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def index():
    # return "<h1>Mission to Mars -THE APP IS RUNNING!</h>"
   
    mars = mongo.db.mars.find_one()

    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():

    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()

    mars.update({}, mars_data, upsert=True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)