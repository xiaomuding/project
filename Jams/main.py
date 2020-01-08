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

for j in range(5):
    t1 = playerCrawler(east_link_q,target_players,"东部")
    t1.start()
    threads_player.append(t1)
    t2 = playerCrawler(west_link_q, target_players,"西部")
    t2.start()
    threads_player.append(t2)

for thread in threads_link:
    thread.join()


for j in range(5):
    east_link_q.put(None)
    west_link_q.put(None)

for thread in threads_player:
    thread.join()

print("对战东部：")
while not data_q_east.empty():
    print(data_q_east.get())

print("对战西部：")
while not data_q_west.empty():
    print(data_q_west.get())


