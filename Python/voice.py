# Importing Required Libraries
import speech_recognition as sr
import pyttsx3
import requests
from bs4 import BeautifulSoup
import pymongo

# Initializing Voice Assistant
assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id) # Setting female voice
rate = assistant.getProperty('rate')
assistant.setProperty('rate', 150) # Setting speech rate

# Initializing Speech Recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Initializing MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['bus_detection_system']

# Defining Greeting Function
def greet():
    assistant.say("Hello, I am your voice assistant for bus detection. How can I help you?")
    assistant.runAndWait()

# Defining Get Bus Schedule Function
def get_bus_schedule():
    assistant.say("Please wait while I get the bus schedule for you.")
    assistant.runAndWait()
    url = 'http://localhost:5000/get_bus_schedule'
    response = requests.get(url)
    bus_schedules = response.json()['speech_output']
    assistant.say("Here are the bus schedules:")
    assistant.runAndWait()
    for bus in bus_schedules:
        assistant.say(f"Bus number {bus['bus_number']} goes from {bus['bus_route']} at {bus['bus_timing']}.")
        assistant.runAndWait()

# Defining Get Bus Location Function
def get_bus_location():
    assistant.say("Please wait while I get the bus location for you.")
    assistant.runAndWait()
    url = 'http://localhost:5000/get_bus_location'
    response = requests.get(url)
    bus_locations = response.json()['result']
    assistant.say("Here are the bus locations:")
    assistant.runAndWait()
    for bus in bus_locations:
        assistant.say(f"Bus number {bus['bus_number']} is currently at {bus['bus_location']}.")
        assistant.runAndWait()

# Defining Get Bus Station Function
def get_bus_station():
    assistant.say("Please wait while I get the bus station for you.")
    assistant.runAndWait()
    url = 'http://localhost:5000/get_bus_station'
    response = requests.get(url)
    bus_stations = response.json()['result']
    assistant.say("Here are the bus stations:")
    assistant.runAndWait()
    for station in bus_stations:
        assistant.say(f"{station['station_name']} is located at {station['station_location']}.")
        assistant.runAndWait()

# Defining Get Blind People Count Function
def get_blind_people_count():
    assistant.say("Please wait while I get the blind people count for you.")
    assistant.runAndWait()
    url = 'http://localhost:5000/get_blind_people_count'
    response = requests.get(url)
    blind_people_counts = response.json()['result']
    assistant.say("Here are the blind people counts:")
    assistant.runAndWait()
    for blind in blind_people_counts:
        assistant.say(f"There are {blind['blind_people_count']} blind people at {blind['station_name']}.")
        assistant.runAndWait()

# Defining Get Bus Arrival Time Function
def get_bus_arrival_time():
    assistant.say("Please wait while I get the bus arrival time for you.")
    assistant.runAndWait()
    url = 'http://localhost:5000/get_bus_arrival_time'
    response = requests.get(url)
    bus_arrival_times = response.json()['result']
    assistant.say("Here are the bus arrival times:")
    assistant.runAndWait()
    for bus in bus_arrival_times:
        assistant.say(f"Bus number {bus['bus_number']} will arrive at {bus['bus_arrival_time']}.")
        assistant.runAndWait()

# Defining Get Bus Departure Time Function
def get_bus_departure_time():
    assistant.say("Please wait while I get the bus departure time for you.")
    assistant.runAndWait()
    url = 'http://localhost:5000/get_bus_departure_time'
    response = requests.get(url)
    bus_departure_times = response.json()['result']
    assistant.say("Here are the bus departure times:")
    assistant.runAndWait()
    for bus in bus_departure_times:
        assistant.say(f"Bus number {bus['bus_number']} will depart at {bus['bus_departure_time']}.")
        assistant.runAndWait()

# Defining Detect Bus Station Function
def detect_bus_station():
    # Assuming RFID technology is used to detect the presence of blind people at the bus station
    # and the station name is stored in a variable called station_name
    station_name = "Madurai Bus Stand" # For example
    assistant.say(f"You are at {station_name}.")
    assistant.runAndWait()
    # Assuming web scraping is used to get the coming buses and their arrival times
    # and the data is stored in a list of tuples called coming_buses
    coming_buses = [("1", "6:00 AM"), ("2", "7:00 AM"), ("3", "8:00 AM")] # For example
    assistant.say("Here are the coming buses and their arrival times:")
    assistant.runAndWait()
    for bus, time in coming_buses:
        assistant.say(f"Bus number {bus} will arrive at {time}.")
        assistant.runAndWait()

# Defining Detect Bus Function
def detect_bus():
    # Assuming RFID technology is used to detect the presence of blind people on the bus
    # and the bus number and location are stored in variables called bus_number and bus_location
    bus_number = "1" # For example
    bus_location = "Madurai" # For example
    assistant.say(f"You are on bus number {bus_number}.")
    assistant.runAndWait()
    assistant.say(f"The bus is currently at {bus_location}.")
    assistant.runAndWait()
    # Assuming web scraping is used to get the nearby stations and their distances
    # and the data is stored in a list of tuples called nearby_stations
    nearby_stations = [("Chennai Bus Stand", "10 km"), ("Bangalore Bus Stand", "20 km"), ("Coimbatore Bus Stand", "30 km")] # For example
    assistant.say("Here are the nearby stations and their distances:")
    assistant.runAndWait()
    for station, distance in nearby_stations:
        assistant.say(f"{station} is {distance} away from the bus.")
        assistant.runAndWait()

# Defining Announce Bus Arrival Function
def announce_bus_arrival():
    # Assuming RFID technology is used to detect the presence of blind people on the bus
    # and the station name and arrival time are stored in variables called station_name and arrival_time
    station_name = "Chennai Bus Stand" # For example
    arrival_time = "6:00 AM" # For example
    assistant.say(f"The bus will arrive at {station_name} at {arrival_time}.")
    assistant.runAndWait()
    # Assuming RFID technology is used to alert the driver about the number of blind people in the surrounding area of the station
    # and the number is stored in a variable called blind_people_count
    blind_people_count = 3 # For example
    assistant.say(f"There are {blind_people_count} blind people in the surrounding area of the station. Please be careful and help them if needed.")
    assistant.runAndWait()

# Defining Announce Bus Departure Function
def announce_bus_departure():
    # Assuming RFID technology is used to detect the presence of blind people on the bus
    # and the station name and departure time are stored in variables called station_name and departure_time
    station_name = "Chennai Bus Stand" # For example
    departure_time = "6:30 AM" # For example
    assistant.say(f"The bus will depart from {station_name} at {departure_time}.")
    assistant.runAndWait()
    # Assuming RFID technology is used to alert the driver about the number of blind people on the bus
    # and the number is stored in a variable called blind_people_count
    blind_people_count = 2 # For example
    assistant.say(f"There are {blind_people_count} blind people on the bus. Please be careful and help them if needed.")
    assistant.runAndWait()

# Defining Listen Function
def listen():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    voice_data = recognizer.recognize_google(audio)
    return voice_data
