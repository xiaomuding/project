from PuKe.Wanjia import *
from PuKe.YiFuPai import *
import random

class Winner:
    AllPai = [];
    def __init__(self,name):
        self.name = name
    def whoWin(self,wanjia1,wanjia2): #判断大小
        if wanjia1.PaiXing > wanjia2.PaiXing:
            print(wanjia1.name, "WIN")

    def getYiFuPai(self,): #得到一副有顺序的牌，然后洗牌，
        for num in Num:
            for color in Color:
                self.AllPai.append({"num": num, "color": color})
        #print(self.AllPai)
        #random.shuffle(self.AllPai)  #这里是python自带的随机打乱数组算法，自己实现一下试试？？
        for i in range(0, len(self.AllPai) - 1):
            #print(i)
            p = random.randrange(i, len(self.AllPai))
            self.AllPai[i], self.AllPai[p] = self.AllPai[p], self.AllPai[i]
        #print(self.AllPai)


#xianqiang = Winner("xianqiang")
#xianqiang.getYiFuPai()





