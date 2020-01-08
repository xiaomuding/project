from Crawler import *
from tooling import *
import queue
import time
from threading import Thread,Lock
#import requests
#from bs4 import BeautifulSoup
#import datetime
import pandas
#import re
#import os

#total_data = []
input_list = [{"year": 2000 ,"team" : ["湖人","76人"],"player" : ["沙奎尔-奥尼尔","阿伦-艾弗森","科比-布莱恩特"]}
            ,{"year": 2001 ,"team" : ["湖人","篮网"],"player" : ["沙奎尔-奥尼尔","杰森-基德","科比-布莱恩特"]},
              {"year": 1999 ,"team" : ["湖人","步行者"],"player" : ["沙奎尔-奥尼尔","雷吉-米勒","科比-布莱恩特"]}]

def main():
    q = queue.Queue()
    ts = []
    for list in input_list:
        print("start")
        link_list = find_link(list["year"], list["team"][0], list["team"][1])
        for link in link_list:
            q.put(link)
        while not q.empty():
            #for i in range(1,3):
            t = playerCrawler(q,list["player"])
            ts.append(t)
            #print(q)
    for t in ts:
        t.start()
    for t in ts:
        t.join()

if __name__ == '__main__':
    start_time = time.time()
    # 启动爬虫
    main()
    print("finish-----------")
    #print(total_data)
    get_csv(total_data, "total.csv")
    end_time = time.time()
    #print("time consumed", end_time-start_time)
    print("total consume time is ", end_time - start_time)
