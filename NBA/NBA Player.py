import pandas as pd
import numpy as n

# 读取网页中的数据表
table = []
for i in range(1,7):
    table.append(pd.read_html('https://nba.hupu.com/stats/players/pts/%d' %i)[0])

# 所有数据纵向合并为数据框
players = pd.concat(table)
# 变量重命名
columns=['排名','球员','球队','得分','命中-出手','命中率','命中-三分','三分命中率','命中-罚球','罚球命中率','场次','上场时间']
players.columns=columns


players.drop(0,inplace=True)
players.to_csv(r"C:\Users\MI\Desktop\球员信息.csv",encoding='utf_8_sig')

