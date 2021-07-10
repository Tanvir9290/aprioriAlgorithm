import numpy as np
import pandas as pd
import itertools as itertools

minSup = int(input("Enter minimum support\n:- "))

maxLen = 0

df = pd.read_csv('Market_Basket_Optimisation.csv',header=None)
df.fillna(0, inplace=True)

#print (df)

transactions = []
for i in range(0,100):
    transactions.append([str(df.values[i,j]) for j in range(0,4) if str(df.values[i,j])!='0'])

#print (transactions)

count = len(transactions)

def moreCombinations(list_elements,size):
    retComb = []
    length = len(list_elements)
    for i in range(length):
        for j in range(i+1,length):
            temp1 = set(list_elements[i])
            temp2 = set(list_elements[j])
            temp3 = temp1.union(temp2)
            if len(temp3) == size:
                retComb.append(set(list(temp3)))
    
    return retComb

def uniqueCombinations(list_elements):
    l = list(itertools.combinations(list_elements, 2))
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

    retArr = []
    dic = {}
    
    for item in checkArr:
        items = set(item)
        #print(items)
        dic[item] = 0
        
        for transaction in transactions:

            transac = set(transaction)

            if transac.issuperset(items):
                dic[item] += 1
        
        items.clear()
        if dic[item] >= minSup:
            retArr.append(item)
        if dic[item] < minSup:
            del dic[item]
            
    #print (dic)
    #print (retArr)
        #cnt = 0
        #items.clear()
        #transac.clear()
        
    return retArr               
    
for i in transactions:
    if len(i) > maxLen:
        maxLen = len(i)
        
oneComb = uniqueInd(transactions)
#print(oneComb)
twoComb = uniqueCombinations(oneComb)

twoComb = checkMin(twoComb)
print(twoComb)
threeComb = moreCombinations(twoComb,3)
#threeComb = checkMin(threeComb)
print(threeComb)

#twoComb = checkMin(twoComb)
#for i in twoComb:
    #print(set(i))



