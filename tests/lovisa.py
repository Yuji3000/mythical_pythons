class Lovisa:
  def __init__(self, title=str, characteristics="brilliant"):
    self.title = title
    self.characteristics = characteristics

  def is_brilliant(self):
    return "brilliant" in self.characteristics

  def is_kind(self):
    return "kind" in self.characteristics
    
  def say(self, phrase):
    return (f'**;* {phrase} **;*')