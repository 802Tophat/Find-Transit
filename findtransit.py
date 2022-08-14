import sys
import requests
from datetime import datetime
import pytz
import argparse


# Define arguments used to get route information
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description='Example:  findtransit.py "METRO Blue Line" "Target Field Station Platform 1" South')
parser.add_argument('start', type=str, help="Route name or number of the transit line you are joining.")
parser.add_argument('stop', type=str, help="Transit Station where you will get off.")
parser.add_argument('direction', type=str, help="Direction you plan to go - North, South, East, West")
args = parser.parse_args()


# Identify the bus route names and IDs
get_routes = requests.get(url="https://svc.metrotransit.org/nextripv2/routes")
routes = get_routes.json()
for i in routes:
    if i['route_label'] == args.start:
        route_id = (i['route_id'])
        break
else:
    print('''
    Please provide a valid beginning route name (case sensitive).
    Use quotations, if your route has more than one word.
    For example: "METRO Blue Line" or "Route 723".
    ''')
    sys.exit()


# Confirm the user can travel in the requested direction
get_directions = requests.get(url="https://svc.metrotransit.org/nextripv2/directions/" + route_id)
directions = get_directions.json()
direction = args.direction.capitalize() + "bound"
for i in directions:
    if i['direction_name'] == direction:
        direction_id = str((i['direction_id']))
        break
else:
    print('''
    Please provide a valid direction of travel for the requested route.
    For example: North, South, East, West
    ''')
    sys.exit()


# Match Destination and Place Code
get_stops = requests.get(url="https://svc.metrotransit.org/nextripv2/stops/" + route_id + "/" + direction_id)
stops = get_stops.json()
for i in stops:
    if i['description'] == args.stop:
        place_code = (i['place_code'])
        break
else:
    print('''
    Please provide a valid Transit Station destination (case sensitive).
    Use quotations, if your route has more than one word.
    For example: "Target Field Station Platform 2" or "MSP Airport Terminal 2 - Humphrey Station"
    ''')
    sys.exit()
# Get departure times for the requested route, direction, and stop.
get_bus_departure = requests.get(url="https://svc.metrotransit.org/nextripv2/" + route_id + "/" + direction_id + "/" + place_code)
bus_departure = get_bus_departure.json()
# Calculate time for next pickup, current time, and difference between times.
if (bus_departure['departures'][0]['departure_time']):
    timezone = pytz.timezone('America/Chicago')
    departure_epoch = (bus_departure['departures'][0]['departure_time'])
    departure_time = datetime.fromtimestamp(departure_epoch, tz=timezone)
    current_time = datetime.now(timezone)
    minutes_remaining = int((departure_time - current_time).total_seconds() / 60)
else:
    print('''
    There are no more transit services for this selected route today.  
    Please try again later.
    ''')
    sys.exit()


# Determine the type of vechile
get_transit = requests.get(url="https://svc.metrotransit.org/nextripv2/vehicles/" + route_id)
transit = get_transit.json()
for i in transit:
    if 'RAIL' in i['trip_id']:
        vehicle = 'train'
    elif 'BUS' in i['trip_id']:
        vehicle = 'bus'
    else:
        # If we can't determine a vehicle type use a generic term for vehicle type.
        vehicle = 'pickup'

# Inform the user of the status of their next depature.
print(f"The next {vehicle} at {args.start} going {args.direction} towards {args.stop} is leaving in {minutes_remaining} minutes at {departure_time:%H:%M}.")