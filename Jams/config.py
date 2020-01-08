import queue

#赛季
years =[2003]
#比赛类型字典
game_types = {"regular":"常规赛","post":"季后赛","final":"总决赛"}
#目标比赛类型
game_type = game_types["regular"]

#目标球员list
target_players = ["勒布朗-詹姆斯"]
#目标球队所在球队list
target_teams = "骑士"
#存放每一场次的URL
link_q = queue.Queue()
#存放球员数据
data_q = queue.Queue()
#东部球队list
east_team = ["凯尔特","雄鹿","公牛","活塞","尼克斯","步行者","篮网","老鹰","奇才","骑士","魔术","猛龙","人","热火","活塞"]
#西部球队list
west_team = ["灰熊","马刺","快船","太阳","爵士","独行侠","掘金","鹈鹕","勇士","火箭","森林狼","开拓者","湖人","马刺","超音速","雷霆"]
#存放对战东部球队数据
data_q_east = queue.Queue()
#存放对战西部球队数据
data_q_west = queue.Queue()
#存放取场次url的线程
threads_link = []
#存放取球员数据的线程
threads_player = []