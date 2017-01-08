# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:32:24 2016

@author: user
"""

#numbers = []
#n=input('请输入数字')
#while n!='':
#    numbers.append(n)
#    n = input() 
#？？？？？不知道该怎么做到input一串数字然后排序


numbers = [1,3,2,14,10]
#def bubble(numbers):
for i in range(len(numbers)):
    for j in range(i):
        if numbers[j] > numbers[i]:
            numbers[j], numbers[i] = numbers[i], numbers[j]
        #print (numbers) print如果放在这里会输出每次进行排序的结果
print(numbers)
        #return numbers
