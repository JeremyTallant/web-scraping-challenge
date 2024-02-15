from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Function to clear data from MongoDB
def clear_mongodb_data():
    # Drop the collection to clear all data
    mongo.db.collection.drop()

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update_one and upsert=True
    mongo.db.collection.update_one({}, {'$set': mars_data}, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)