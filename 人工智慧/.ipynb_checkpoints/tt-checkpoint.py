import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import yfinance as yf
data = yf.download('AAPL', start="2023-01-01", end="2023-08-05")
prices = data["Adj Close"].dropna(how="all")

e = np.linspace(0,1,num=1024,endpoint=True)
f = np.linspace(1,50,num=1024,endpoint=True)
gg = np.linspace(0,2*np.pi,num=1024,endpoint=True)
d = [138,139,140,141,142,143,144,145,146,147]

def fitness(prices,D, E, F, G):
  A1 = np.zeros((D+1, 3),dtype="float")
  for i in range(D+1):  #147
    if i!=D:
      A1[i,0] = 1
      A1[i,1] = (D - i) ** E
      A1[i,2] = (D - i) ** E * (np.cos(F * np.log(D - i) + G))
    else: 
      A1[i,0] = 1
      A1[i,1] = 0
      A1[i,2] = 0
  b1 = np.log(np.array(prices[:D+1]))
  ABC = np.linalg.lstsq(A1, b1, rcond=None)[0]
  A = ABC[0]
  B = ABC[1]
  DD = ABC[2]
  C = DD / B
  MSE = [ (np.log(prices[j]) - (A+B*(D - j) ** E+DD*(D - j) ** E * (np.cos(F * np.log(D - j) + G))))**2 if j<D else (np.log(prices[j]) - A)**2 for j in range(D+1)]
  
  return np.sum(MSE),ABC


    


p = 10000
r = 0.01
m = 1000
g = 10
survive = round(p * r)

pop = np.random.randint(0, 2, (p, 34))
for i in range(p):
  gene_s = pop[i, :]
  while np.sum(2 ** np.array(range(4)) * gene_s[:4]) > 9:
    pop[i, :4] = np.random.randint(0, 2, (1, 4))

fit = np.zeros((p, 1))
for generation in tqdm(range(g)):
    for i in range(p):
        gene = pop[i, :]
        D = d[np.sum(2 ** np.array(range(4)) * gene[:4])]
        E = e[np.sum(2 ** np.array(range(10)) * gene[4:14])]
        F = f[np.sum(2 ** np.array(range(10)) * gene[14:24])]
        G = gg[np.sum(2 ** np.array(range(10)) * gene[24:34])]
        fit[i],_ = fitness(prices,D, E, F, G)
    sortf = np.argsort(fit[:, 0])
    pop = pop[sortf, :]
    for i in range(survive, p):
        fid = np.random.randint(0, survive)
        mid = np.random.randint(0, survive)
        while mid == fid:
          mid = np.random.randint(0, survive)
        count=0
        while count==0 or np.sum(2 ** np.array(range(4)) * pop[i,:4]) > 9:
          count+=1
          mask = np.random.randint(0, 2, (1, 34))
          son = pop[mid, :].copy()
          father = pop[fid, :]
          son[mask[0, :] == 1] = father[mask[0, :] == 1]
          pop[i, :] = son
    for i in range(m):
        mr = np.random.randint(survive, p)
        mc = np.random.randint(0, 34)
        pop[mr, mc] = 1 - pop[mr, mc]
        while np.sum(2 ** np.array(range(4)) * pop[mr,:4]) > 9:
          pop[mr, mc] = 1 - pop[mr, mc]
          mc = np.random.randint(0, 4)
          pop[mr, mc] = 1 - pop[mr, mc]

for i in range(p):
  gene = pop[i, :]
  D = d[np.sum(2 ** np.array(range(4)) * gene[:4])]
  E = e[np.sum(2 ** np.array(range(10)) * gene[4:14])]
  F = f[np.sum(2 ** np.array(range(10)) * gene[14:24])]
  G = gg[np.sum(2 ** np.array(range(10)) * gene[24:34])]
  fit[i],ABC = fitness(prices,D, E, F, G)
sortf = np.argsort(fit[:, 0])
pop = pop[sortf, :]

gene = pop[0, :]


A = ABC[0]
B = ABC[1]
D = ABC[2]
C = D / B
Tc = d[np.sum(2 ** np.array(range(4)) * gene[:4])]
E = e[np.sum(2 ** np.array(range(10)) * gene[4:14])]
F = f[np.sum(2 ** np.array(range(10)) * gene[14:24])]
G = gg[np.sum(2 ** np.array(range(10)) * gene[24:34])]
print("A:", A, " B:", B, " C:", C, " Tc:", Tc," 貝他:", E," w:", F," phi:", G)
print("-------------------------------------------------------------------------------------")
MSE = [ (np.log(prices[j]) - (A+B*(Tc - j) ** E+(B*C)*(Tc - j) ** E * (np.cos(F * np.log(Tc - j) + G))))**2 if j<Tc else (np.log(prices[j]) - A)**2 for j in range(Tc+1)]
y_axis = [ (A+B*(Tc - j) ** E+(B*C)*(Tc - j) ** E * (np.cos(F * np.log(Tc - j) + G))) if j<Tc else A for j in range(Tc+1)]
print("最小MSE:",np.sum(MSE))

plt.plot(np.arange(0,Tc+1),np.log(np.array(prices[:Tc+1])),label="real data")
plt.plot(np.arange(0,Tc+1),y_axis,label="LPPL model")
plt.legend()
plt.title("LPPL model for AAPL")
plt.xlabel("time")
plt.ylabel("log(price)")
plt.show()