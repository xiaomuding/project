import requests
from bs4 import BeautifulSoup
import datetime
import pandas


link = 'http://bbs.hupu.com/bxj'

r = requests.get(link)
html = r.content
html = html.decode('UTF-8')
soup1 = BeautifulSoup(html,'lxml')

soup = soup1.find('div',class_='show-list')

post_list = soup.find_all('li')
#print(post_list,"----------------")
data_list = []
for post in post_list:

    title_id = post.find('div',class_='titlelink box')
    print(title_id,"-------")

    title1 = title_id.a
    print(title1,"*****")
    title2 = title1.text

    print(title2, "------------")
    title=title2.strip()
    print(title,"------------")

    post_link = title_id.a['href']
    post_link = 'https://bbs.hupu.com'+post_link
    print(post_link)
    

    #作者、作者链接、创建时间
    author_div = post.find('div',class_='author box')
    print(author_div,"----------------------")

    author = author_div.find('a',class_='aulink').text.strip()
    print(author, "----------------------")

    author_page = author_div.find('a',class_='aulink')['href']
    print(author_page,"----------")

    start_data1 = author_div.select('a:nth-of-type(2)')[0]
    print(start_data1,"----------")
    start_data = start_data1.get_text()
    print(start_data,"-------------")
    
    #回复人数和浏览次数
    reply_view = post.find('span',class_='ansour box').text.strip()
    print(reply_view,"--------------")

    reply = reply_view.split('/')[0].strip()
    view = reply_view.split('/')[1].strip()
    print(reply,"----",view,"--------")

    #最后回复用户和最后回复时间
    reply_div = post.find('div',class_='endreply box')
    print(reply_div,"------------------")

    reply_time = reply_div.a.text.strip()

    print(reply_time,"----------------")

    #last_reply = reply_div.find('span',class_='endauthor').text.strip()
    last_reply = reply_div.span.text.strip()
    print(last_reply,"--------------")

    if ':' in reply_time:
        date_time = str(datetime.date.today())+' '+ reply_time

        print(date_time,"**********")
        date_time = datetime.datetime.strptime(date_time,'%Y-%m-%d %H:%M')

        print(date_time, "**********")
    else:
        date_time = datetime.datetime.strptime(reply_time,'%Y-%m-%d').date()
        print(date_time,"-----------")

    data_list.append([title,post_link,author,author_page,start_data,reply,view,last_reply,date_time.strftime('%Y-%m-%d %H:%M')])

#print(data_list)


#test=pandas.DataFrame(data=data_list)
#test.to_csv("./test.csv",encoding='utf-8')
