import unittest


class LampStateMachine(unittest.TestCase):
  OFF = 0
  LOW = 33
  MEDIUM = 66
  HIGH = 100

  NO_TOUCH_DETECTED = 0
  TOUCH_DETECTED = 1

  __lamp_state_machine = \
    { 
      OFF: [OFF, LOW], 
      LOW: [LOW, MEDIUM], 
      MEDIUM: [MEDIUM, HIGH], 
      HIGH: [HIGH, OFF] 
    } 

  def get_next_state(self, current_state, input_value):
    next_states = self.__lamp_state_machine[current_state]
    return next_states[input_value]

  def test_givenACurrentStateOfOffAndNoTouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeOff(self):
    expected = self.OFF
    actual = self.get_next_state(self.OFF, self.NO_TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfOffAndATouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeLow(self):
    expected = self.LOW
    actual = self.get_next_state(self.OFF, self.TOUCH_DETECTED) 
    self.assertEqual(expected, actual)


  def test_givenACurrentStateOfLowAndNoTouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeLow(self):
    expected = self.LOW
    actual = self.get_next_state(self.LOW, self.NO_TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfLowAndATouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeMedium(self):
    expected = self.MEDIUM
    actual = self.get_next_state(self.LOW, self.TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfMediumAndNoTouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeMedium(self):
    expected = self.MEDIUM
    actual = self.get_next_state(self.MEDIUM, self.NO_TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfMediumAndATouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeHigh(self):
    expected = self.HIGH
    actual = self.get_next_state(self.MEDIUM, self.TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfHighAndNoTouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeHigh(self):
    expected = self.HIGH
    actual = self.get_next_state(self.HIGH, self.NO_TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

  def test_givenACurrentStateOfHighAndATouchDetected_whenGetNextStateIsCalled_thenTheNextLampStateShouldBeOff(self):
    expected = self.OFF
    actual = self.get_next_state(self.HIGH, self.TOUCH_DETECTED) 
    self.assertEqual(expected, actual)

if __name__ == '__main__':
  unittest.main()
