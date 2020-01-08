import requests
from bs4 import BeautifulSoup
#import datetime
import pandas
import re
from Crawler import *
import Crawler


def find_link(year,team1,team2):
    org_url = "http://www.stat-nba.com/playoffchart/" + str(year) + ".html"
    lxml = playerCrawler.get_lxml(org_url)
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
            player_data = playerCrawler.get_player(url, player)
            if(player_data != None):
                sum_data.append(player_data)
    return sum_data

def get_csv(sum_data,file_name):
    test = pandas.DataFrame(data=sum_data,
                            columns=["姓名", "得分", "投篮", "命中", "出手", "时间", "篮板", "助攻", "抢断", "盖帽", "失误", "罚球命中", "罚球总数",
                                     "三分命中", "三分出手"],
                            )
    test.to_csv(file_name, encoding='utf-8')


