class Person:
  def __init__(self, name=str):
    self.name = name
    self.stoned = False

  def is_stoned(self):
    return self.stoned