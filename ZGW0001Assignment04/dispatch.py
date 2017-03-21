import unittest

def dispatch(values=None):

    #Validate parm
    if(values == None):
        print("Hello")
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values

    #Perform designated function
    if(values['op'] == 'adjust'):
        return values    #<-------------- replace this with your implementation
    elif(values['op'] == 'predict'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values


# Test Cases

class DispatchTest(unittest.TestCase):
    def test100_010_ShouldRaiseExceptionNoParameters(self):
        expected_string = "error: parameter is missing"
        with self.assertRaises(ValueError) as context:
            dispatch()
        self.assertAlmostEquals(expected_string, context.exception.args[0][0:len(expected_string)])

# dispatch()
