import requests
from bs4 import BeautifulSoup
#import datetime
#import pandas
import re
import os
import queue
from threading import Thread,Lock
import threading

total_data = []
num = 0

class playerCrawler(threading.Thread):
    def __init__(self,q,player_list):
        threading.Thread.__init__(self)
        self.q = q
        self.url = self.q.get()
        self.player_list = player_list
        print(player_list)
    def run(self) -> None:
        self.get_data()

    def get_lxml(self):
        print("get lxml")
        try:
            r = requests.get(self.url,timeout = 200)
        except Exception as e:
            self.q.put(self.url)
            print(e)
        html = r.content
        html = html.decode('UTF-8')
        lxml = BeautifulSoup(html, 'lxml')
        return lxml
    def get_data(self):
        global total_data
        global num
        print("get data")
        for player_name in self.player_list:
            data = self.get_player(player_name)
            print(data)
            if(num == 0):
                if (data != None):
                    num = 1
                    total_data.append(data)
                    num = 0

    def get_player(self,player_name):
        print("get player")
        lxml = self.get_lxml()
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




