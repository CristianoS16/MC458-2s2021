#Cristiano Sampaio Pinheiro RA:256352
import math
def computeChange(coins, nCoins, value):
    aux = [math.inf]*(value+min(coins))
    aux[0]=0
    newcoins = [0]
    newcoins.extend(coins)
    for i in range(0,value+min(coins)):
        for j in range(0,nCoins):
            if(i>=coins[j]):
                aux[i]=min(aux[i-coins[j]]+1,aux[i])
    if(aux[value]!=math.inf):
        return  value, aux[value]
    else:
        for i in range(value, value+min(coins)):
            if(aux[i]!=math.inf):
                return i, aux[i]
    
value = int(input())
coinsNumber = int(input())
coins = [int(n) for n in input().split()]

change = computeChange(coins,coinsNumber,value)

print(change[0], change[1])
