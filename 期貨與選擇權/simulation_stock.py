import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt


def simulation(nn, NN, T=1, u=0.13, sigma=0.2, st_price=100,rebalance=1):
    n = int(int(nn * T) / rebalance)
    dt = rebalance / n
    N = NN

    out = np.zeros((n + 1, N))
    out[0, :] = st_price

    random_error = np.random.normal(0, 1, (n, N))

    for j in range(n):
        ss = u * dt * out[j, :] + sigma * out[j, :] * random_error[j, :] * np.sqrt(dt)
        out[j + 1, :] = out[j, :] + ss

    return out


def simulation_plot(nn, NN):
    for i in range(NN):
        plt.plot(np.linspace(0, 1, num=nn + 1), simulation(nn, NN)[:, i])
        plt.title(f"time interval of t is 1/{nn}")
    plt.show()

if __name__ == "__main__":
    simulation_plot(52, 10)
    simulation_plot(12, 10)
    simulation_plot(252, 10)
    for i in [1000, 10000, 100000]:
        plt.hist(simulation(252, i)[-1, :], bins=100)
        plt.title(f"the number of sample paths is {i}")
        plt.show()
# # a小題------------------------------------------------------------------------------------------------
# simulation_plot(52, 10)
# # b小題------------------------------------------------------------------------------------------------
# simulation_plot(12, 10)
# simulation_plot(252, 10)

# # c小題------------------------------------------------------------------------------------------------
# for i in [1000, 10000, 100000]:
#     plt.hist(simulation(252, i)[-1, :], bins=100)
#     plt.title(f"the number of sample paths is {i}")
#     plt.show()
