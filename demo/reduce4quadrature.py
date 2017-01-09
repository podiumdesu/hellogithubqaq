#Python提供的sum()函数可以接受一个list并求和，
#请编写一个prod()函数，可以接受一个list并利用reduce()求积：

# default ver1.0
# 这个完全就是错的，根本就不懂reduce的用法
# from functools import reduce
# def prod(sum,y):
#     sum = sum*y
#     return sum
# l = [input("please input a list")]
# for y in l:
#     print(reduce(prod,y))

# default ver2.0
# 不能输入list
# 错误原因：input的时候是字符串，即使是变成[]里面的内容也仍然是字符串
# 迭代以后x的值也是一个个字符串，没找到很好的解决方法
# from functools import reduce
# def prod(x,y):
#     return x*y
# l = [input("please input a list")]
# #l = l.split(",")
# print(l)
# numberlist = [x for x in l]
# print(numberlist)
# print(reduce(prod,numberlist))



# ver1.0
from functools import reduce
def prod(x,y):
    return x*y
l = [1,2,3,5,6,7,8]
print(reduce(prod,l))
