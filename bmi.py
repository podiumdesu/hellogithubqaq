# -*- coding: utf-8 -*-
h =input('请输入你的身高（单位为米）')
w =input('请输入你的体重（单位为kg）')
bmi = float(w)/(float(h)*float(h))
#bmi =float(int(w))/(float(int(h)*float(int(h)))
#float(raw_input("enter a float: "))
if bmi <18.5:
  print('过轻')
elif bmi >= 18.5 and bmi < 25:
  print('正常')
elif bmi >=25 and bmi < 28:
  print('过重')
elif bmi >=28 and bmi < 32:
  print('肥胖')
else:
  print('严重肥胖')
  
