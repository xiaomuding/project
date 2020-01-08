import requests
from bs4 import BeautifulSoup
import datetime
import pandas

data_list= []
link = 'https://bbs.hupu.com/vote'
for i in range(0,10):
    url = link+'-'+ str(i)
    r = requests.get(url)
    html = r.content
    html = html.decode('UTF-8')
    soup1 = BeautifulSoup(html,'lxml')
    #print(soup1)
    soup = soup1.find('ul',class_ = 'for-list')
    #print(soup)
    soup_list = soup.find_all('li')
    #print(soup_list)
    soup_list.remove(soup_list[0])


    for list in soup_list:
        #取title
        title = list.find('a',class_= 'truetit')
        #print(title,"--------------")
        title = title.text.strip()
        #print(title, "--------------")
        #取作者
        author = list.find('a', class_='aulink')
        #print(author, "--------------")
        author = author.text.strip()
        #print(author, "--------------")
        #取回复次数
        reply = list.find('span', class_='ansour box')
        #print(reply, "--------------")
        reply = reply.text.strip()
        #print(reply, "--------------")
        reply_list = reply.split('/')
        #print(reply_list)
        reply = reply_list[0].strip()
        #print(reply,"#########")
        data_list.append([title,author,reply])

#print(data_list)
new_data_list = []
for list1 in data_list:
    if list1 not in new_data_list:
        new_data_list.append(list1)

test=pandas.DataFrame(data=new_data_list)
test.to_csv("./shihuhu.csv",encoding='utf-8')
