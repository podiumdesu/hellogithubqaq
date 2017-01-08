# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:56:45 2016

@author: user
"""

def midsearch(a,m):
    min=0
    max=len(a)-1
    while min <=max:
        mid =int((min+max)/2)
        
        if a[mid]>m:
            max =mid-1
        elif a[mid]<m:
            min =mid+1
    #如果没有+——1，会出现最后一位或者第一位数查找不到的问题
    #这个加一还是减一要算的。。。。。
        else:
            return mid+1
    return -1

print(midsearch([1,3,5,8,10,14,17],1))
print(midsearch([1,2,3,4,5,6,7,8,9,10,11,12,15,16,18],18))
#运行函数时要加上print
            