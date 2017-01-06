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
