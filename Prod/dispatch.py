import math
import datetime
from datetime import timedelta
from datetime import date
from datetime import time

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
        degrees = float(obs[0:obs.find('d')])
        minutes = float(obs[obs.find('d')+1:len(obs)])
        if (degrees < 0 or degrees > 90 or minutes < 0 or minutes > 60):
            values['error'] = 'observation is invalid'
            return values
        if (degrees == 0 and minutes < 0.1):
            values['error'] = 'observation is invalid'
            return values

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
            temp = float(values['temperature'])
            if (temp < -20 or temp > 120):
                values['error'] = 'temperature is invalid'
                return values

        # If pressure is missing default to 1010
        if (not('pressure' in values)):
            pressure = 1010
        else:
            # Check for invalid pressure inputs
            pressure = float(values['pressure'])
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

        if (horizon == 'natural'):
            dip = (-0.97 * math.sqrt(height)) / 60
        else:
            dip = 0

        observation = degrees + (minutes / 60)
        refraction = ((-0.00452)*pressure) / (273+convert_to_celsius(temp)) / math.tan(observation * math.pi / 180)
        alt = observation + dip + refraction

        altitude = degrees_to_minutes(alt)

        values['altitude'] = altitude



        return values    #<-------------- replace this with your implementation
    elif(values['op'] == 'predict'):
        if (not('body' in values)):
            values['error'] = 'Body is missing'
            return values

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
    cels = float(temp - 32) * 5 / 9
    return cels

def minutes_to_degrees(minutes):
    deg = str(minutes)[0:str(minutes).find('d')]
    minutes = minutes - int(minutes)
    deg = deg + (minutes * 60)
    return deg

def degrees_to_minutes(degrees):
    deg = int(degrees)
    degrees = (degrees - deg) * 60
    deg_string = str(degrees)
    if (int(deg_string[deg_string.find('.')+2: deg_string.find('.')+3]) > 4):
        degrees = degrees + 0.1

    deg_minutes = str(degrees)[0:str(degrees).find('.')+2]
    altitude = str(deg) + 'd' + deg_minutes
    return altitude

def read_stars_file(star):
    stars = open('stars', 'r')
    for line in stars:
        words = line.split()
        if (words[0] == star):
            return words

    return '-1'
