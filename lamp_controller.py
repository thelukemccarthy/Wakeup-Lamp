import unittest
from current_lamp_state import CurrentLampState
from lamp_state import LampState

class LampController(unittest.TestCase):
  currentLampState = CurrentLampState()

  def get_lamp_state(self):
    return self.currentLampState.get()

  def set_lamp_state(self, new_lamp_state):
    self.currentLampState.set(new_lamp_state)
    
if __name__ == '__main__':
  unittest.main()
