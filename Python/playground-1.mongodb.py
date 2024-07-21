from pymongo import MongoClient

# Initializing MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['bus_detection_system']

# Creating Bus Schedule Collection
bus_schedule = db['bus_schedule']
bus_schedule_data = [
    {
        'bus_number': '1',
        'bus_route': 'Madurai to Chennai',
        'bus_timing': '6:00 AM'
    },
    {
        'bus_number': '2',
        'bus_route': 'Madurai to Bangalore',
        'bus_timing': '7:00 AM'
    },
    {
        'bus_number': '3',
        'bus_route': 'Madurai to Coimbatore',
        'bus_timing': '8:00 AM'
    }
]
bus_schedule.insert_many(bus_schedule_data)

# Creating Bus Location Collection
bus_location = db['bus_location']
bus_location_data = [
    {
        'bus_number': '1',
        'bus_location': 'Madurai'
    },
    {
        'bus_number': '2',
        'bus_location': 'Bangalore'
    },
    {
        'bus_number': '3',
        'bus_location': 'Coimbatore'
    }
]
bus_location.insert_many(bus_location_data)

# Creating Bus Station Collection
bus_station = db['bus_station']
bus_station_data = [
    {
        'station_name': 'Madurai Bus Stand',
        'station_location': 'Madurai'
    },
    {
        'station_name': 'Chennai Bus Stand',
        'station_location': 'Chennai'
    },
    {
        'station_name': 'Bangalore Bus Stand',
        'station_location': 'Bangalore'
    },
    {
        'station_name': 'Coimbatore Bus Stand',
        'station_location': 'Coimbatore'
    }
]
bus_station.insert_many(bus_station_data)

blind_people_count = db['blind_people_count']
blind_people_count_data = [
    {
        'station_name': 'Madurai Bus Stand',
        'blind_people_count': 5
    },
    {
        'station_name': 'Chennai Bus Stand',
        'blind_people_count': 3
    },
    {
        'station_name': 'Bangalore Bus Stand',
        'blind_people_count': 2
    },
    {
        'station_name': 'Coimbatore Bus Stand',
        'blind_people_count': 4
    }
]
blind_people_count.insert_many(blind_people_count_data)

# Creating Bus Arrival Time Collection
bus_arrival_time = db['bus_arrival_time']
bus_arrival_time_data = [
    {
        'bus_number': '1',
        'bus_arrival_time': '6:00 AM'
    },
    {
        'bus_number': '2',
        'bus_arrival_time': '7:00 AM'
    },
    {
        'bus_number': '3',
        'bus_arrival_time': '8:00 AM'
    }
]
bus_arrival_time.insert_many(bus_arrival_time_data)

# Creating Bus Departure Time Collection
bus_departure_time = db['bus_departure_time']
bus_departure_time_data = [
    {
        'bus_number': '1',
        'bus_departure_time': '6:30 AM'
    },
    {
        'bus_number': '2',
        'bus_departure_time': '7:30 AM'
    },
    {
        'bus_number': '3',
        'bus_departure_time': '8:30 AM'
    }
]
bus_departure_time.insert_many(bus_departure_time_data)

