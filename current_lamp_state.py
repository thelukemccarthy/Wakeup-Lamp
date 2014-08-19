import unittest
import os
from lamp_state import LampState

class CurrentLampState(unittest.TestCase):
  CURRENT_STATE_FILENAME = 'current_lamp_state.txt'

  def get(self):
    if(os.path.isfile(self.CURRENT_STATE_FILENAME)):
      file = open(self.CURRENT_STATE_FILENAME, "r")
      value = file.readline()
      file.close()
      return int(value)
    else:
      lampState = LampState()
      return lampState.OFF
      
  def set(self, newState):
    file = open(self.CURRENT_STATE_FILENAME, "w")
    file.write(str(newState))
    file.close()

  def test_givenTheLampStateIsUnknown_whenGetIsCalled_thenTheCurrentLampStateShouldBeOff(self):
    if(os.path.isfile(self.CURRENT_STATE_FILENAME)):
      os.remove(self.CURRENT_STATE_FILENAME)
    lampState = LampState()
    expected = lampState.OFF
    actual = self.get()
    self.assertEqual(expected, actual)
    
  def test_givenTheLampStateOfHigh_whenGetIsCalled_thenTheCurrentLampStateShouldBeHigh(self):
    lampState = LampState()
    expected = lampState.HIGH
    self.set(expected)
    actual = self.get()
    self.assertEqual(expected, actual)  
    
  def test_givenALampState_whenSetIsCalled_thenTheLampStateShouldBeSaved(self):
    lampState = LampState()
    expected = lampState.LOW
    self.set(expected)
    actual = self.get()
    self.assertEqual(expected, actual)
    
if __name__ == '__main__':
  unittest.main()
