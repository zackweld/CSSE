import math

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
            height = float(values['height'])
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
        else:
            # Check for invalid pressure inputs
            pressure = int(values['pressure'])
            if (pressure < 100 or pressure > 1100):
                values['error'] = 'pressure is invalid'
                return values

        # If horizon is missing default to natural
        if (not('horizon' in values)):
            horizon = 'natural'
        else:
            horizon = values['horizon']
            if (not(horizon == 'artificial' or horizon == 'natural')):
                values['error'] = 'horizon is invalid'
                return values


        # Check to see if altitude is already in dictionary
        if ('altitude' in values):
            values['error'] = 'altitude is in input'
            return values

        # Calculation
        dip = 0
        if (horizon == 'natural'):
            dip = (-0.97 * math.sqrt(height)) / 60

        obsDegrees = float(degrees) + (minutes / 60)

        refraction = (-0.00452*pressure) / (273+convert_to_celsius(temp)) / \
                     math.tan(obsDegrees)

        altitude = obsDegrees + dip + refraction

        altDegrees = str(altitude)[0:str(altitude).find('.')]

        altitude = (altitude - int(altDegrees)) * 60

        altMinutes = str(altitude)[0:str(altitude).find('.')]

        fullAltitude = altDegrees + altMinutes

        values['altitude'] = fullAltitude


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


def convert_to_celsius(temp):
    cels = (temp - 32) * (5/9)
    return cels
