from Crawler import *
from tooling import *
#import requests
#from bs4 import BeautifulSoup
#import datetime
import pandas
import time
#import re

#import os

'''
player_list = ["沙奎尔-奥尼尔","阿伦-艾弗森","科比-布莱恩特"]
link_list = find_link(2000,"湖人","76人")
get_csv(link_list,player_list,"test.csv")

#os.environ['HTTP_PROXY'] = 'http://127.0.0.1:1080'
#os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:1080'
'''

input_list = [{"year": 2000 ,"team" : ["湖人","76人"],"player" : ["沙奎尔-奥尼尔","阿伦-艾弗森","科比-布莱恩特"]}
            ,{"year": 2001 ,"team" : ["湖人","篮网"],"player" : ["沙奎尔-奥尼尔","杰森-基德","科比-布莱恩特"]},
              {"year": 1999 ,"team" : ["湖人","步行者"],"player" : ["沙奎尔-奥尼尔","雷吉-米勒","科比-布莱恩特"]}]

total_data = []
start_time = time.time()
for list in input_list:
    print("start")
    link_list = find_link(list["year"],list["team"][0],list["team"][1])
    print(link_list)
    sum_data = get_csv_data(link_list,list["player"])
    print(sum_data)
    total_data.extend(sum_data)

print("got total data")

get_csv(total_data,"1total.csv")
end_time = time.time()
print("total consume time is ", end_time-start_time)