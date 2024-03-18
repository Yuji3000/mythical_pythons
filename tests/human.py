class Human:
  def __init__(self, name="Jane"):
    self.name = name
    self.encounter_counter = 0
    self.ogre_saw = 0

  def notices_ogre(self):
    if self.ogre_saw and self.ogre_saw % 3 == 0:
      return True
    else:
      return False 