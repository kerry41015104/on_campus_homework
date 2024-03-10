import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import yfinance as yf
data = yf.download('AAPL', start="2023-01-01", end="2023-08-05")
prices = data["Adj Close"].dropna(how="all")    

e = np.linspace(0,1,num=1024,endpoint=True) #beta
f = np.linspace(1,50,num=1024,endpoint=True) #omega
gg = np.linspace(0,2*np.pi,num=1024,endpoint=True) # phi
d = [138,139,140,141,142,143,144,145,146,147] #tc



def logPt(tc, A, B, DD, beta, omega, phi):
    t = np.arange(0, tc).reshape((tc, 1))
    predict = A + B*(tc-t)**beta + DD*(tc-t)**beta*(np.cos(omega*np.log(tc-t)+phi))
    predict = np.append(predict, [[A]], axis=0)
    return predict

def fitness(prices,tc, beta, omega, phi):
  A1 = np.zeros((tc, 3))
  t = np.arange(0,tc).reshape((tc, 1))
  A1[t, 0] = 1
  A1[t, 1] = (tc - t) ** beta
  A1[t, 2] = (tc - t) ** beta * (np.cos(omega * np.log(tc - t) + phi))
  A1 = np.append(A1,[[1,0,0]],axis=0)
  b1 = np.log(np.array(prices[:tc+1]))
  ABC = np.linalg.lstsq(A1, b1, rcond=None)[0]
  A = ABC[0]
  B = ABC[1]
  DD = ABC[2]
  MSE = np.sum((logPt(tc, A, B, DD, beta, omega, phi) - b1.reshape((tc+1, 1))) ** 2)
  return MSE,ABC

def gene2coef(gene):  
    tc = d[np.sum(2 ** np.array(range(4)) * gene[:4])]
    beta = e[np.sum(2 ** np.array(range(10)) * gene[4:14])]
    omega = f[np.sum(2 ** np.array(range(10)) * gene[14:24])]
    phi = gg[np.sum(2 ** np.array(range(10)) * gene[24:34])]
    return tc, beta, omega, phi
    
def plot_results(prices, predictExp, title):
    plt.plot(np.arange(0, tc + 1), np.array(prices[:tc + 1]), label="Real data")
    plt.plot(np.arange(0, tc + 1), predictExp, label="LPPL model")
    plt.legend()
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.show()

popNum = 10000
survive_rate = 0.01
mutationNum = 2000
generationNum = 100
mse_history = np.zeros(generationNum)
survive = round(popNum * survive_rate)
np.random.seed(seed=10)
pop = np.random.randint(0, 2, (popNum, 34))
for i in range(popNum):
  gene_s = pop[i, :]
  while np.sum(2 ** np.array(range(4)) * gene_s[:4]) > 9:
    pop[i, :4] = np.random.randint(0, 2, (1, 4))

fit = np.zeros((popNum, 1))
for generation in tqdm(range(generationNum)):
    for i in range(popNum):
        gene = pop[i, :]
        tc, beta, omega, phi = gene2coef(gene)
        fit[i],_ = fitness(prices,tc, beta, omega, phi)
    sortf = np.argsort(fit[:, 0])
    pop = pop[sortf, :]
    # 紀錄目前最佳的 MSE
    mse_history[generation] = np.min(fit[:, 0])
    for i in range(survive, popNum):
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
    for i in range(mutationNum):
        mr = np.random.randint(survive, popNum)
        mc = np.random.randint(0, 34)
        pop[mr, mc] = 1 - pop[mr, mc]
        while np.sum(2 ** np.array(range(4)) * pop[mr,:4]) > 9:
          pop[mr, mc] = 1 - pop[mr, mc]
          mc = np.random.randint(0, 4)
          pop[mr, mc] = 1 - pop[mr, mc]

for i in range(popNum):
  gene = pop[i, :]
  tc, beta, omega, phi = gene2coef(gene)
  fit[i],ABC = fitness(prices,tc, beta, omega, phi)
sortf = np.argsort(fit[:, 0])
pop = pop[sortf, :]

gene = pop[0, :]
tc, beta, omega, phi = gene2coef(gene)
MSE,ABC = fitness(prices,tc, beta, omega, phi)
A = ABC[0]
B = ABC[1]
DD = ABC[2]
C = DD / B

print("A:", A, " B:", B, " C:", C)
print()
print(" Tc:", tc," 貝他:", beta," w:", omega," phi:", phi)
print("-------------------------------------------------------------------------------------")
predict = logPt(tc, A, B, DD, beta, omega, phi)
predictExp = np.exp(predict[:])
MSE_ture = np.sum((np.array(prices[:tc+1]).reshape((tc+1,1)) - predictExp) ** 2)  
#print("最小MSE:",MSE)
print("真實MSE:",MSE_ture)

plot_results(prices, predictExp, "Final LPPL Model Results")

plt.plot(np.arange(1, generationNum + 1), mse_history, marker='o')
plt.title("MSE Evolution Over Generations")
plt.xlabel("Generation")
plt.ylabel("Mean Squared Error (MSE)")
plt.show()