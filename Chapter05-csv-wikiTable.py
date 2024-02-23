import csv
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsObj = BeautifulSoup(html, 'html.parser')

# Get the first table
table = bsObj.findAll('table', {'class':'wikitable'})[0]
rows = table.findAll('tr')

os.makedirs('saved-csv', exist_ok=True)

csvFile = open('saved-csv/comparison.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.find_all(['td', 'th']):
            text = cell.get_text(strip=True)
            print(text)
            csvRow.append(text)

        print(csvRow)
        writer.writerow(csvRow)
finally:
    csvFile.close()