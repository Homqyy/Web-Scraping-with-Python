from pythonScraping import *
from urllib.request import urlopen

def geoCoding(apiKey, address):
    url='https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address,apiKey)

    respond = urlopen(url).read().decode('utf-8')
    print(respond)

secretsData = getSecrets('google')

apiKey = secretsData['api_key']
address = '1+Science+Park+Boston+MA+02114'
geoCoding(apiKey, address)