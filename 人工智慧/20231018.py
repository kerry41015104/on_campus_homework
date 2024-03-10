import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


s = 16273.38
k = 16500
t = 14 / 365
r = 0.0166
# vol = 0.2
implied_vol = 0.14134
call = 93.0


def blscall(s, k, t, r, vol):
    d1 = (math.log(s / k) + (r + vol * vol / 2) * t) / (vol * math.sqrt(t))
    d2 = d1 - vol * math.sqrt(t)
    call = s * norm.cdf(d1) - k * math.exp(-r * t) * norm.cdf(d2)
    return call


def bitcall(S, k, T, r, vol, N):
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

    call = 0
    for r1 in range(N + 1):
        if STree[r1][N] > k:
            call += PTree[r1][N] * (STree[r1][N] - k)

    return call * math.exp(-r * T)


CRR_10 = bitcall(s, k, t, r, implied_vol, 10)
CRR_100 = bitcall(s, k, t, r, implied_vol, 100)
CRR_1000 = bitcall(s, k, t, r, implied_vol, 1000)
black_scholes = blscall(s, k, t, r, implied_vol)

ds = 1
delta = (blscall(s + ds, k, t, r, implied_vol) - blscall(s, k, t, r, implied_vol)) / (
    ds
)


print(f"black_scholes誤差: {abs(black_scholes - call)}")
print(f"CRR_10誤差: {abs(CRR_10 - black_scholes)}")
print(f"CRR_100誤差: {abs(CRR_100 - black_scholes)}")
print(f"CRR_1000誤差: {abs(CRR_1000 - black_scholes)}")
print(f"delta: {delta}")
