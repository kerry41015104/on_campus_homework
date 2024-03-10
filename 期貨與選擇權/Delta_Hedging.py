import numpy as np
from Monte_Carlo_Simulation import Monte_Carlo, BS_formula
from Binomial_Trees import bitcall_Eur_2
from scipy.stats import norm
import pandas as pd
from tqdm import tqdm

def hedge_strategy(way="delta"):
    df = pd.DataFrame(columns=['time_rebalance', 'performance'])
    time_rebalance = [5,4,2,1,0.5,0.25]
    for kk in tqdm(time_rebalance):
        rebalance_freq = kk
        dt = rebalance_freq/52
        idx = np.linspace(0,20,num=int(20/rebalance_freq)+1)
        out = Monte_Carlo(S,T,u,sigma,int(20/rebalance_freq),1000)
        out = np.round(out, decimals=2)
        out = np.transpose(out)
        total_cost=np.zeros((out.shape[1],))
        #scenarios = np.zeros((out.shape[0]+1, 7))
        for j in range(out.shape[1]):
            scenarios = np.zeros((out.shape[0]+1, 7))
            for i in range(1, out.shape[0]+1):
                scenarios[i, 0] = idx[i-1]
                scenarios[i, 1] = out[i-1, j]
                if way =="stop_loss":
                    if scenarios[i, 1] >= K: scenarios[i, 2] = 1
                    else: scenarios[i, 2] = 0
                else:
                    scenarios[i, 2] = BS_formula(out[i-1, j], K, ((20-(idx[i-1]))/52+0.00000001), r, sigma, 'c')[1].round(3)
                scenarios[i, 3] = (scenarios[i, 2] - scenarios[i-1, 2])*unit_shares
                scenarios[i, 4] = ((scenarios[i, 3] * out[i-1, j])/1000).round(1)
                scenarios[i, 5] = (scenarios[i-1, 5] + scenarios[i-1, 6] + scenarios[i, 4])
                scenarios[i, 6] = (scenarios[i, 5] * (r* dt)).round(1)

            if scenarios[-1, 1] >= K:
                total_cost[j] = scenarios[-1, 5]*1000-K*unit_shares
            else:
                total_cost[j] = scenarios[-1, 5]*1000
        df = df.append({'time_rebalance':kk, 'performance':(np.std(total_cost) / op_value).round(3)}, ignore_index=True)
    return df.T,idx
#第二題
S = 49
K = 50
r = 0.05
sigma = 0.2
T = 20/52 
unit_shares = 100000
u = 0.13
op_value = BS_formula(S, K, T, r, sigma, 'c')[0] * unit_shares
df,idx = hedge_strategy("delta") #using delta or stop_loss
print(df)
#第三題 計算Put Greek Letters using closed-form formula
S = 50
K = 52
r = 0.05
sigma = 0.3
T = 2
d1 =(np.log(S / K) + (r + sigma * sigma / 2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)
delta = norm.cdf(d1)-1
gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
theta = - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2)
vega = S * norm.pdf(d1) * np.sqrt(T)
rho = -K * T * np.exp(-r * T) * norm.cdf(-d2)
print("delta:",delta.round(3),"gamma:",gamma.round(3),"theta:",theta.round(3),"vega:",
      vega.round(3),"rho:",rho.round(3))

price , STree= bitcall_Eur_2(S, K, T, r, sigma, 252*T, 'p')
delta_tree = (price[0,1] - price[1,1])/(STree[0,1] - STree[1,1])
dd1 =(price[0,2] - price[1,2])/(STree[0,2] - STree[0,0])
dd2 = (price[1,2] - price[2,2])/(STree[0,0] - STree[2,2])
h = 0.5*(STree[0,2] - STree[2,2])
gamma_tree = (dd1 - dd2)/h
theta_tree = (price[1,2] - price[0,0])/(2*(1/252))
price_sigma ,_= bitcall_Eur_2(S, K, T, r, sigma+0.0001, 252*T, 'p')
vega_tree = (price_sigma[0,0] - price[0,0])/0.0001
price_r ,_= bitcall_Eur_2(S, K, T, r+0.0001, sigma, 252*T, 'p')
rho_tree = (price_r[0,0] - price[0,0])/0.0001
print()
print("delta_tree:",delta_tree.round(3),"gamma_tree:",gamma_tree.round(3),"theta_tree:",
      theta_tree.round(3),"vega_tree:",vega_tree.round(3),"rho_tree:",rho_tree.round(3))