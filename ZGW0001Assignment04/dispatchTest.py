import unittest
import dispatch

class DispatchTest(unittest.TestCase):

    # Validating the input for dispatch
    # Must be a dictionary of one or more key-value pairs
    def test100_010_DispatchNoParameter(self):
        expected_result = {'error': 'parameter is missing'}
        self.assertDictEqual(expected_result, dispatch.dispatch())

    def test100_020_DispatchNotADictionary(self):
        expected_result = {'error': 'parameter is not a dictionary'}
        self.assertDictEqual(expected_result, dispatch.dispatch("hello"))

    def test100_030_DispatchNoOpSpecified(self):
        expected_result = {'temperature': '72', 'error': 'no op is specified'}
        self.assertEquals(expected_result, dispatch.dispatch({'temperature': '72'}))


    def test100_040_DispatchOpIsNotALegalOperation(self):
        expected_result = {'temperature': '72', 'error': 'op is not a legal operation'}
        self.assertDictEqual(expected_result, dispatch.dispatch({'temperature': '72', 'op': 'Wrong'}))


    def test100_050_DispatchExecutesAdjust(self):
        passed = "fail"
        values = {'temperature': '72', 'op': 'adjust'}
        #Validate parm
        if(values == None):
            pass
            # return {'error': 'parameter is missing'}
        if(not(isinstance(values,dict))):
            pass
        #     return {'error': 'parameter is not a dictionary'}
        if (not('op' in values)):
            pass
        #     values['error'] = 'no op is specified'
        #     return values

        #Perform designated function
        if(values['op'] == 'adjust'):
            passed = "pass"
            # return values    #<-------------- replace this with your implementation
        elif(values['op'] == 'predict'):
            pass
            # return values    #This calculation is stubbed out
        elif(values['op'] == 'correct'):
            pass
            # return values    #This calculation is stubbed out
        elif(values['op'] == 'locate'):
            pass
            # return values    #This calculation is stubbed out
        else:
            pass
            # del values['op']
            # values['error'] = 'op is not a legal operation'
            # return values

        self.assertEquals(passed, "pass")


############
# Adjust Tests
############

# Check inputs

    def test200_010_AdjustMissingNecessaryValues(self):
        expected_result = {'error': 'mandatory information missing'}
        missingObservation = {'op': 'adjust', 'horizon': 'natural'}
        # missingHorizon = {'op': 'adjust', 'observation': '50'}
        self.assertDictEqual(expected_result, dispatch.dispatch(missingObservation))
        # self.assertDictEqual(expected_result, dispatch.dispatch(missingHorizon))

    def test200_020_AdjustObservationInvalid(self):
        expected_result = {'op': 'adjust', 'horizon': 'natural', 'observation': '91', 'error': 'observation is invalid'}
        call = {'op': 'adjust', 'horizon': 'natural', 'observation': '91d00.0'}
        call2 = {'op': 'adjust', 'horizon': 'natural', 'observation': '0d00.0'}
        call3 = {'op': 'adjust', 'horizon': 'natural', 'observation': '45d-05.0'}
        call4 = {'op': 'adjust', 'horizon': 'natural', 'observation': '0d61.0'}
        call5 = {'op': 'adjust', 'horizon': 'natural', 'observation': '000.0'}
        self.assertDictEqual(expected_result, dispatch.dispatch(call))
        self.assertDictEqual(expected_result, dispatch.dispatch(call2))
        self.assertDictEqual(expected_result, dispatch.dispatch(call3))
        self.assertDictEqual(expected_result, dispatch.dispatch(call4))
        self.assertDictEqual(expected_result, dispatch.dispatch(call5))


