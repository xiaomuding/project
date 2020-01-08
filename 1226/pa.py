import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler:
    def __init__(self,provinces):
        self.provinces = provinces
    def start_element(self,name,attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name,number))
    def end_element(self,name):
        pass
    def char_data(self,text):
        pass



def get_entry(url):

    content = requests.get(url).content.decode('gb2312')
    start = content.find('<map name="map_86" id="map_86">')

    end = content.find('</map>')
    print(start,"******",end,"******",len('</map>'))
    content = content[start:end].strip()
    #return content
    provinces = []
    handle = DefaultSaxHandler(provinces)
    parse = ParserCreate()
    parse.StartElementHandler = handle.start_element
    #parse.EndElementHandler = handle.end_element
    parse.Parse(content)
    return provinces



orig = get_entry("http://www.ip138.com/post/")
print(orig)