import json

'''
Get secrets
'''
def getSecrets(secretName):
    validNames = ['twitter', 'google', 'ipstack']

    if secretName not in validNames:
        raise ValueError('Invalid secret name')

    with open('secrets.json', 'r') as f:
        return json.load(f)[secretName]