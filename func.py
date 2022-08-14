from urllib.request import urlopen , urlretrieve


def open_html(someadress):
    try:
        Htmlcode = urlopen(someadress).read()
    except:
        print('Url do not exists')
        exit()
    return Htmlcode

def save_html(someadress):
    try:
        urlretrieve(someadress,'site.html')
        print('File saved as html')
    except:
        print('Save ERROR')