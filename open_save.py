from urllib.request import urlopen , urlretrieve
from bs4 import BeautifulSoup
import os

def open_html(someadress):
    try:
        Htmlcode = urlopen(someadress).read()
    except:
        print('Url do not exists')
        exit()
    return Htmlcode

'''def make_file(somesoup):
    file_name = 'site.html'
    if os.path.exists(file_name):
        os.remove(file_name)
    f = open(file_name, 'x', encoding="utf-8")
    a = somesoup.prettify()
    f.write(a)
    f.close()'''

def make_file(someadress):
    urlretrieve(someadress,'site.html')
