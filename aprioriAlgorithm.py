import numpy as np
import pandas as pd
import itertools as itertools

minSup = int(input("Enter minimum support\n:- "))

maxLen = 0

df = pd.read_csv('Market_Basket_Optimisation.csv',header=None)
df.fillna(0,inplace=True)

transactions = []
for i in range(0,10):
    transactions.append([str(df.values[i,j]) for j in range(0,4) if str(df.values[i,j])!='0'])

count = len(transactions)

def uniqueCombinations(list_elements,comb):
    l = list(itertools.combinations(list_elements, comb))
    s = set(l)
    return list(s)

def uniqueInd(mainArr):
    comArr = []
    for i in mainArr:
        for j in i:
            if j not in comArr:
                comArr.append(j)
    
    return comArr

def checkMin(checkArr):
    lenArr = len(checkArr)
    items = set()
    transac = set()
    comp = False
    cnt = 0
    
    for i in range(0,lenArr):
        items.add(checkArr[i])
        for j in range(0,count):
            transac.add(transactions[j])
            comp = transac.issuperset(items)
            if comp is True:
                cnt += 1
            transac.clear()
        if cnt < minSup:
            checkArr.pop(i)
        
        cnt = 0
        items.clear()
        transac.clear()
        
    return checkArr               
    
for i in transactions:
    if len(i) > maxLen:
        maxLen = len(i)
        
oneComb = uniqueInd(transactions)
oneCombMin = checkMin(oneComb)

