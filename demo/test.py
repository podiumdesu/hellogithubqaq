#print("hello,world!")

#print("please input your name")
#name=input()
#print("hello,",name)

print('''line1
line2
line3''')

# 用来计算成绩的增长比
# 小明成绩从72提升成今年的85，计算成绩提高的百分点，并用字符串格式化显示出'xx.x%'

name=input("please input your name")
first_score=int(input("please input your score of last semester"))
next_score=int(input("please input your score of this semester"))
percent=(next_score-first_score)/first_score*100
#print("%s, your score has improved %.1f %" % (name,percent))
print("%s, your score has improved %.1f %%" % (name,percent))  #注意转义符号的使用啊!!!!




# 计算100以内所有奇数之和
i =1
sum =0
num=int(input("please input a number"))  #注意要加上引号！！！！！
while i<=num:
  sum=sum+i
  i=i+2
print(sum)


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


# 利用递归函数移动汉诺塔:
# 这太可怕了，我理解问题复杂化以为是“模拟整个过程，再导出步骤记录”
# 查具体的算法，这个汉诺塔问题应该可以抽象为用位置参数模拟搬运。。
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)   # 这一步目前还没有看懂！！！！！！！
    print('move', a, '-->', c)
    move(n-1, b, a, c)

print(move(4,'A','B','C'))
