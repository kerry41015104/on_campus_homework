import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def Monte_Carlo(S,T,r,vol,N,M): #N is the number of steps, M is the number of paths
    dt = T/N
    St = np.zeros((M,N+1))
    St[:,0] = S
    np.random.seed(48)
    for i in range(N):
        St[:,i+1] = np.multiply(St[:,i],np.exp((r-0.5*vol*vol)*dt+vol*np.random.normal(0,1,(M,))*math.sqrt(dt)))
    return St

def BS_formula(s, k, t, r, vol,option_type):
    d1 = (math.log(s / k) + (r + vol * vol / 2) * t) / (vol * math.sqrt(t))
    d2 = d1 - vol * math.sqrt(t)
    if option_type == 'c':
        price = s * norm.cdf(d1) - k * math.exp(-r * t) * norm.cdf(d2)
    else:
        price = k * math.exp(-r * t) * norm.cdf(-d2) - s * norm.cdf(-d1) 
    return price,norm.cdf(d1)

def Option_price(S,K,T,r,vol,N,M,option_type):
    ST = Monte_Carlo(S,T,r,vol,N,M)
    if option_type == 'c':
        std_payoff = np.std(np.maximum(K - ST[:,-1], 0)*math.exp(-r*T))
        price = np.mean(np.maximum(ST[:,-1] - K, 0))*math.exp(-r*T)
    else:
        std_payoff = np.std(np.maximum(K - ST[:,-1], 0)*math.exp(-r*T))
        price = np.mean(np.maximum(K - ST[:,-1], 0))*math.exp(-r*T)
    return price,std_payoff,ST

def C_I(ci,u,std_payoff,M):
    standard_error = std_payoff/math.sqrt(M)
    CI_u= u + norm.ppf((1+ci)/2)*standard_error
    CI_l= u + norm.ppf((1-ci)/2)*standard_error
    return standard_error,CI_u,CI_l


if __name__ == "__main__":
    # Part 1 Standard Error and Number of Trials
    all_terminal_values = []
    for i in [100, 10000, 1000000]:
        price,std_payoff,ST = Option_price(50,52,2,0.05,0.3,1,i,'p')
        standard_error,CI_u,CI_l = C_I(0.95,price,std_payoff,i)
        print(f"the number of trials is {i}, the option_price is {price:.3f}, the standard error is {standard_error:.6f}")
        print(f"the confidence interval is [{CI_l:.3f}, {CI_u:.3f}]")
        print("----------------------------------------------------------")
        all_terminal_values.append(ST[:, -1])
    print("the option value of the Black-Scholes formula is","{:.3f}".format(BS_formula(50,52,2,0.05,0.3,'p')))
    print()
    print()
    fig, axes = plt.subplots(len(all_terminal_values), 1, figsize=(8, 12))
    for i in range(len(all_terminal_values)):
        axes[i].hist(all_terminal_values[i], bins=100)
        axes[i].set_title(f"the number of sample paths {len(all_terminal_values[i])}")
    plt.subplots_adjust(hspace=0.5, bottom=0.1)
    plt.show()

    #Part 2 Standard Deviation of Estimated Option Values
    Option_price_500 = np.zeros((502,3))
    k=0
    for i in [100, 10000, 1000000]:
        for j in range(500):
            price,_,_ = Option_price(50,52,2,0.05,0.3,1,i,'p')
            Option_price_500[j,k] = price
        Option_price_500[j+1,k] = np.mean(Option_price_500[:500,k])
        Option_price_500[j+2,k] = np.std(Option_price_500[:500,k])
        k+=1

    df = pd.DataFrame(Option_price_500,columns=['100','10000','1000000'])
    print(df.head(30))
    print()
    print(f"under 100 (NP) the means is {df.iloc[-2,0]} and standard deviations is {df.iloc[-1,0]}")
    print(f"under 10000 (NP) the means is {df.iloc[-2,1]} and standard deviations is {df.iloc[-1,1]}")
    print(f"under 1000000 (NP) the means is {df.iloc[-2,2]} and standard deviations is {df.iloc[-1,2]}")