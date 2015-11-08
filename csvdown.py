__author__ = 'marti'

from urllib3 import request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=11&e=10&f=2014&g=d&a=2&b=27&c=2014&ignore=.csv'

def download_csv(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str =str(csv)
    lines =csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()

download_csv(goog_url)