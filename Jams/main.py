import requests
from bs4 import BeautifulSoup
from Jams.tooling import *
from Jams.get_link import *
from Jams.Crawler import *
from threading import Thread,Lock
import threading
import time
#import datetime
import pandas
import re
from Jams.config import *


#每一年一个线程
for year in years:
    t = threading.Thread(target=find_links, args=(year,))
    t.start()
    threads_link.append(t)

#time.sleep(20)

for j in range(10):
    t = playerCrawler(link_q,target_players)
    t.start()
    threads_player.append(t)

for thread in threads_link:
    thread.join()


for thread in threads_player:
    link_q.put(None)
    print("put a None")

for thread in threads_player:
    thread.join()

while not data_q.empty():
    print(data_q.get())


