Num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Color = ["Hei","Hong","Mei","Fang"]

#Pai = {"num":"1","color":"Hei"}
#print(Pai)

AllPai= [];
def GetYiFuPai():
    for num in Num:
        for color in Color:
            AllPai.append({"num":num,"color":color})

#print(AllPai[5]["num"])
#YiShouPai = [];
