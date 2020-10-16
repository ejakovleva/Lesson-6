class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(sum(self._income.values()))


income_1 = {"wage": 100000, 'bonus': 20000}
worker_1 = Position("John", "Snow", "the king", income_1)
worker_1.get_full_name()
worker_1.get_total_income()

income_2 = {"wage": 150000, 'bonus': 20000}
worker_2 = Position("Geralt", "of Reivia", 'the witcher', income_2)
worker_2.get_full_name()
worker_2.get_total_income()
