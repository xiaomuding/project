import requests
from bs4 import BeautifulSoup
#import datetime
#import pandas
import re

class playerCrawler:
    def __init__(self,name):
        self.name = name

    @classmethod
    def get_lxml(cls,url):
        r = requests.get(url,timeout = 200)
        html = r.content
        html = html.decode('UTF-8')
        lxml = BeautifulSoup(html, 'lxml')
        return lxml
    @classmethod
    def get_player(cls,url, player_name):
        lxml = cls.get_lxml(url)
        sort = lxml.find_all('tr', class_='sort')
        for item in sort:
            name_info = item.find('td',
                                  class_=re.compile("normal player_name_out change_color col0 row\d")).text.strip()
            # print(name_info)
            if (name_info == player_name):
                score = item.find('td', class_=re.compile("normal pts change_color col21 row\d")).text.strip()
                ratio_info = item.find('td', class_=re.compile("normal fgper change_color col3 row\d")).text.strip()
                get_ball = item.find('td', class_=re.compile("normal fg change_color col4 row\d")).text.strip()
                total_ball = item.find('td', class_=re.compile("normal fga change_color col5 row\d")).text.strip()
                time_info = item.find('td', class_=re.compile("normal mp change_color col2 row\d")).text.strip()
                rebounds = item.find('td', class_=re.compile("normal trb change_color col13 row\d")).text.strip()
                assists = item.find('td', class_=re.compile("normal ast change_color col16 row\d")).text.strip()
                steals = item.find('td', class_=re.compile("normal stl change_color col17 row\d")).text.strip()
                blocks = item.find('td', class_=re.compile("normal blk change_color col18 row\d")).text.strip()
                error = item.find('td', class_=re.compile("normal tov change_color col19 row\d")).text.strip()
                free_get_ball = item.find('td', class_=re.compile("normal ft change_color col10 row\d")).text.strip()
                free_total_ball = item.find('td', class_=re.compile("normal fta change_color col11 row\d")).text.strip()
                three_get_ball = item.find('td',
                                           class_=re.compile("normal threep change_color col7 row\d")).text.strip()
                three_total_ball = item.find('td',
                                             class_=re.compile("normal threepa change_color col8 row\d")).text.strip()
                # print(score)
                data_list = [player_name, score, ratio_info, get_ball, total_ball, time_info, rebounds, assists, steals,
                             blocks, error, free_get_ball, free_total_ball, three_get_ball, three_total_ball]
                # print(data_list)
                return data_list



