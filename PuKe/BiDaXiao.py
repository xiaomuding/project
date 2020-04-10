from PuKe.PaiXing import *

GetYiFuPai()
print(AllPai)

Player1 = [AllPai[1],AllPai[2],AllPai[3]]
Player1 = [AllPai[1],AllPai[2],AllPai[3]]

def Compare(player1,player2):
    PaiXing_player1 = PanDuan(player1[1],player1[2],player1[3])
    PaiXing_player2 = PanDuan(player2[1], player2[2], player2[3])
