import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


s = 16273.38
k = 16500
t = 14 / 365
r = 0.0166
# vol = 0.2
call = 93.0

CALLprice = {
    16100: 293,
    16200: 236,
    16300: 177,
    16400: 131,
    16500: 93,
    16600: 64,
    16700: 43.5,
    16800: 28.5,
}


def blscall(s, k, t, r, vol):
    d1 = (math.log(s / k) + (r + vol * vol / 2) * t) / (vol * math.sqrt(t))
    d2 = d1 - vol * math.sqrt(t)
    call = s * norm.cdf(d1) - k * math.exp(-r * t) * norm.cdf(d2)
    return call


def BisectionBLS(s, k, t, r, call):
    left = 0.000001
    right = 1
    while right - left > 0.00001:
        mid = (left + right) / 2
        if (blscall(s, k, t, r, mid) - call) * (blscall(s, k, t, r, left) - call) < 0:
            right = mid
        else:
            left = mid
    return (left + right) / 2

# n: 時間間隔數, m: 模擬次數

def Monte_Carlo(S,T,r,vol,N,M):
    dt = T/N
    St = np.zeros((M,N+1))
    St[:,0] = S
    for i in range(N):
        St[:,i+1] = np.multiply(St[:,i],np.exp((r-0.5*vol*vol)*dt+vol*np.random.normal(0,1,(M,))*math.sqrt(dt)))
    return St

def error(N=100, M=1000):
    tt=[]
    for i in range(10):
        ST = Monte_Carlo(s,t,r,vol,N,M)
        call1 = np.mean(np.maximum(ST[:,-1] - k, 0))*math.exp(-r*t)
        tt.append(abs(call1-93.0))
    return  np.mean(tt)

vol = BisectionBLS(s, k, t, r, call)
print("第一題:", vol)
print('第二題:', error())

nn=[ error(N = i) for i in range(10,210,10)]
mm = [error(M = i) for i in range(500,3000,100)]
plt.xlabel("N or M numbers", loc="right")
plt.ylabel("error", loc="top")
plt.plot(np.arange(10,210,10), nn, "b-")
plt.show()

plt.xlabel("N or M numbers", loc="right")
plt.ylabel("error", loc="top")
plt.plot(np.arange(500,3000,100), mm, "r-")
plt.show()

y = []
x = []
for key, value in CALLprice.items():
    y.append(BisectionBLS(s, key, t, r, value))
    x.append(key)
plt.xlabel("strike price", loc="right")
plt.ylabel("Implied volatility", loc="top")
plt.plot(x, y, "b-")
plt.show()

#plt.plot(ST.transpose())
#plt.show()

