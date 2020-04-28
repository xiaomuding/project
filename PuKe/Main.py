from PuKe.Winner import *
from PuKe.Wanjia import *

winner = Winner("patric")
winner.getYiFuPai()

wanjia1 = Wanjia("文杰",winner.AllPai[1],winner.AllPai[2],winner.AllPai[3])
wanjia2 = Wanjia("韩鹏",winner.AllPai[4],winner.AllPai[5],winner.AllPai[6])

print(wanjia1.name,"------",wanjia1.Pai1,wanjia1.Pai2,wanjia1.Pai3)
#print(wanjia1.name,"------",wanjia1.PaiXing,wanjia1.DianShu1,wanjia1.DianShu2,wanjia1.DianShu3,wanjia1.HuaSe1,wanjia1.HuaSe2,wanjia1.HuaSe3)

print(wanjia2.name,"------",wanjia2.Pai1,wanjia2.Pai2,wanjia2.Pai3)
#print(wanjia2.name,"------",wanjia2.PaiXing,wanjia2.DianShu1,wanjia2.DianShu2,wanjia2.DianShu3,wanjia2.HuaSe1,wanjia2.HuaSe2,wanjia2.HuaSe3)

winner.whoWin(wanjia1,wanjia2)