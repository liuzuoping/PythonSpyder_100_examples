# -*- coding: utf-8 -*-
# coding: utf-8
import pandas as pd
import numpy as np
data1=pd.read_csv('housedata1.csv',encoding='gbk')
data2=pd.read_csv('housedata2.csv',encoding='gbk')
data=pd.concat([data1,data2],axis=0,ignore_index=False)
data=pd.DataFrame(data)
# data=str(data).encode('gbk')
data=data.sort_values('area')
data=data.reset_index()
data=data.drop(labels='index',axis=1)
# print(data.head())
print(data.loc[:,'area'].value_counts())
# for i,data['price'][i] in enumerate(data['price']):
#     data['price'][i]=int(data['price'][i].replace('元/平',''))
    #print(i,data['price'][i])
# print('changed_price\n',data['price'].head())
# print(data.head())

# print(type(data['price'][0])
data.to_csv('cleaned.csv', mode='a', encoding='gbk', header=False, index=False)

# print(data.loc[:,'area'].value_counts())
# print(data.describe())

# area=data.groupby(by='area')['price'].mean()

#print(data.loc[:,'price'].mean())
#area=data.groupby(by='area')['price']
# print(area)