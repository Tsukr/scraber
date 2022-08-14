import func as opse

adress = input('Enter url: ')
html = opse.open_html(adress)

opse.save_html(adress)