import pandas as pd
import numpy as np
from sympy import *
本金攤還 = pd.DataFrame(columns=['pmt','利息','償還本金', '尚欠本金'])
x = Symbol('x')
pmt = solve((x/(0.0194/12))*(1-1/(1+0.0194/12)**216)-20000000,x)[0]

本金攤還=本金攤還.append({'pmt':0,'利息' : 0 , '償還本金' : 0,'尚欠本金':20000000},ignore_index=True)

for i in range(0,24):
    本金攤還=本金攤還.append({'pmt':20000000*(0.0194/12),'利息' : 20000000*(0.0194/12) , '償還本金' : 0,'尚欠本金':20000000},ignore_index=True)

for i in range(25,241):
    本金攤還=本金攤還.append({'pmt':pmt,'利息' :本金攤還.iloc[i-1,3]*(0.0194/12)  , '償還本金' :pmt-本金攤還.iloc[i-1,3]*(0.0194/12),'尚欠本金':本金攤還.iloc[i-1,3]-pmt+本金攤還.iloc[i-1,3]*(0.0194/12)},ignore_index=True)

本金攤還 = 本金攤還.astype('float32')

本金攤還 = np.around(本金攤還,)
print(本金攤還)
print("利息總合:",sum(本金攤還['利息']))