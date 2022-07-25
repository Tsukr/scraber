from urllib.request import urlopen

def open_html():
    adress = input('Enter url: ')
    try:
        Htmlcode = urlopen(adress).read()
    except:
        print('Url do not exists')
        exit()
    return Htmlcode

open_html()

#some change