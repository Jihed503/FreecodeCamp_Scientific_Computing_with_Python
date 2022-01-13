class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height
  
  def get_area(self):
      return self.width*self.height

  def get_perimeter(self):
      return 2*self.width + 2*self.height

  def get_diagonal(self):
      return (self.width**2 + self.height**2)**.5
  
  def get_picture(self):
      if self.width > 50 or self.width > 50 :
        return 'Too big for picture.'
      ch = ''
      for i in range(self.height) :
        ch += self.width*'*' + '\n'
      return ch
 
  def get_amount_inside(self,s):
     #if s.width <= self.width and s.height <= self.height:
     if s.get_perimeter() <= self.get_perimeter() and s.get_diagonal() <= self.get_diagonal():
       return self.get_area() // s.get_area()
     else: return 0

  def __str__(self):
    return 'Rectangle(width={}, height={})'.format(self.width, self.height)


class Square(Rectangle):
  def __init__(self, side):
    Rectangle.__init__(self, side, side)

  def set_side(self, side):
    self.height = side
    self.width = side

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.height = height
    self.width = height

  def __str__(self):
    return 'Square(side={})'.format(self.height)