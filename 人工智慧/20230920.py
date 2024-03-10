
T = int(input())
if T > 100 or T < 1:
    exit()
for t in range(T):
    N = int(input())
    if N > 1000 or N <1: exit()
    buy = []
    sell = []
    stockprice = -1
    for n in range(N):
        str = input()
        strlist = str.split()
        share = int(strlist[1])
        price = int(strlist[-1])
        if strlist[0]=="buy":
            while len(sell)>0:
                order = sell[0]
                if order[0]>price:
                    break
                dealamount = min(order[1],share)
                stockprice = order[0]
                order[1] -= dealamount
                share -= dealamount
                if order[1]==0:
                    sell.pop(0)
                if share==0:
                    break
            if share>0:
                i = 0
                while(i<len(buy) and price<buy[i][0]):
                    i+=1
                if(i<len(buy) and price==buy[i][0]):
                    buy[i][1] += share
                else:
                    buy.insert(i,[price,share])
        elif strlist[0]=="sell":
            while len(buy)>0:
                order = buy[0]
                if order[0]<price:
                    break
                dealamount = min(order[1],share)
                stockprice = price
                order[1] -= dealamount
                share -= dealamount
                if order[1]==0:
                    buy.pop(0)
                if share==0:
                    break
            if share>0:
                i = 0
                while(i<len(sell) and price>sell[i][0]):
                    i+=1
                if(i<len(sell) and price==sell[i][0]):
                    sell[i][1] += share
                else:
                    sell.insert(i,[price,share])
        else: exit()    
        if not sell:
            print('-',end=' ')
        else:
            print(sell[0][0],end=' ')
        if not buy:
            print('-',end=' ')
        else:
            print(buy[0][0],end=' ')
        if stockprice==-1:
            print('-')
        else:
            print(stockprice)
            
            
            
            
            
            
            
            