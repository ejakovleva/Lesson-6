from random import randint
from time import sleep
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} has moved off")

    def stop(self):
        print(f"{self.name} car has stopped")

    def turn(self):
        direction = [randint(1, 3) for _ in range(4)]
        for i in direction:
            sleep(2)
            if i == 1:
                print(f"{self.name} turned to the right")
                sleep(2)
            if i == 2:
                print(f"{self.name} turned to the left")
                sleep(1)
            if i == 3:
                print(f"{self.name} turned around")
                sleep(1)

    def show_speed(self):
        for i in self.speed:
            print(f"Your speed is {i} km/h")
            sleep(1)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        for i in self.speed:
            if i > 60:
                print(f'Your speed is {i} km/h! You are going over the speed limit!')
            else:
                print(f"Your speed is {i} km/h")
            sleep(1)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        for i in self.speed:
            if i > 40:
                print(f'Your speed is {i} km/h! You are going over the speed limit!')
            else:
                print(f'f"Your speed is {i} km/h"')
            sleep(1)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car_1 = PoliceCar(60, 'white', 'Lada Police', True)
car_1.go()
car_1.turn()
car_1.stop()
sleep(1)

speed_list_1 = [randint(0, 150) for _ in range(5)]
town_car_1 = TownCar(speed_list_1, "red", 'Mercedes', False)
sleep(1)
town_car_1.go()
town_car_1.show_speed()
town_car_1.stop()

work_car_1 = WorkCar(speed_list_1, "yellow", 'Ford', False)
work_car_1.go()
work_car_1.show_speed()
work_car_1.turn()
work_car_1.stop()

speed_list_2 = [randint(0, 250) for _ in range(5)]
sport_car_1 = SportCar(speed_list_2, 'white', 'Audi', False)
sport_car_1.go()
sport_car_1.show_speed()
sport_car_1.stop()

print(car_1.name, car_1.color, car_1.is_police)
print(town_car_1.name, town_car_1.color, town_car_1.is_police)
print(work_car_1.name, work_car_1.color, work_car_1.is_police)
print(sport_car_1.name, sport_car_1.color, sport_car_1.is_police)