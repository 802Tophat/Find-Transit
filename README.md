# Find Transit (Target)
## Description
This program will assist in finding the next transit vehicle leaving a defined  station on a defined route in a defined direction.

API calls are made to https://svc.metrotransit.org/ to return the next available transit pickup, based on user provided information.


## Installing Requirements
    pip install -r requirements.txt


## Notes
You will need to know the following information in order to use this application successfully. For assistance in identifying any of these required fields visit https://www.metrotransit.org/schedules-maps. 

1. Route name.
2. The transit station you want to start your journey from. The station selected must be on the selected route.
3. The primary cardinal direction you plan to travel (North, South, East, West).  The direction selected must be a direction traveled on the selected route.

Example:

    Route Name: "METRO Blue Line"
    Starting Point: "Target Field Station Platform 2"
    Direction: South


## Usage 
    usage: findtransit.py [-h] route start direction

    Example:  findtransit.py "METRO Blue Line" "Target Field Station Platform 1" South

    positional arguments:
        route       Route name of the transit line you are joining.
        start       Transit Station where you will get off.
        direction   Direction you plan to go - North, South, East, West

    optional arguments:
    -h, --help  show this help message and exit


## Example
In this example we are looking for the next train available on the "METRO Blue Line" leaving from "Target Field Station 2" and going South.

    findtransit.py "METRO Blue Line" "Target Field Station Platform 2" south

    The next train on METRO Blue Line going South from Target Field Station Platform 2 is leaving in 8 minutes at 15:35.