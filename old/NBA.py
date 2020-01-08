import requests
from bs4 import BeautifulSoup
import datetime
import pandas
import re

def get_sort(url):
    r = requests.get(url)
    html = r.content
    html = html.decode('UTF-8')
    soup1 = BeautifulSoup(html, 'lxml')
    #print(soup1)
    sort = soup1.find_all('tr', class_='sort')
    #print(sort)
    return sort
def get_player(sort,player_name):
    for item in sort:
        name_info = item.find('td',class_=re.compile("normal player_name_out change_color col0 row\d")).text.strip()
        #print(name_info)
        if(name_info == player_name):
            time_info = item.find('td',class_=re.compile("normal mp change_color col2 row\d")).text.strip()
            ratio_info = item.find('td',class_=re.compile("normal fgper change_color col3 row\d")).text.strip()
            get_ball = item.find('td',class_=re.compile("normal fg change_color col4 row\d")).text.strip()
            total_ball = item.find('td',class_=re.compile("normal fga change_color col5 row\d")).text.strip()
            free_get_ball = item.find('td',class_=re.compile("normal ft change_color col10 row\d")).text.strip()
            free_total_ball = item.find('td',class_=re.compile("normal fta change_color col11 row\d")).text.strip()
            three_get_ball = item.find('td',class_=re.compile("normal threep change_color col7 row\d")).text.strip()
            three_total_bal = item.find('td',class_=re.compile("normal threepa change_color col8 row\d")).text.strip()


#get_info("http://www.stat-nba.com/game/17437.html")
get_player(get_sort("http://www.stat-nba.com/game/17437.html"),"阿伦-艾弗森")