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

        obs = values['observation']
        if ('d' not in obs):
            values['error'] = 'observation is invalid'
            return values
        # degrees = int(obs.substring(0, obs.indexOf('d')))
        degrees = int(obs[0:obs.find('d')])
        # minutes = float(obs.substring(obs.indexOf('d')+1, obs.length))
        minutes = float(obs[obs.find('d')+1:len(obs)])
        if (degrees < 0 or degrees > 90 or minutes < 0 or minutes > 60):
            values['error'] = 'observation is invalid'
        if (degrees == 0 and minutes < 0.1):
            values['error'] = 'observation is invalid'


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


