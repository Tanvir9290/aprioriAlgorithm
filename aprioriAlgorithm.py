import numpy as np
import pandas as pd
import itertools as itertools

minSup = int(input("Enter minimum support\n:- "))
maxLen = 0
CombRepeat = 0
itemsCombRepeat = {}

#import dataset
df = pd.read_csv('Market_Basket_Optimisation.csv',header=None)
df.fillna(0, inplace=True)

#convert dataset into array
transactions = []
for i in range(0,500):
    transactions.append([str(df.values[i,j]) for j in range(0,5) if str(df.values[i,j])!='0'])


def get_power_set(s):
  power_set=[[]]
  for elem in s:
    # iterate over the sub sets so far
    for sub_set in power_set:
      # add a new subset consisting of the subset at hand added elem
      power_set=power_set+[list(sub_set)+[elem]]
  return power_set

#creates three or more combination of item pair
def moreCombinations(list_elements,size):
    retComb = []
    length = len(list_elements)
    for i in range(length):
        for j in range(i+1,length):
            temp1 = set(list_elements[i])
            temp2 = set(list_elements[j])
            temp3 = temp1.union(temp2)
            temp3 = sorted(temp3)
            
            if len(temp3) == size:
                if tuple(temp3) not in retComb:
                    retComb.append(tuple(temp3))
    retComb = set(retComb)
    return list(retComb)

#checks minimum support for one pair of items
def oneCombMinCheck(checkArray):
    
    retArr = []
    dict = {}
    for item in checkArray:
        dict[item] = 0
        global itemsCombRepeat
        itemsCombRepeat[item] = 0

        for transec in transactions:
            if item in transec:
                dict[item] += 1

                itemsCombRepeat[item] += 1
        
        if dict[item] < minSup:
            del dict[item]
    
    for i in dict.keys():
        retArr.append(i)
    retArr = set(retArr)
    return list(retArr)

#creates combination of two pair of items
def uniqueCombinations(list_elements):
    l = list(itertools.combinations(list_elements, 2))
    s = set(l)
    return list(s)

#returns single pair of items from transaction
def uniqueInd(mainArr):
    comArr = []
    for i in mainArr:
        for j in i:
            if j not in comArr:
                comArr.append(j)
    comArr = set(comArr)
    return list(comArr)

#checks combination of items minimum support 
def checkMin(checkArr):
    retArr = []
    dic = {}
    
    for item in checkArr:
        items = set(item)
        dic[item] = 0
        global itemsCombRepeat
        itemsCombRepeat[item] = 0
        for transaction in transactions:
            transac = set(transaction)
            if transac.issuperset(items):
                dic[item] += 1

                itemsCombRepeat[item] += 1
   
        if dic[item] < minSup:
            del dic[item]
        if itemsCombRepeat[item] == 0:
            del itemsCombRepeat[item]

    for i in dic.keys():
        retArr.append(i)

    retArr = set(retArr)  
    return list(retArr)  
             
#determine maximum pair available in transaction   
for i in transactions:
    if len(i) > maxLen:
        maxLen = len(i)
        
oneComb = uniqueInd(transactions)
oneComb = oneCombMinCheck(oneComb)
#print(oneComb)
twoComb = uniqueCombinations(oneComb)
twoComb = checkMin(twoComb)
#print(twoComb)
resultSet= []
resultSet.append(oneComb)
resultSet.append(twoComb)

#Creates pair of items and checks minimum support for that pair at the same time
for i in range(3,maxLen+1):
    tempComb = moreCombinations(resultSet[i-2],i)
    
    if len(tempComb) >= 1:
        tempComb = checkMin(tempComb)
        if len(tempComb) == 0:
            break
        else:
            resultSet.append(tempComb)
    else:
        break

print("Our maximum pair of items which meets minimum support")
#print(resultSet[-1])

for i in resultSet[-1]:
    print(sorted(get_power_set(i)))

print(itemsCombRepeat)

