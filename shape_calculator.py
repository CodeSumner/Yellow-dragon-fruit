#https://replit.com/@CodeSumner/boilerplate-polygon-area-calculator#main.py
class Rectangle:
    #names = []
    #name = []
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #Rectangle.name = [self.width, self.height]
        #Rectangle.names.append(Rectangle.name)


    def set_width(self, width):
        self.width = width
        #Rectangle.name[0] = self.width
        return self.width

    def set_height(self, height):
        self.height = height
        #Rectangle.name[1] = self.height
        return self.height

    def get_area(self):
        return self.height * self.width
       

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width
       
    def get_diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** .5
        
    def get_picture(self):
        row = ''
        rows = ''
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            for j in range(self.height):
                for i in range(self.width):
                    row += '*'
                rows += row + '\n'
                row =''
            return rows
    
    def get_amount_inside(self, name):
            if self.width == self.height:
                if name.width == name.height:
                    print(self.side, self.side, name.side)
                    return (self.side//name.side) * (self.side//name.side)
                else:
                    return (self.side//name.width) * (self.side//name.height)
            else:
                if name.width == name.height:
                    print(self.width, self.height, name.side)
                    return (self.width//name.side) * (self.height//name.side)
                else:
                    return (self.width//name.width) * (self.height//name.height)

    def __str__ (self):
        if self.width == self.height:
            return ("Square(side=" + str(self.width) + ")")
        else:
            return ("Rectangle(width=" + str(self.width) + \
                    ", height=" + str(self.height) + ")")


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        Square.side = side
        Rectangle.height = Square.side
        Rectangle.width = Square.side
        #Rectangle.name = [Square.side, Square.side]
        #Rectangle.names.append(Rectangle.name)
    

    def set_side(self, side):
        self.side = side
        Square.side = self.side
        Rectangle.height = Square.side
        Rectangle.width = Square.side
        #Rectangle.name[0] = Rectangle.width
        #Rectangle.name[1] = Rectangle.height
        return "Square(side=" + str(Square.side) + ")"

    def set_height(self, height):
        Square.side = height
        Rectangle.height = Square.side
        Rectangle.width = Square.side
        #Rectangle.name[0] = Rectangle.width
        #Rectangle.name[1] = Rectangle.height
        return "Square(side=" + str(Square.side) + ")"
    
    def set_width(self, width):
        Square.side = width
        Rectangle.width = Square.side
        Rectangle.height = Square.side
        #Rectangle.name[0] = Rectangle.width
        #Rectangle.name[1] = Rectangle.height
        return "Square(side=" + str(Square.side) + ")"



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print('v', rect.get_amount_inside(sq))

rect = Rectangle(3, 6)
sq = Square(5)
print(rect.get_area())
print(sq.get_area())

rect.set_width(4)
rect.set_height(8)
print(rect)
rect2 = Rectangle(4, 8)
print(rect2)
print(rect2.get_amount_inside(rect))

