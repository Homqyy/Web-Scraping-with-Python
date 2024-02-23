from urllib.request import urlopen
from bs4 import BeautifulSoup
from pythonScraping import *
import datetime
import random
import re
import json

random.seed(datetime.datetime.now().timestamp())

def getCountry(ipAddress):
    secretsData = getSecrets('ipstack')
    apiKey = secretsData['api_key']

    try:
        response = urlopen('http://api.ipstack.com/{}?access_key={}'.format(
            ipAddress, apiKey)).read().decode('utf-8')
    except:
        return None

    responseJson = json.loads(response)
    return responseJson.get('country_code')

def getLinks(articleUrl):
    fullUrl = 'http://en.wikipedia.org{}'.format(articleUrl)
    print('Get links => {}'.format(fullUrl))
    html = urlopen(fullUrl)

    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj.find('div', {'id':'bodyContent'}).find_all('a', 
                                                     href=re.compile('^(/wiki/)((?!:).)*$'))

def getHistoryIPs(pageUrl):
    # edit history URL is of the form:
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'http://en.wikipedia.org/w/index.php?title={}&action=history'.format(pageUrl)
    print('history url is: {}'.format(historyUrl))

    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    # find only the links with class "mw-anonuserlink" which has IP addresses
    # instead of usernames
    ipAddresses = bsObj.find_all('a', {'class':'mw-userlink mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())

    return addressList

links = getLinks('/wiki/Python_(programming_language)')

while(len(links) > 0):
    for link in links:
        print('-'*20)
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            print("{} is from {}".format(historyIP, country))

    newLink = links[random.randint(0, len(links) - 1)].attrs['href']
    links = getLinks(newLink)
