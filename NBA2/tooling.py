import requests
from bs4 import BeautifulSoup
#import datetime
import pandas
import re
from Crawler import *
import Crawler


def get_lxml(url):
    r = requests.get(url, timeout=200)
    html = r.content
    html = html.decode('UTF-8')
    lxml = BeautifulSoup(html, 'lxml')
    return lxml
def get_player(url, player_name):
    lxml = get_lxml(url)
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

def find_link(year,team1,team2):
    org_url = "http://www.stat-nba.com/playoffchart/" + str(year) + ".html"
    lxml = get_lxml(org_url)
    game_link_list = lxml.find_all('a', class_='gamelink')
    #print(game_link)
    link_list = []
    for game_link in game_link_list:
        text = game_link.text.strip()
        link = game_link['href']
        if(team1 in text and team2 in text):
            link_list.append("http://www.stat-nba.com" + link)
    return link_list

def get_csv_data(link_list,player_list):
    sum_data = []
    for player in player_list:
        for url in link_list:
            player_data = get_player(url, player)
            if(player_data != None):
                sum_data.append(player_data)
    return sum_data

def get_csv(sum_data,file_name):
    test = pandas.DataFrame(data=sum_data,
                            columns=["姓名", "得分", "投篮", "命中", "出手", "时间", "篮板", "助攻", "抢断", "盖帽", "失误", "罚球命中", "罚球总数",
                                     "三分命中", "三分出手"],
                            )
    test.to_csv(file_name, encoding='utf-8')


