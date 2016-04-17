#120 kilometers per hour = 33.33 meters per second

# car[0] begins the row of cars at the very end of the road, and we are going
# backwards, so [[1] starts at car[0]-1000/33 m. So on...

import random
import numpy as np


class Car():

    def __init__(self, starting_position, preceding_car, starting_speed = 0, accelerate = 2, decelerate = 2, max_speed = 1000/33):

        colors_list = ("green", "pink", "black", "blue", "yellow", "white", "magenta")
        self.color = random.choice(colors_list)
        # the starting position will be assigned to the vehicles in reverse order
        # along the road, evenly distributed
        self.position = starting_position
        # each car will start on the road at once, at the intial speed of 0.
        self.starting_speed = starting_speed
        # we need to find the speed of the car which will increase by 2 m/s based a run time of 60 seconds. At second 0, speed = accelerate*0 = 0 because it is not moving
        # after 1 second, the car speed = 2 m/s.
        self.speed = accelerate * (0, 61)  # (m/s)/s


    def __str__(self):
        intro = "Car {}, Starting Position: {}, Speed: {} m/s, Distance from Car in Front: {}, Total Distance Traveled: {}."
        return str(intro.format(self.id, self.position, self.speed, self.preceding_car.postion, self.distance))

    def distance_check_of_car_in_front(self):
        """This function will determine the distance between the preceding car and car.
        The input is the position of preceding car and the position of car.
        The preceding car positon minus the position of car = the distance."""
        self.distance = self.preceding_car.position - self.position
        return self.distance

    def check_speed(self):
        return self.speed

    def check_if_car_can_move(self):
        """This function will check whether a car can move forward.
        The input is the distance_check_of_car_in_front.
        If distance_check_of_car_in_front > 2 m: True
        Else: False"""
        if self.distance > 2:
            return self.accelerate
        else:
            pass

    def move_the_car(self):
        """This function will move the vehicle forward by an acceleration rate of 2 m/s to the maximum speed of 33.33 m/s if distance >= 33.33 m.
        The input of this function is the distance between the cars.
        If the check_distance >= the speed of the preceding car: car = accelerate up to a distance = preceding car speed.
        Else: car speed == car speed.
        The minimum distance = rate of acceleration = 2 m/s."""
        if self.speed <= 1000/30:
            return self.accelerate

    def random_slow_down(self):
        """This function will randomly select a car to slow down at a rate of 2 (m/s)/s. There is a 10% that a car will be chosen,
        so the range only needs to include 10 numbers."""
        slow_down = random.randint(1,10)
        if slow_down == 1:
            self.speed -= 2
            return self.speed
        else:
            pass

#     def calculate_ideal_speed():
#         """This function will calculate the optimal speed for a car in traffic on the road.
#         The optimal speed <= 33.33 m/s and <= speed of preceding car."""


class TrafficSim():

    def __init__(self):
        self.cars = []
        preceding_car = None

        """Creates the cars"""
        for x in range(30):
            # the car will "start" where the front of his bumper is on the road.
            car = Car(967 - (x*33), preceding_car)
            car.id = x
            car.front_bumper = 967 - (x*33)
            car.rear_bumper = 962 - (x*33)
            preceding_car = car
            car.original_start = 967 - (x*33)

            self.cars.append(car)

            preceding_car = car

        self.cars[0].preceding_car = self.car[-1]

    def run(self):

        print("Test Run")
        sim_timer = 0
        data_set = []

        while sim_timer < 61:

            for car in road.cars:
                car.random_slow_down()
                print(car)

            for car in road.cars:
                car.distance_check_of_car_in_front()
                print(car)

            for car in road.cars:
                car.check_speed()
                print(car)

            for car in road.cars:
                car.move_the_car()

        sim_timer += 1

        print("End of Test")
