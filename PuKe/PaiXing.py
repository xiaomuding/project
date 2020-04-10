from PuKe.YiFuPai import *


DanZhang = 100000000
DuiZi = 200000000
ShunZi = 300000000
TongHua = 400000000
TongHuaShun = 500000000
BaoZi = 600000000
def NumCompare(num1,num2,num3):
    if num1 == num2 and num1 == num3:
        return 3
    elif(num1 == num2 and num1 != num3) or (num1 == num3 and num1 != num2) or (num2 == num3 and num2 != num1):
        return 2
    elif max(num1,num2,num3) - min(num1,num2,num3) == 2:
        return 8
    else:
        return 0

#print(NumCompare(5,6,7))

def ColorCompare(color1,color2,color3):
    if color1 == color2 and color1 == color3:
        return 1
    else:
        return 0

def ColorNum(color):
    if color == "Hei":
        return 4
    elif color == "Hong":
        return 3
    elif color == "Mei":
        return 2
    else:
        return 1


def PanDuan(Pai1,Pai2,Pai3):
    #print(Pai["num"],"****",Pai["color"])
    tem1 = NumCompare(Pai1["num"],Pai2["num"],Pai3["num"])
    tem2 = ColorCompare(Pai1["color"],Pai2["color"],Pai3["color"])
    if tem1 == 3:
        return BaoZi+Pai1["num"]*10
    elif tem1 ==2:
        if Pai1["num"] == Pai2["num"]:
            return DuiZi+1000*Pai1["num"]+Pai3["num"]*10----------------做到这里了
    elif tem1 == 8 and tem2 == 1:
        return TongHuaShun
    elif tem1 ==8 and tem2 == 0:
        return ShunZi
    elif tem1 == 0 and tem2 == 1:
        return TongHua
    else:
        return DanZhang


GetYiFuPai()
#print(AllPai)
print(PanDuan(AllPai[1],AllPai[28],AllPai[37]))