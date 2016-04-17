# Road Rage

The purpose of this project was to complete a simulation of vehicles driving a stretch of road for 1000 meters over a period of time of 60 seconds.

The 30 vehicles would start "driving" the road all at the same time, starting at evenly spaced distances(ie. car1 would start at 1000 meters, and the next car2 would start at 967 meters; measuring from the front of car1's from bumper to the front bumper of car2). The vehicles would start from a dead stop and accelerate at a constant rate of 2(m/s)/s.

Our pinnacle objective is to find the optimal speed that a vehicle could travel without running into the car in front of it, while maintaining a distance between the car in front of it equal to the traveling current speed.

The optimal speed limit for this road is equal to one standard deviation above the average speed.

Mean = (sum of the fastest speed of all 30 vehicles over the course of 60 seconds) / 30.

Variance = sum((the differences between the mean and each individual car's fastest speed)^2) / 30.

Standard Deviation = square root of Variance

General Assumptions:
  The maximum speed is capped at 33.3333 m/s.
  The cars all measure 5 meters long.
  Every second, 3 out of the 30 vehicles will randomly decelerate at a rate of 2(m/s)/s.
  The road is one lane, thus not allowing for passing.
  Although not road is not circular, to generate a simulation that allows for a continuous stream of traffic, when a vehicle gets to the end of the road (1000m), the vehicle will return to the beginning of the road (0m).

## Getting Started

This simple python program can be run by opening the terminal, using the python3 command and running road_rage.py
There is also a more interactive file which can be opened in the jupyter notebook.


### Pre-requisities

To be able to install this software, your machine needs to have python3 installed. The other requirements can be found on the requirements.txt file.


### Installing

Begin by opening your terminal and running python3 on the command line. Run road_rage.py to view the simulation of the vehicles and the average speed they were able to travel at over the course of 60 seconds. The jupyter notebook shows a graph of the position of the vehicles at specific times on a normal (x,y) coordinate plane.


## Built With

jupyter notebook
atom


## Authors

The authors of road_rage.py were David Mohrmann and Ryan Oakes.
# traffic-simulation
