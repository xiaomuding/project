from PuKe.YiFuPai import *
from PuKe.PaiXing import *

class Wanjia():
    PaiXing = ""
    DianShu1 = ""
    DianShu2 = ""
    DianShu3 = ""
    HuaSe1 = ""
    HuaSe2 = ""
    HuaSe3 = ""
    def __init__(self,pai1,pai2,pai3):
        self.Pai1 = pai1
        self.Pai2 = pai2
        self.Pai3 = pai3
    #def getPaiXing(self):
        tem1 = NumCompare(self.Pai1["num"], self.Pai2["num"], self.Pai3["num"])
        tem2 = ColorCompare(self.Pai1["color"], self.Pai2["color"], self.Pai3["color"])
        if tem1 == 3:  #豹子只需要比较点数
            self.PaiXing =  BaoZi
            self.DianShu1 = self.Pai1["num"]
        elif tem1 == 2: #对子先比对子点数，再比第三张点数，再比对子花色
            self.PaiXing = DuiZi
            if self.Pai1["num"] == self.Pai2["num"]:
                self.DianShu1 = self.Pai1["num"]
                self.HuaSe1 = max(ColorNum(self.Pai1["color"]),ColorNum(self.Pai2["color"]))
                self.DianShu2 = self.Pai3["num"]
            if self.Pai1["num"] == self.Pai3["num"]:
                self.DianShu1 = self.Pai1["num"]
                self.HuaSe1 = max(ColorNum(self.Pai1["color"]),ColorNum(self.Pai3["color"]))
                self.DianShu2 = self.Pai2["num"]
            if self.Pai3["num"] == self.Pai2["num"]:
                self.DianShu1 = self.Pai3["num"]
                self.HuaSe1 = max(ColorNum(self.Pai3["color"]),ColorNum(self.Pai2["color"]))
                self.DianShu2 = self.Pai1["num"]
        elif tem1 == 8 and tem2 == 1: #同花顺先比顺子中最大的点数，再比花色
            self.PaiXing = TongHuaShun
            self.DianShu1 = max(self.Pai1["num"],self.Pai2["num"],self.Pai3["num"])
            self.HuaSe1 = ColorNum(self.Pai1["color"])
        elif tem1 == 8 and tem2 == 0: #顺子先比点数，再比花色
            self.PaiXing = ShunZi
            self.DianShu1 = max(self.Pai1["num"], self.Pai2["num"], self.Pai3["num"])
            if self.DianShu1 == self.Pai1["num"]:
                self.HuaSe1 =ColorNum(self.Pai1["color"])
            elif self.DianShu1 == self.Pai2["num"]:
                self.HuaSe1 = ColorNum(self.Pai2["color"])
            else:
                self.HuaSe1 = ColorNum(self.Pai3["color"])
        elif tem1 == 0 and tem2 == 1:  #同花先比点数，后比花色
            self.PaiXing = TongHua
            self.DianShu1 = max(self.Pai1["num"],self.Pai2["num"],self.Pai3["num"])
            self.DianShu3 = min(self.Pai1["num"],self.Pai2["num"],self.Pai3["num"])
            if self.DianShu1 == self.Pai1["num"]:
                if self.DianShu3 == self.Pai2["num"]:
                    self.DianShu2 = self.Pai3["num"]
                else:
                    self.DianShu2 = self.Pai2["num"]
            elif self.DianShu1 == self.Pai2["num"]:
                if self.DianShu3 == self.Pai1["num"]:
                    self.DianShu2 = self.Pai3["num"]
                else:
                    self.DianShu2 = self.Pai1["num"]
            else:
                if self.DianShu3 == self.Pai1["num"]:
                    self.DianShu2 = self.Pai2["num"]
                else:
                    self.DianShu2 = self.Pai1["num"]
            self.HuaSe1 = self.Pai1["color"]

        else:  #单张比点数，再比花色
            self.PaiXing =  DanZhang
            self.DianShu1 = max(self.Pai1["num"], self.Pai2["num"], self.Pai3["num"])
            self.DianShu3 = min(self.Pai1["num"], self.Pai2["num"], self.Pai3["num"])

            if self.DianShu1 == self.Pai1["num"]:
                self.HuaSe1 = ColorNum(self.Pai1["color"])
                if self.DianShu3 == self.Pai2["num"]:
                    self.DianShu2 = self.Pai3["num"]
                else:
                    self.DianShu2 = self.Pai2["num"]
            elif self.DianShu1 == self.Pai2["num"]:
                self.HuaSe1 = ColorNum(self.Pai2["color"])
                if self.DianShu3 == self.Pai1["num"]:
                    self.DianShu2 = self.Pai3["num"]
                else:
                    self.DianShu2 = self.Pai1["num"]
            else:
                self.HuaSe1 = ColorNum(self.Pai3["color"])
                if self.DianShu3 == self.Pai1["num"]:
                    self.DianShu2 = self.Pai2["num"]
                else:
                    self.DianShu2 = self.Pai1["num"]

