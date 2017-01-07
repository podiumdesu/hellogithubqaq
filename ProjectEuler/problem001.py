# coding = utf-8
#No.1  1000以内所有可以整除3和5的数的和
#If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def compute(i):
    ans = 0
    for x in range(i):
        if x %3==0 or x%5==0:
            ans = ans + x
    return ans
print(compute(1000))
# 这段辣鸡代码跑不起来，一跑内存直接上99%，气。
# L=[]
# while i<1000
#     if i % 3 ==0 or i % 5 ==0:
#         L.append[i]
#     else:
#         i=i+1
# sum = 0
# for num in L:
#     sum = sum+num
# print(sum)
# 所以不能一个个数组元素添加，必须要通过挑选吧
