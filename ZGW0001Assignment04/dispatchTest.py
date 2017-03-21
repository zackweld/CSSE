import unittest
from \ZGW0001Assignment04 import dispatch

class DispatchTest(unittest.TestCase):

    # Validating the input for dispatch
    # Must be a dictionary of one or more key-value pairs
    def test100_010_DispatchNoParameter(self):
        expected_result = {}
        self.assertDictEqual(expected_result, dispatch.dispatch())
    #
    # def test100_020_DispatchNotADictionary(self):
    #     expected_result = {'error': 'parameter is not a dictionary'}
    #     self.assertDictEqual(expected_result, dispatch.dispatch("hello"))
    #
    #
    # def test100_030_DispatchNoOpSpecified(self):
    #     expected_result = {'temperature': '72', 'error': 'no op is specified'}
    #     self.assertEquals(expected_result, dispatch.dispatch({'temperature': '72'}))
    #
    #
    # def test100_040_DispatchOpIsNotALegalOperation(self):
    #     expected_result = {'temperature': '72', 'error': 'op is not a legal operation'}
    #     self.assertDictEqual(expected_result, dispatch.dispatch({'temperature': '72', 'op': 'Wrong'}))
    #
    #
    # def test100_050_DispatchExecutesAdjust(self):
    #     passed = 0
    #     values = {'temperature': '72', 'op': 'adjust'}
    #     #Validate parm
    #     if(values == None):
    #         return {'error': 'parameter is missing'}
    #     if(not(isinstance(values,dict))):
    #         return {'error': 'parameter is not a dictionary'}
    #     if (not('op' in values)):
    #         values['error'] = 'no op is specified'
    #         return values
    #
    #     #Perform designated function
    #     if(values['op'] == 'adjust'):
    #         passed = 1
    #         return values    #<-------------- replace this with your implementation
    #     elif(values['op'] == 'predict'):
    #         return values    #This calculation is stubbed out
    #     elif(values['op'] == 'correct'):
    #         return values    #This calculation is stubbed out
    #     elif(values['op'] == 'locate'):
    #         return values    #This calculation is stubbed out
    #     else:
    #         del values['op']
    #         values['error'] = 'op is not a legal operation'
    #         return values
    #
    #     self.assertEquals(passed, 1)
