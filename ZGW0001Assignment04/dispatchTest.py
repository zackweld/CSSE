import unittest
import dispatch as d
import math

class dispatchTest(unittest.TestCase):
    def test100_010_ShouldRaiseExceptionNoParameters(self):
        expected_string = "\'error\': \'parameter is missing\'"
        print("Hello")
        with self.assertRaises(ValueError) as context:
            d.dispatch()
        self.assertAlmostEquals(expected_string, context.exception.args[0][0:len(expected_string)])




dispatchTest.test100_010_ShouldRaiseExceptionNoParameters()

