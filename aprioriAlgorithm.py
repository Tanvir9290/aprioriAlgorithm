import numpy as np
import pandas as pd
import itertools as itertools

minSup = int(input("Enter minimum support\n:- "))

maxLen = 0

df = pd.read_csv('Market_Basket_Optimisation.csv',header=None)
df.fillna(0, inplace=True)

#print (df)

transactions = []
for i in range(0,200):
    transactions.append([str(df.values[i,j]) for j in range(0,5) if str(df.values[i,j])!='0'])

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
                if temp3 not in retComb:
                    retComb.append(tuple(temp3))
    retComb = set(retComb)
    return list(retComb)

def oneCombMinCheck(checkArray):
    retArr = []
    dict = {}
    for item in checkArray:
        dict[item] = 0
        for transec in transactions:
            if item in transec:
                dict[item] += 1
        if dict[item] < checkMin:
            del dict[item]
    for i in dict.keys():
        retArr.append(i)
    retArr = set(retArr)
    return list(retArr)

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
        if dic[item] < minSup:
            del dic[item]
    for i in dic.keys():
        retArr.append(i)
    #print (dic)
    #print (retArr)
    retArr = set(retArr)  
    return list(retArr)               
    
for i in transactions:
    if len(i) > maxLen:
        maxLen = len(i)
        
oneComb = uniqueInd(transactions)
oneComb = oneCombMinCheck(oneComb)

'''twoComb = uniqueCombinations(oneComb)
twoComb = checkMin(twoComb)
#print(twoComb)
threeComb = moreCombinations(twoComb,3)
print(threeComb)
threeComb = checkMin(threeComb)
print(threeComb)
fourComb = moreCombinations(threeComb,4)
print(fourComb)'''
'''fiveComb = moreCombinations(threeComb,5)
print(fiveComb)
'''
#twoComb = checkMin(twoComb)
#for i in twoComb:
    #print(set(i))



