import pandas as pd
import numpy as np


委買= pd.DataFrame(columns=['價格', '張數'])
委賣= pd.DataFrame(columns=['價格', '張數'])
output = pd.DataFrame(columns=['T','Ask','Bid', 'Price'])
輸入 = pd.DataFrame(columns=['狀態','張數','價格',])
list123 = list()
a =''
count = 0
i=0
while a !='quit 1':
    a = input()
    count +=1
    b = a.split()
    if len(b) == 1:
        list123.append(int(b[0]))
        total = list123[0]
        i +=1
    if len(b) > 1 and count <= (list123[i-1])*total+2:
        輸入=輸入.append({'狀態':b[0],'張數' : b[1] , '價格' : b[4]},ignore_index=True)


print(輸入)