import math
import unittest
import dispatch
import datetime
from datetime import timedelta, date, time


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
        expected_result = {'op': 'adjust', 'horizon': 'natural', 'observation': '91d00.0', 'error': 'observation is invalid'}
        expected_result2 = {'op': 'adjust', 'horizon': 'natural', 'observation': '-1d05.0', 'error': 'observation is invalid'}
        expected_result3 = {'op': 'adjust', 'horizon': 'natural', 'observation': '45d-05.0', 'error': 'observation is invalid'}
        expected_result4 = {'op': 'adjust', 'horizon': 'natural', 'observation': '5d61.0', 'error': 'observation is invalid'}
        expected_result5 = {'op': 'adjust', 'horizon': 'natural', 'observation': '000.0', 'error': 'observation is invalid'}
        expected_result6 = {'op': 'adjust', 'horizon': 'natural', 'observation': '0d00.0', 'error': 'observation is invalid'}
        call = {'op': 'adjust', 'horizon': 'natural', 'observation': '91d00.0'}
        call2 = {'op': 'adjust', 'horizon': 'natural', 'observation': '-1d05.0'}
        call3 = {'op': 'adjust', 'horizon': 'natural', 'observation': '45d-05.0'}
        call4 = {'op': 'adjust', 'horizon': 'natural', 'observation': '5d61.0'}
        call5 = {'op': 'adjust', 'horizon': 'natural', 'observation': '000.0'}
        call6 = {'op': 'adjust', 'horizon': 'natural', 'observation': '0d00.0'}
        self.assertDictEqual(expected_result, dispatch.dispatch(call))
        self.assertDictEqual(expected_result2, dispatch.dispatch(call2))
        self.assertDictEqual(expected_result3, dispatch.dispatch(call3))
        self.assertDictEqual(expected_result4, dispatch.dispatch(call4))
        self.assertDictEqual(expected_result5, dispatch.dispatch(call5))
        self.assertDictEqual(expected_result6, dispatch.dispatch(call6))


    def test200_030_AdjustHeightLeftOutSetToZero(self):
        call = {'op': 'adjust', 'observation': '45d30.0'}
        height = -1
        if (not('height' in call)):
            height = 0
        self.assertEquals(height, 0)

    def test200_040_AdjustHeightIsInvalid(self):
        expected_result = {'op': 'adjust', 'observation': '45d30.0', 'height': '-1', 'error': 'height is invalid'}
        call = {'op': 'adjust', 'observation': '45d30.0', 'height': '-1'}
        self.assertDictEqual(expected_result, dispatch.dispatch(call))

    def test200_050_AdjustTempIsLeftOut(self):
        call = {'op': 'adjust', 'observation': '45d30.0'}
        temp = 0
        if (not('temperature' in call)):
            temp = 72
        self.assertEquals(temp, 72)

    def test200_060_AdjustTempIsInvalid(self):
        expected_result = {'op': 'adjust', 'observation': '45d30.0', 'temperature': '-21', 'error': 'temperature is invalid'}
        expected_result2 = {'op': 'adjust', 'observation': '45d30.0', 'temperature': '121', 'error': 'temperature is invalid'}
        call = {'op': 'adjust', 'observation': '45d30.0', 'temperature': '-21'}
        call2 = {'op': 'adjust', 'observation': '45d30.0', 'temperature': '121'}
        self.assertDictEqual(expected_result, dispatch.dispatch(call))
        self.assertDictEqual(expected_result2, dispatch.dispatch(call2))

    def test200_070_AdjustPressureIsLeftOut(self):
        call = {'op': 'adjust', 'observation': '45d30.0'}
        pressure = 0
        if (not('pressure' in call)):
            pressure = 1010
        self.assertEquals(pressure, 1010)

    def test200_080_AdjustPressureIsInvalid(self):
        call = {'op': 'adjust', 'observation': '45d30.0', 'pressure': '99'}
        call2 = {'op': 'adjust', 'observation': '45d30.0', 'pressure': '1101'}
        expected_result = {'op': 'adjust', 'observation': '45d30.0', 'pressure': '99', 'error': 'pressure is invalid'}
        expected_result2 = {'op': 'adjust', 'observation': '45d30.0', 'pressure': '1101', 'error': 'pressure is invalid'}
        self.assertDictEqual(expected_result, dispatch.dispatch(call))
        self.assertDictEqual(expected_result2, dispatch.dispatch(call2))

    def test200_090AdjustHorizonIsLeftOut(self):
        call = {'op': 'adjust', 'observation': '45d30.0'}
        horizon = 'random'
        if (not('horizon' in call)):
            horizon = 'natural'
        self.assertEquals(horizon, 'natural')

    def test200_100_AdjustHorizonIsInvalid(self):
        call = {'op': 'adjust', 'observation': '45d30.0', 'horizon': 'random'}
        expected_result = {'op': 'adjust', 'observation': '45d30.0', 'horizon': 'random', 'error': 'horizon is invalid'}
        self.assertDictEqual(expected_result, dispatch.dispatch(call))

    def test200_110_AdjustAltitudeAlreadyInDict(self):
        call = {'op': 'adjust', 'observation': '45d30.0', 'altitude': '50'}
        expected_result = {'op': 'adjust', 'observation': '45d30.0', 'altitude': '50', 'error': 'altitude is in input'}
        self.assertDictEqual(expected_result, dispatch.dispatch(call))


#########################
# Check Calculations
#########################

    def test300_010_AdjustValidCalculation(self):
        call = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000',
                'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        expected_result = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000',
                'horizon': 'artificial', 'op': 'adjust', 'temperature': '85',
                           'altitude': '29d59.9'}
        self.assertDictEqual(expected_result, dispatch.dispatch(call))

        call2 = {'observation': '45d15.2', 'height': '6', 'pressure': '1010',
                'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        expected_result2 = {'observation': '45d15.2', 'height': '6', 'pressure': '1010',
                'horizon': 'natural', 'op': 'adjust', 'temperature': '71',
                            'altitude': '45d11.9'}
        self.assertDictEqual(expected_result2, dispatch.dispatch(call2))

        call3 = {'observation': '42d0.0', 'op': 'adjust'}
        expected_result3 = {'observation': '42d0.0', 'op': 'adjust', 'altitude': '41d59.0'}
        self.assertDictEqual(expected_result3, dispatch.dispatch(call3))

        call4 = {'observation': '42d0.0', 'op': 'adjust', 'extraKey': 'ignore'}
        expected_result4 = {'observation': '42d0.0', 'op': 'adjust', 'extraKey': 'ignore',
                            'altitude': '41d59.0'}

    def test300_020_ConvertToCelsius(self):
        expected_result = 29.4444
        self.assertAlmostEqual(expected_result, dispatch.convert_to_celsius(85), 2)

    def test300_030_AdjustCalculateDip(self):
        height = float(19)
        expected_result = -0.0704689
        dip = (-0.97) * math.sqrt(height) / 60
        self.assertAlmostEqual(expected_result, dip, 4)

    def test300_040_AdjustCalculateMinToDegrees(self):
        observation = '30d1.5'
        obs_degrees = float(observation[0:observation.find('d')])
        obs_minutes = float(observation[observation.find('d')+1: len(observation)])
        obs = obs_degrees + (obs_minutes / 60)
        expected_result = 30.025
        self.assertAlmostEqual(expected_result, obs, 5)

    def test300_050_AdjustCalculatRefraction(self):
        expected_result = -0.0258595
        pressure = 1000
        cels = 29.4444
        observation = 30.025
        refraction = (-0.00452) * pressure / (273+cels) / (math.tan(observation * math.pi / 180))

        self.assertAlmostEqual(expected_result, refraction, 4)

#######################
#   Test Predict Op
#######################
    def test400_010_PredictMissingBody(self):
        expected_result = {'op': 'predict', 'error': 'Body is missing'}
        call = {'op': 'predict'}
        self.assertDictEqual(expected_result, dispatch.dispatch(call))

    def test400_020_CheckReadFile(self):
        current_star_info = dispatch.read_stars_file('Hamal')
        self.assertEquals(current_star_info[0], 'Hamal')
        self.assertEquals(current_star_info[1], '327d58.7')
        self.assertEquals(current_star_info[2], '23d32.3')
        invalid_star = dispatch.read_stars_file('Name')
        self.assertEquals('-1', invalid_star)

    def test400_030_PredictBodyNotValid(self):
        expected_result = {'op': 'predict', 'body': 'unknown', 'error': 'Star not in catalog'}
        call = {'op': 'predict', 'body': 'unknown'}
        self.assertDictEqual(expected_result, dispatch.dispatch(call))

    def test400_040_PredictMissingDate(self):
        call = {'op': 'predict', 'body': 'Hamal'}
        date = "random"
        if not('date' in  call):
            date = '2001-01-01'
        self.assertEquals('2001-01-01', date)

    def test400_050_PredictInvalidDate(self):
        call1 = {'op': 'predict', 'body': 'Hamal', 'date': '20030-0302-1'}
        expected_result1 = {'op': 'predict', 'body': 'Hamal', 'date': '20030-0302-1', 'error': 'Invalid date'}
        call2 = {'op': 'predict', 'body': 'Hamal', 'date': '2000-05-23'}
        expected_result2 = {'op': 'predict', 'body': 'Hamal', 'date': '2000-05-23', 'error': 'Invalid date'}
        call3 = {'op': 'predict', 'body': 'Hamal', 'date': '2002-13-23'}
        expected_result3 = {'op': 'predict', 'body': 'Hamal', 'date': '2002-13-23', 'error': 'Invalid date'}
        call4 = {'op': 'predict', 'body': 'Hamal', 'date': '2002-05-33'}
        expected_result4 = {'op': 'predict', 'body': 'Hamal', 'date': '2002-05-33', 'error': 'Invalid date'}
        self.assertDictEqual(expected_result1, dispatch.dispatch(call1))
        self.assertDictEqual(expected_result2, dispatch.dispatch(call2))
        self.assertDictEqual(expected_result3, dispatch.dispatch(call3))
        self.assertDictEqual(expected_result4, dispatch.dispatch(call4))

    def test400_060_PredictMissingTime(self):
        call = {'op': 'predict', 'body': 'Hamal'}
        time = 'random'
        if not(time in call):
            time = '00:00:00'
        self.assertEquals('00:00:00', time)

    def test400_070_PredictInvalidTime(self):
        call1 = {'op': 'predict', 'body': 'Hamal', 'time': '0h0e030:'}
        expected_result1 = {'op': 'predict', 'body': 'Hamal', 'time': '0h0e030:', 'error': 'Invalid time'}
        call2 = {'op': 'predict', 'body': 'Hamal', 'time': '25:30:30'}
        expected_result2 = {'op': 'predict', 'body': 'Hamal', 'time': '25:30:30', 'error': 'Invalid time'}
        call3 = {'op': 'predict', 'body': 'Hamal', 'time': '02:50:30'}
        expected_result3 = {'op': 'predict', 'body': 'Hamal', 'time': '02:50:30', 'error': 'Invalid time'}
        call4 = {'op': 'predict', 'body': 'Hamal', 'time': '02:40:50'}
        expected_result4 = {'op': 'predict', 'body': 'Hamal', 'time': '02:40:50', 'error': 'Invalid time'}
        self.assertDictEqual(expected_result1, dispatch.dispatch(call1))
        self.assertDictEqual(expected_result2, dispatch.dispatch(call2))
        self.assertDictEqual(expected_result3, dispatch.dispatch(call3))
        self.assertDictEqual(expected_result4, dispatch.dispatch(call4))

    def test400_080_PredictAngularDifference(self):
        year = 2016
        angularDifference = (2016 - 2001) * dispatch.minutes_to_degrees('-0d14.31667')
        angularDifference = dispatch.degrees_to_minutes(angularDifference)
        self.assertEquals(angularDifference, '-3d34.8')

    def test400_090_PredictAccountForLeapYears(self):
        year = 2016
        numberOfLeapYears = 0
        for i in range(2001, year):
            if (i % 4) == 0:
                numberOfLeapYears += 1

        totalProgression = numberOfLeapYears * dispatch.minutes_to_degrees('0d59.0')
        totalProgression = dispatch.degrees_to_minutes(totalProgression)
        self.assertEquals(totalProgression, '2d57.0')

    def test400_100_PredictPrimeMeridianRotation(self):
        year = 2016
        angularDifference = (2016 - 2001) * dispatch.minutes_to_degrees('-0d14.31667')
        numberOfLeapYears = 0
        for i in range(2001, year):
            if (i % 4) == 0:
                numberOfLeapYears += 1

        totalProgression = numberOfLeapYears * dispatch.minutes_to_degrees('0d59.0')

        rotation = dispatch.minutes_to_degrees('100d42.6') + angularDifference + totalProgression
        rotation = dispatch.degrees_to_minutes(rotation)
        self.assertEquals(rotation, '100d4.8')

    def test400_110_PredictAngleEarthsRotation(self):
        total_seconds = int(timedelta(days=16, hours=03, minutes=15, seconds=42).total_seconds())
        self.assertEquals(total_seconds, 1394142)
        # rotation = total_seconds / 86164.1 * 360
        # rotation = degrees_to_minutes(rotation)
        rotation = 0
        self.assertEquals(rotation, '164d54.5')
