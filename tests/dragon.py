class Dragon:
  def __init__(self, name = str, color = str, rider = str ):
    self.name = name
    self.color = color
    self.rider = rider
    self.times_eat = 0
    
  def is_hungry(self):
    if self.times_eat < 3:
      return True
    else:
      return False
  
  def eat(self):
    self.times_eat += 1