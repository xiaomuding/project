import requests
from bs4 import BeautifulSoup
from Jams.tooling import *
from Jams.config import *
#import datetime
import pandas
import re
import queue


def find_links(year):
    #global link_q
    #上半个赛季
    for month in ["10","11","12"]:
        print("start",year,month)
        org_url = "http://www.stat-nba.com/gameList_simple-" + str(year) + "-" + month + ".html"
        get_link(org_url)
    #下半个赛季（第二年）
    for month in ["01","02","03","04","05","06"]:
        print("start",year,month)
        org_url = "http://www.stat-nba.com/gameList_simple-" + str(year+1) + "-" + month + ".html"
        get_link(org_url)


def get_link(org_url):
    lxml = get_lxml(org_url)
    game_link_list = lxml.find_all('a', target="_blank")
    # print(game_link_list)
    for game_link in game_link_list:
        text = game_link.text.strip()
        link = game_link['href']
        if (target_teams in text):
            #link_q.put("http://www.stat-nba.com/" + link)
            #print(text)
            text_list = text.split("-")
            #print(text_list)
            for t in text_list:
                tem = re.findall(r"\D*",t)
                #print(tem)
                while '' in tem:
                    tem.remove('')
                enemy = ''.join(tem)
                print(enemy)
                if(enemy == target_teams):
                    continue
                elif(enemy in east_team):
                    print("东部对手")
                    east_link_q.put("http://www.stat-nba.com/" + link)
                else:
                    print("西部对手")
                    west_link_q.put("http://www.stat-nba.com/" + link)


#test
#get_link("http://www.stat-nba.com/gameList_simple-2008-04.html")



