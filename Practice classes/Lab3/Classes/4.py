import math  

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        """Выводит координаты точки"""
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        """Изменяет координаты точки"""
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        """Вычисляет расстояние до другой точки"""
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)

p1 = Point(3, 4)
p2 = Point(7, 1)

p1.show()  
p2.show()  

distance = p1.dist(p2)
print(f"Расстояние между точками: {distance}")  

p1.move(10, 10)  
p1.show()  
