# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：


#default ver1.0
# l = input("please input the names,use , to seperate")
# name = [s.lower() for s in l]
# print([map(upper(name[0])),name])



# ver1.0 只能指定list然后把首字母大写
# 不能input数据，因为会让多个名字变成一个字符串，然后只实现第一个大写的情况
#l = [input("please input the names,use','to seperate:")]
l = ['adam', 'LISA', 'barT']
#print(l)
#name = [s.lower() for s in l]  #这样写会让用户输入的时候变成分隔的字母
name = [s.lower() for s in l]
#print(name)
def fn(x):
    return x.capitalize()
print(list(map(fn,name)))
