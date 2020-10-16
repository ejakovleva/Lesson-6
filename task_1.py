from itertools import cycle
from time import sleep


class TrafficLight:
    __color = [chr(128997), chr(129000), chr(129001)]

    def running(self):
        for j in cycle(TrafficLight.__color):
            print(j)
            if TrafficLight.__color.index(j) == 0:
                sleep(7)
            elif TrafficLight.__color.index(j) == 1:
                sleep(2)
            elif TrafficLight.__color.index(j) == 2:
                sleep(5)


traffic_light_1 = TrafficLight()
traffic_light_1.running()
