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
        desired_star = read_stars_file(values['body'])

        if (desired_star == '-1'):
            values['error'] = 'Star not in catalog'
            return values

        if not('date' in values):
            date = '2001-01-01'
        else:
            date = values['date']
            if not(check_date(date)):
                values['error'] = 'Invalid date'
                return values

        if not('time' in values):
            time = '00:00:00'
        else:
            time = values['time']
            if not(check_time(time)):
                values['error'] = 'Invalid time'
                return values

        # Establish year, month, date, hour, minute, second
        year = int(date[0:3])
        month = int(date[5:6])
        day = int(date[8:9])
        hour = int(time[0:1])
        minute = int(time[3:4])
        second = int(time[6:7])

        # Determine angular difference for each year
        angularDifference = (year - 2001) * minutes_to_degrees('-0d14.31667')

        # Take into account leap years
        # numberOfLeapYears = 0
        # for i in range(2001, year):
        #     if (i % 4) == 0:
        #         numberOfLeapYears++
        #
        # totalProgression = numberOfLeapYears * minutes_to_degrees('0d59.0')





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
    deg = float(minutes[0:minutes.find('d')])
    m = float(minutes[minutes.find('d')+1: len(minutes)])
    m = m / 60
    deg = deg + m
    if minutes[0] == '-':
        deg = deg * (-1)
    return deg

def degrees_to_minutes(degrees):
    deg = int(degrees)
    degrees = abs(degrees - deg) * 60
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

def check_date(d):
    if not(len(d) == 10):
        return False
    if not(d[0:3].isdigit()) or not(d[5:6].isdigit()) or not(d[8:9].isdigit()):
        return False
    if not(d[4] == '-') or not(d[7] == '-'):
        return False
    year = int(d[0:3])
    month = int(d[5:6])
    day = int(d[8:9])
    if year < 2001 or not(month is date.month) or not(day is date.day(month, year)):
        return False

    return True

def check_time(t):
    if not(len(t) == 8):
        return False
    if not(t[0:1].isdigit()) or not(t[3:4].isdigit()) or not(t[6:7].isdigit()):
        return False
    if not(t[2] == ':') or not(t[5] == ':'):
        return False
    hour = int(t[0:1])
    minutes = int(t[3:4])
    seconds = int(t[6:7])
    if not(hour is time.hour) or not(minutes is time.minute) or not(seconds is time.second):
        return False

    return True
