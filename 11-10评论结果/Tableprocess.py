import pandas as pd
df1 = pd.read_excel(r'C:\Users\xiaoLiu\Desktop\口碑评论.xlsx', header=0, index_col=None)
df2 = pd.read_excel(r'C:\Users\xiaoLiu\Desktop\评论详情.xlsx', header=0, index_col=None)
df3 = pd.merge(df1, df2, how='outer', on='字段4_link', left_on=None, right_on=None,
               left_index=False, right_index=False, sort=False,
               suffixes=('_x', '_y'), copy=True, indicator=False)
df3.to_csv('./lianjiepinglun.csv')