# Importing Required Libraries
from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
from voice import get_bus_schedule, get_bus_location, get_bus_station, get_blind_people_count  # Import your voice functions

app = Flask(__name__)
CORS(app)  

client = MongoClient('mongodb://localhost:27017/')
db = client['bus_detection_system']
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/get_bus_schedule', methods=['GET'])
def trigger_voice_assistant_for_bus_schedule():
    response = get_bus_schedule() 
    return jsonify({'speech_output': response})  # Return speech output as JSON


# API to get Bus Schedule
'''@app.route('/get_bus_schedule', methods=['GET'])
def get_bus_schedule():
    
    bus_schedule = db.bus_schedule.find()
    output = []
    for bus in bus_schedule:
        output.append({'bus_number': bus['bus_number'], 'bus_route': bus['bus_route'], 'bus_timing': bus['bus_timing']})
    return jsonify({'result': output})'''

# API to get Bus Location
@app.route('/get_bus_location', methods=['GET'])
def get_bus_location():
    bus_location = db.bus_location.find()
    output = []
    for bus in bus_location:
        output.append({'bus_number': bus['bus_number'], 'bus_location': bus['bus_location']})
    return jsonify({'result': output})

# API to get Bus Station
@app.route('/get_bus_station', methods=['GET'])
def get_bus_station():
    bus_station = db.bus_station.find()
    output = []
    for bus in bus_station:
        output.append({'station_name': bus['station_name'], 'station_location': bus['station_location']})
    return jsonify({'result': output})

# API to get Blind People Count
@app.route('/get_blind_people_count', methods=['GET'])
def get_blind_people_count():
    blind_people_count = db.blind_people_count.find()
    output = []
    for blind in blind_people_count:
        output.append({'station_name': blind['station_name'], 'blind_people_count': blind['blind_people_count']})
    return jsonify({'result': output})

# API to get Bus Arrival Time
@app.route('/get_bus_arrival_time', methods=['GET'])
def get_bus_arrival_time():
    bus_arrival_time = db.bus_arrival_time.find()
    output = []
    for bus in bus_arrival_time:
        output.append({'bus_number': bus['bus_number'], 'bus_arrival_time': bus['bus_arrival_time']})
    return jsonify({'result': output})

# API to get Bus Departure Time
@app.route('/get_bus_departure_time', methods=['GET'])
def get_bus_departure_time():
    bus_departure_time = db.bus_departure_time.find()
    output = []
    for bus in bus_departure_time:
        output.append({'bus_number': bus['bus_number'], 'bus_departure_time': bus['bus_departure_time']})
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True)
# API to get Bus Schedule, Location, and Station
@app.route('/', methods=['GET'])
def get_bus_info():
    try:
        bus_schedule = db.bus_schedule.find()
        bus_location = db.bus_location.find()
        bus_station = db.bus_station.find()

        output = {
            'bus_schedule': [{'bus_number': bus['bus_number'], 'bus_route': bus['bus_route'], 'bus_timing': bus['bus_timing']} for bus in bus_schedule],
            'bus_location': [{'bus_number': bus['bus_number'], 'bus_location': bus['bus_location']} for bus in bus_location],
            'bus_station': [{'station_name': bus['station_name'], 'station_location': bus['station_location']} for bus in bus_station]
        }

        return jsonify({'result': output})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
# Importing necessary libraries
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Defining API endpoint
@app.route('/get_bus_schedule', methods=['GET'])
def get_bus_schedule():
    try:
        api_url = 'http://localhost:5000/get_bus_schedule'
        response = requests.get(api_url)
        bus_schedules = response.json()['result']
    
        return jsonify({'response': 'Bus schedules retrieved successfully!'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

