import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "https://www.homqyy.cn"

def getAbsoluteURL(baseUrl, source):
    if source.startswith('https://'):
        url = source
    elif source.startswith('www.'):
        url = source
    else: # Only URI
        url = baseUrl + "/" + source
    
    if baseUrl not in url:
        return None

    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace(baseUrl, '')
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path

html = urlopen('https://www.homqyy.cn')
bsObj = BeautifulSoup(html, 'html.parser')
downloadList = bsObj.find_all(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        fileUrlQuoted = quote(fileUrl, safe='/:')
        print('fileUrl: {} => {}'.format(fileUrl, fileUrlQuoted))
        urlretrieve(fileUrlQuoted, getDownloadPath(baseUrl, fileUrlQuoted, downloadDirectory))