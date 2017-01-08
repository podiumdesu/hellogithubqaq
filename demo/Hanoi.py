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
