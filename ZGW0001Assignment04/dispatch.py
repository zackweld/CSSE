import unittest

def dispatch(values=None):

    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op is specified'
        return values

    #Perform designated function
    if(values['op'] == 'adjust'):
        if (not('observation' in values)):
            return {'error': 'mandatory information missing'}

        # Check observation correct form
        obs = values['observation']
        if ('d' not in obs):
            values['error'] = 'observation is invalid'
            return values

        # Confirm observation values within range
        degrees = int(obs[0:obs.find('d')])
        minutes = float(obs[obs.find('d')+1:len(obs)])
        if (degrees < 0 or degrees > 90 or minutes < 0 or minutes > 60):
            values['error'] = 'observation is invalid'
        if (degrees == 0 and minutes < 0.1):
            values['error'] = 'observation is invalid'

        # If height is missing default to 0
        if (not('height' in values)):
            height = 0
        # If height is less than zero send error
        else:
            height = int(values['height'])
            if (height < 0):
                values['error'] = 'height is invalid'
                return values

        # If temp is missing default to 72
        if (not('temperature' in values)):
            temp = 72
        else:
            # If pressure is invalide return error
            temp = int(values['temperature'])
            if (temp < -20 or temp > 120):
                values['error'] = 'temperature is invalid'
                return values

        # If pressure is missing default to 1010
        if (not('pressure' in values)):
            pressure = 1010



        return values    #<-------------- replace this with your implementation
    elif(values['op'] == 'predict'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        del values['op']
        values['error'] = 'op is not a legal operation'
        return values


