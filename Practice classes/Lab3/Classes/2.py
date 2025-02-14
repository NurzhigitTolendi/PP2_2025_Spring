class Shape:
    def __init__(self):
        pass  
    
    def area(self):
        return 0  

class Square(Shape):
    def __init__(self, length):
        super().__init__()  
        self.length = length  
    
    def area(self):
        return self.length ** 2 

# Example usage
shape = Shape()
print("Shape area:", shape.area()) 

length1 = int(input())
square = Square(length1)
print("Square area:", square.area())  
