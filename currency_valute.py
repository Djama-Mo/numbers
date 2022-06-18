from urllib.request import urlopen
from xml.dom import minidom

# URL with XML-data of Foreign Currency Market
URL = 'https://www.cbr.ru/scripts/XML_daily.asp'


# Get XML file from URL
def get_data(url):
    return urlopen(url).read()


# Get current value USD -> RUB
def get_current_value():
    dom = minidom.parseString(get_data(URL))
    dom.normalize()
    elements = dom.getElementsByTagName('Valute')
    for node in elements:
        if node.childNodes[0].firstChild.data == '840':
            return node.childNodes[4].firstChild.data.replace(',', '.')
