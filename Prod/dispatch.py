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
        star_SHA = desired_star[1]
        star_declination = desired_star[2]

        # Determine angular difference for each year
        angularDifference = (year - 2001) * minutes_to_degrees('-0d14.31667')

        # Take into account leap years
        numberOfLeapYears = 0
        for i in range(2001, year):
            if (i % 4) == 0:
                numberOfLeapYears += 1

        totalProgression = numberOfLeapYears * minutes_to_degrees('0d59.0')

        # Calculate Prime meridian rotation
        primeMeridianRotation = minutes_to_degrees('100d4.8') + angularDifference + totalProgression
        primeMeridianRotation = degrees_to_minutes(primeMeridianRotation)
        # Calculate angle of earth's rotation
        total_seconds = int(timedelta(days=day, hours=hour, minutes=minute, seconds=second).total_seconds())
        rotation = total_seconds / 86164.1 * 360
        rotation = degrees_to_minutes(rotation)
        # Calculate Aries total
        ariesTotal = minutes_to_degrees(primeMeridianRotation) + minutes_to_degrees(rotation)
        ariesTotal = degrees_to_minutes(ariesTotal)

        # Calculate GHA star
        gha_star = minutes_to_degrees(ariesTotal) + minutes_to_degrees(star_SHA)
        gha_star = degrees_to_minutes(gha_star)

        values['long'] = gha_star
        values['lat'] = star_declination


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
    if not(deg_string[deg_string.find('.')+2: deg_string.find('.')+3] == ''):
        if (int(deg_string[deg_string.find('.')+2: deg_string.find('.')+3]) > 4):
            degrees = degrees + 0.1

    deg_minutes = str(degrees)[0:str(degrees).find('.')+2]
    while deg > 360:
        deg = deg - 360
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
    if not(d[0:4].isdigit()) or not(d[5:7].isdigit()) or not(d[8:10].isdigit()):
        return False
    if not(d[4:5] == '-') or not(d[7:8] == '-'):
        return False
    year = int(d[0:4])
    month = int(d[5:7])
    day = int(d[8:10])

    if year < 2001 or month < 1 or month > 12:
        return False

    if month == 01 or month == 03 or month == 05 or month == 07 or month == 8 or month == 10 or month == 12:
        if day > 31:
            return False
    elif month == 02:
        if (year % 4) == 0:
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    else:
        if day > 30:
            return False


    return True

def check_time(t):
    if not(len(t) == 8):
        return False
    if not(t[0:2].isdigit()) or not(t[3:5].isdigit()) or not(t[6:8].isdigit()):
        return False
    if not(t[2:3] == ':') or not(t[5:6] == ':'):
        return False
    hour = int(t[0:2])
    minutes = int(t[3:5])
    seconds = int(t[6:8])

    if hour < 0 or hour > 23 or minutes < 0 or minutes > 59 or seconds < 0 or seconds > 59:
        return False


    return True
