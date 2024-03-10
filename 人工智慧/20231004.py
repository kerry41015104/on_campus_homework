import numpy as np
import matplotlib.pyplot as plt
import matplotlib

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
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
PUTprice = {
    16100: 114,
    16200: 149,
    16300: 194,
    16400: 246,
    16500: 308,
    16600: 384,
    16700: 466,
    16800: 555,
}
ST = np.arange(15800, 17200)


def OptionProfit(pos):
    callposition = pos[0]
    putposition = pos[1]
    profit = np.zeros(ST.shape)
    for position in callposition:
        K = position[0]
        N = position[1]
        C = CALLprice[K]
        profit = profit + (np.maximum(ST - K, 0) - C) * N
    for position in putposition:
        K = position[0]
        N = position[1]
        P = PUTprice[K]
        profit = profit + (np.maximum(K - ST, 0) - P) * N
    return profit


pos1 = [[], [[16400, -1], [16600, -1], [16500, 2]]]
p1 = OptionProfit(pos1)
pos2 = [[[16300, -1], [16700, -1], [16500, 2]], []]
p2 = OptionProfit(pos2)
pos3 = [[[16500, 1]], [[16500, 1]]]
p3 = OptionProfit(pos3)
pos4 = [[[16400, 1]], [[16600, 1]]]
p4 = OptionProfit(pos4)
pos5 = [[[16300, 1]], [[16700, 1]]]
p5 = OptionProfit(pos5)
plt.xlabel("到期現貨價格", loc="right")
plt.ylabel("總損益", loc="top", rotation=360)
plt.plot([ST[0], ST[-1]], [0, 0], "k--")
plt.plot(ST, p1, "b-", label="Butterfly賣權空頭")
plt.plot(ST, p2, "r-", label="Butterfly買權空頭")
plt.plot(ST, p3, "g-", label="Straddle")
plt.plot(ST, p4, "y-", label="Strangle小")
plt.plot(ST, p5, "m-", label="Strangle大")
plt.legend(loc="best", title="第一題")
plt.show()  



a = [value for key, value in CALLprice.items()]
b = [value for key, value in PUTprice.items()]
c = [key for key, value in PUTprice.items()]
d = [c - p + k for c, p, k in zip(a, b, c)]  # 查看差距最大兩線
pos1 = [[[16200, 1]], [[16200, -1]]]
p1 = OptionProfit(pos1)
pos2 = [[[16800, 1]], [[16800, -1]]]
p2 = OptionProfit(pos2)
print(p2[0] - p1[0])  # 13.5
plt.xlabel("到期現貨價格", loc="right")
plt.ylabel("總損益", loc="top", rotation=360)
plt.plot([ST[0], ST[-1]], [0, 0], "k--")
plt.plot(ST, p1, "b-", label="LongCShortP16200")
plt.plot(ST, p2, "r-", label="LongCShortP16800")
plt.legend(loc="best", title="第二題")
plt.show()

pos1 = [[[16100, -1]], []]
p1 = OptionProfit(pos1)
pos2 = [[[16800, -1]], []]
p2 = OptionProfit(pos2)
pos3 = [[], [[16100, 1]]]
p3 = OptionProfit(pos3)
pos4 = [[], [[16800, 1]]]
p4 = OptionProfit(pos4)
pos5 = [[[16600, 1], [16400, -1]], []]
p5 = OptionProfit(pos5)
pos6 = [[[16700, 1], [16300, -1]], []]
p6 = OptionProfit(pos6)
plt.xlabel("到期現貨價格", loc="right")
plt.ylabel("總損益", loc="top", rotation=360)
plt.plot([ST[0], ST[-1]], [0, 0], "k--")
plt.plot(ST, p1, "b-", label="ShortC 16100")
plt.plot(ST, p2, "r-", label="ShortC 16800")
plt.plot(ST, p3, "g-", label="LongP 16100")
plt.plot(ST, p4, "y-", label="LongP 16800")
plt.plot(ST, p5, "m-", label="空頭價差小")
plt.plot(ST, p6, "c-", label="空頭價差大")
plt.legend(loc="best", title="第三題")
plt.show()
