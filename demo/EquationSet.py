# 定义一个函数quadratic(a,b,c)，接收3个参数，返回一元二次方程
# 这个函数之前军训的时候写过，当时写了整整两个小时，还借鉴了很多的代码。当时完全不会，写了很多很多bug出来
#这次大概只写了半小时吧，而且也没有很多的bug，算是进步吧

import math
def quadratic(a,b,c):
    if not isinstance(a,(int)):
        raise TypeError('please input an integer')  #这里的参数检查好像没有派上用场
    if not isinstance(b,(int)):
        raise TypeError('please input an integer')
    if not isinstance(c,(int)):
        raise TypeError('please input an integer')
    delt = b*b-4*a*c
    if a == 0:       # 检查是否相等的时候不能用=，要用==!!!!!!!!!!!!!!!!!
        if b == 0:
            if c==0:
                return 'x为任意实数'
            else:
                return '该方程无解'
        else:
            x1 = x2 = -c/b
            return x1,x2   # 这里返回多个值的时候tuple很难看
    else:
        if delt > 0:
            x1 = (-b+math.sqrt(delt))/(2*a)   # 注意括号的使用!!!!!!!!!!!
            x2 = (-b-math.sqrt(delt))/(2*a)
            return x1,x2
        elif delt == 0:
            x1 = x2 = (-b)/(2*a)
            return x1,x2
        else:
            return "无实数根"

a = int(input('please input a(ax^2+bx+c=0)'))
b = int(input('please input b(ax^2+bx+c=0)'))
c = int(input('please input c(ax^2+bx+c=0)'))
print (quadratic(a,b,c))
