class Shape:
    def __init__(self,color="Red"):
        self.color=color

class Rectangle(Shape):
    def __init__(self,color,width,height):
        super().__init__(color)
        self.width =width
        self.height =height
rect = Rectangle("blue",10,5)
print(rect.color)
        

