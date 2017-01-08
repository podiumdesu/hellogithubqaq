# version1
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:56:42 2016
@author: PetnaKanojo
"""
def yanghui(n):
    l=[1]
    if n==0:
        return l
    else:
        if n!=1:
            x=0
            p=n
            while p-1>0:
                s=yanghui(n-1)[x]+yanghui(n-1)[x+1]
                l.append(s)
                x=x+1
                p=p-1
            else:
                l.append(1)
        else:
            l.append(1)
    return l
i=input('请输入自然数')
t =int(i)
for n in range(t+1):
    print(yanghui(n))



# version2
# 存在问题：代码太长，有点丑，输入1的时候会输出两行。这是问题！！！！
# -*- coding: utf-8 -*-
"""
Created on SUN JAN  8 18:51:10 2017
@author: PetnaKanojo
"""
def triangles(q):
    l = [1]
    yield l
    l = [1,1]
    yield l
    while len(l)<q:
        l =[1]+[l[i]+l[i+1] for i in range(len(l)-1)]+[1]
        yield l

q = int(input("please input a number:"))
# if not isinstance (q,(int)):
#     raise TypeError('bad operand type')
for d in triangles(q):
    print(d)
