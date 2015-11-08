__author__ = 'marti'

import random
from urllib3 import request


def download_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    request.urlretrieve(url, full_name)

download_image("http://www.hwsw.hu/kepek/hirek/2014/12/upc_ondemand.jpg")

