import unittest
from lamp_state import LampState

class LampStateMachine(unittest.TestCase):
  NO_TOUCH_DETECTED = 0
  TOUCH_DETECTED = 1

  __lampState = LampState()

  __lamp_state_machine = \
    { 
      __lampState.OFF: [__lampState.OFF, __lampState.LOW], 
      __lampState.LOW: [__lampState.LOW, __lampState.MEDIUM], 
      __lampState.MEDIUM: [__lampState.MEDIUM, __lampState.HIGH], 
      __lampState.HIGH: [__lampState.HIGH, __lampState.OFF] 
    } 

  def get_next_state(self, current_state, input_value):
    next_states = self.__lamp_state_machine[current_state]
    return next_states[input_value]

  def test_givenACurrentStateOfOffAndNoTouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeOff(self):
    expected = self.__lampState.OFF
    actual = self.get_next_state(self.__lampState.OFF, self.NO_TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfOffAndATouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeLow(self):
    expected = self.__lampState.LOW
    actual = self.get_next_state(self.__lampState.OFF, self.TOUCH_DETECTED) 
    self.assertEqual(expected, actual)


  def test_givenACurrentStateOfLowAndNoTouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeLow(self):
    expected = self.__lampState.LOW
    actual = self.get_next_state(self.__lampState.LOW, self.NO_TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfLowAndATouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeMedium(self):
    expected = self.__lampState.MEDIUM
    actual = self.get_next_state(self.__lampState.LOW, self.TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfMediumAndNoTouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeMedium(self):
    expected = self.__lampState.MEDIUM
    actual = self.get_next_state(self.__lampState.MEDIUM, self.NO_TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfMediumAndATouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeHigh(self):
    expected = self.__lampState.HIGH
    actual = self.get_next_state(self.__lampState.MEDIUM, self.TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfHighAndNoTouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeHigh(self):
    expected = self.__lampState.HIGH
    actual = self.get_next_state(self.__lampState.HIGH, self.NO_TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfHighAndATouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeOff(self):
    expected = self.__lampState.OFF
    actual = self.get_next_state(self.__lampState.HIGH, self.TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

if __name__ == '__main__':
  unittest.main()
