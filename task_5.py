class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Started drawing with a pen {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Started drawing with a pencil {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Started drawing with a handle {self.title}')


brush = Stationery('brush for painting')
brush.draw()

pen = Pen('Erich Krause')
pen.draw()

pencil = Pencil('Red')
pencil.draw()

handle = Handle('Black')
handle.draw()