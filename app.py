from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Function to connect to MongoDB
def get_mongo_data(db_name, collection_name):
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]
    return list(collection.find({}, {'_id': 0}))  # Return data excluding '_id'

# API endpoint to fetch weather data
@app.route('/weather', methods=['GET'])
def get_weather():
    weather_data = get_mongo_data('weather_db', 'weather_data')
    return jsonify(weather_data)

# API endpoint to fetch titles
@app.route('/titles', methods=['GET'])
def get_titles():
    titles_data = get_mongo_data('web_data', 'scraped_titles')
    return jsonify(titles_data)

# Serve the frontend HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
