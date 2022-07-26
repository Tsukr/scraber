import open_save
from bs4 import BeautifulSoup
adress = input('Enter url: ')
html = open_save.open_html(adress)

open_save.make_file(adress)