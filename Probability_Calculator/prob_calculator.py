import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **colors):
    contents = []
    for i,j in colors.items():
      for k in range(j):
        contents.append(i)
    self.contents = contents

  def draw(self, num_balls_drawn):
    if num_balls_drawn >= len(self.contents):
      return self.contents
    else:
      l=[]
      for i in range(num_balls_drawn):
        selected_color = random.choice(self.contents)
        l.append(selected_color)
        self.contents.remove(selected_color)
      return l


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected_balls_list = []
  for i,j in expected_balls.items():
    for k in range(j):
      expected_balls_list.append(i)
  
  m = 0
  for i in range(num_experiments):
    draw_list = copy.deepcopy(hat).draw(num_balls_drawn)
    test = True
    for i in set(expected_balls_list):
      if expected_balls_list.count(i) > draw_list.count(i):
        test = False
        break
    if test:
      m+=1
        
  return m/num_experiments
