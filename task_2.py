class Road:
    depth = 5
    kg = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        print(self._length * self._width * Road.kg * Road.depth/1000)


road_1 = Road(5000, 20)
road_1.asphalt_mass()
