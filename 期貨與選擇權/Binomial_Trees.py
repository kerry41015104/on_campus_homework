import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def bitcall_Eur_2(S, k, T, r, vol, N, option_type): #有每一步的option price
    dt = T / N
    u = math.exp(vol * math.sqrt(dt))
    d = math.exp(-vol * math.sqrt(dt))
    p = (math.exp(r * dt) - d) / (u - d)
    STree = np.zeros((N + 1, N + 1))
    price = np.zeros((N + 1, N + 1))
    STree[0][0] = S
    for c1 in range(N):
        STree[0][c1 + 1] = STree[0][c1] * u
        for r1 in range(c1 + 1):
            STree[r1 + 1][c1 + 1] = STree[r1][c1] * d

    if option_type == 'c':
        price[:,-1] = np.maximum(STree[:,-1] - k, 0)
    if option_type == 'p':
        price[:,-1] = np.maximum(k - STree[:,-1], 0)

    for c1 in range(N-1,-1,-1):
        for r1 in range(N):
            price[r1][c1] = (p*price[r1][c1+1] + (1-p)*price[r1+1][c1+1])*math.exp(-r*dt)
    return price,STree

def BS_formula(s, k, t, r, vol,option_type):
    d1 = (math.log(s / k) + (r + vol * vol / 2) * t) / (vol * math.sqrt(t))
    d2 = d1 - vol * math.sqrt(t)
    if option_type == 'c':
        price = s * norm.cdf(d1) - k * math.exp(-r * t) * norm.cdf(d2)
    else:
        price = k * math.exp(-r * t) * norm.cdf(-d2) - s * norm.cdf(-d1) 
    return price

def bitcall_Eur(S, k, T, r, vol, N, option_type): #European option
    dt = T / N
    u = math.exp(vol * math.sqrt(dt))
    d = math.exp(-vol * math.sqrt(dt))
    p = (math.exp(r * dt) - d) / (u - d)
    STree = np.zeros((N + 1, N + 1))
    PTree = np.zeros((N + 1, N + 1))
    STree[0][0] = S
    for c1 in range(N):
        STree[0][c1 + 1] = STree[0][c1] * u
        for r1 in range(c1 + 1):
            STree[r1 + 1][c1 + 1] = STree[r1][c1] * d

    PTree[0][0] = 1
    for c1 in range(N):
        for r1 in range(c1 + 1):
            PTree[r1][c1 + 1] += PTree[r1][c1] * p
            PTree[r1 + 1][c1 + 1] += PTree[r1][c1] * (1 - p)

    option_price = 0
    for r1 in range(N + 1):
        if option_type == 'c':
            if STree[r1][N] > k:
                option_price += PTree[r1][N] * (STree[r1][N] - k)
        if option_type == 'p':
            if STree[r1][N] < k:
                option_price += PTree[r1][N] * (k - STree[r1][N])        

    return option_price * math.exp(-r * T),u,d,p,PTree,STree

def bitcall_Ame(S, k, T, r, vol, N, option_type): #American option
    dt = T / N
    u = math.exp(vol * math.sqrt(dt))
    d = math.exp(-vol * math.sqrt(dt))
    p = (math.exp(r * dt) - d) / (u - d)
    STree = np.zeros((N + 1, N + 1))
    price = np.zeros((N + 1, N + 1))    
    STree[0][0] = S
    for c1 in range(N):
        STree[0][c1 + 1] = STree[0][c1] * u
        for r1 in range(c1 + 1):
            STree[r1 + 1][c1 + 1] = STree[r1][c1] * d

    if option_type == 'c':
        price[:,-1] = np.maximum(STree[:,-1] - k, 0)
    if option_type == 'p':
        price[:,-1] = np.maximum(k - STree[:,-1], 0)

    for c1 in range(N-1,-1,-1):
        for r1 in range(N):
            if option_type == 'c':
                price[r1][c1] = max(STree[r1][c1] - k, (p*price[r1][c1+1] + (1-p)*price[r1+1][c1+1])*math.exp(-r*dt))
            if option_type == 'p':
                price[r1][c1] = max(k - STree[r1][c1], (p*price[r1][c1+1] + (1-p)*price[r1+1][c1+1])*math.exp(-r*dt))

    return price[0][0]

def bitcall_Ame_2(S, k, T, r, vol, N, option_type):
    if option_type == "p":
      option_type = -1
    else:
      option_type = 1
    dt = T / N
    u = np.exp(vol * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    q = 1 - p
    option_values = np.flip(np.maximum(0, option_type * (S * u**np.arange(N+1) * d**(N-np.arange(N+1)) - k)))
    for i in range(N-1, -1, -1):
        option_values = np.maximum(0, np.exp(-r * dt) * (p * option_values[:-1] + q * option_values[1:]))
        underlying_values = np.flip(S * u**np.arange(i+1) * d**(i-np.arange(i+1)))
        early_exercise_values = np.maximum(0, option_type * (underlying_values - k))
        option_values = np.maximum(option_values, early_exercise_values)
    return option_values[0]

if __name__ == '__main__':
    # (a) (b)
    s,k,T,r,vol = 50,52,2,0.05,0.3
    CRR_24,u,d,p = bitcall_Eur(s,k,T,r,vol, 24, 'p')[:4]
    print(f"CRR_24: u = {u:.3f}, d = {d:.3f}, p = {p:.3f}")
    CRR_104,u,d,p = bitcall_Eur(s,k,T,r,vol, 104, 'p')[:4]
    print(f"CRR_104: u = {u:.3f}, d = {d:.3f}, p = {p:.3f}")
    CRR_504,u,d,p = bitcall_Eur(s,k,T,r,vol, 504, 'p')[:4]
    print(f"CRR_504: u = {u:.3f}, d = {d:.3f}, p = {p:.3f}")
    black_scholes = BS_formula(s,k,T,r,vol,'p')
    print()
    print(f"the option value of the Black-Scholes formula is {black_scholes:.3f}")
    print(f"the option value of the CRR model with 24 steps is {CRR_24:.3f}")
    print(f"the option value of the CRR model with 104 steps is {CRR_104:.3f}")
    print(f"the option value of the CRR model with 504 steps is {CRR_504:.3f}")
    print()
    # (e)
    CRR_24_Ame = bitcall_Ame_2(s,k,T,r,vol, 24, 'p')
    CRR_104_Ame = bitcall_Ame_2(s,k,T,r,vol, 104, 'p')
    CRR_504_Ame = bitcall_Ame_2(s,k,T,r,vol, 504, 'p')
    print(f"the American option of the CRR model with 24 steps is {CRR_24_Ame:.3f}")
    print(f"the American option of the CRR model with 104 steps is {CRR_104_Ame:.3f}")
    print(f"the American option of the CRR model with 504 steps is {CRR_504_Ame:.3f}")
    # (c)
    CRR = [bitcall_Eur(s,k,T,r,vol, i, 'p')[0] for i in range(1,253)]
    plt.plot(np.arange(1,253),[black_scholes]*252,"r--")
    plt.plot(np.arange(1,253),CRR,alpha=0.5)
    plt.show()  
    #  (d)
    for i in [6,12,52]:   #compute the terminal stock prices as well as their corresponding probabilities
        terminal_price = bitcall_Eur(50,52,2,0.05,0.3,i,'p')[5][:,-1]
        prob = bitcall_Eur(50,52,2,0.05,0.3,i,'p')[4][:,-1]
        plt.plot(terminal_price,prob,'-o',alpha=(100-i)/100)
    plt.legend(['6 steps','12 steps','52 steps'])
    plt.title('Terminal Stock Prices vs. Probabilities')
    plt.show()

