MENTION IN PYTHON
==

### 第一个文本编辑器
* #### 直接运行py文件（linux下）
  1. 在`.py`文件的第一行加上一个特殊的注释
      ```py
      #!/usr/bin/env python3

      print("hello,world")
      ```
  2. 通过命令给`hello.py`以执行权限
      ```py
      $ chmod a+x hello.py
      ```
  3. 直接运行即可

### python基础
* 数据类型和变量
  * 整数
    1. 十六进制用`0x`前缀和0-9，a-f表示，例如`0xff00`
  * 浮点数
    1. 1.23*10^9就是`1.23e9`
  * 字符串（是以单引号`'`或者双引号`"`括起来的任意文本。

    1. 转义字符`\`

      `I \'m \"ok\"!`

       PS:`\n`换行，`\t`制表符，`\\`转义自身
    2. 字符串里面有很多字符需要转义。使用`r''`表示`''`内部字符串默认不转义
    3. 使用`'''...'''`来表示多行内容
  * 空值
    1. 用`none`表示，`none`不能理解为`0`因为`0`是有意义的    
  * 常量
    1. 除法
      * `/`精确除法，得到的是浮点数，即使是两个整数恰好整除
      * `//`地板除，两个整数的除法仍然是整数
      ```py
      10//3
      3
      ```
      * 余数运算 `%`

* 字符串和编码 中国使用的是`GB2312`
  * UNICODE
    1. 用两个字节表示一个字符。
    2. 但是如果文本基本是英文的话，用unicode编码比ASCII需要多一倍的存储空间。

  * utf-8
    1. utf-8可以把一个unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字符
    被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会别编码成4-6个字节。

            在计算机内存中统一使用Unicode编码，当需要保存道硬盘又或者需要传输的时候，
            就转为utf-8编码
            浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：
            所以很多网页的源码上会有类似`<meta charset="utf-8"  />`的信息，
            表示该网页正是用的是UTF-8编码

  * Python的字符串
    1. `ord()`获取字符的整数表示，`chr()`把编码转换成对应的字符
    2. 字节流`bytes`与`str`的转化

        ```py
        >>> '中文'.encode('utf-8')
        b'\xe4\xb8\xad\xe6\x96\x87'

        >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
        '中文'
        ```

    3. 利用`len()`计算`str`包含多少个字符或者`bytes`有多少字节数

    4. 申明  
    ```py
     #!/usr/bin/env python3'
     # -*- coding: utf-8 -*-
    ```

    * 格式化
    ```py
    'hi &s , your score is %d.'% ('pnk',100)
    ```
    `%d`整数  `%f`浮点数  `%s`字符串 `%x`十六进制整数 `%%`转义

    6. 指定是否补0和整数与小数的位数
        ```py
        >>> '%2d-%02d' % (3, 1)
        ' 3-01'
        >>> '%.2f' % 3.1415926
        '3.14'
        ```

* 使用list和tuple

区别： list是一种有序的集合，可以随时添加和删除其中的元素；tuple和list相似，
但是tuple一旦初始化就不能修改

  * list
    1. `len()`获得元素个数
    2. 索引是从[0]开始的，注意不要越界，[-1]直接获取最后一个元素
    3. 添加元素：`classmates.append('PnK') `
    4. 插入指定位置：`classmates.insert(1,'Alex')`
    5. 删除末尾元素：`classmates.pop(i)`不加i删除最末尾的元素
    6. 替换元素：`classmates[i]='dd'`直接替换
    7. 数据类型可以不同
    8. list里面可以是另一个list
  * tuple
    1. tuple不可变，所以代码更安全。最好多用tuple。
    2. 只有一个元素的时候定义tuple必须加上一个逗号来消除歧义`t=(1,)`!!!!!!!!!!
    3. tuple内含的list里面如果发生变化是允许的，tuple的所谓的“不变”是说，tuple的每个元素，
    指向永远不变


* 条件判断

哈哈哈哈计算机很强啊哈哈哈哈
  * if 条件判断
    1. `if``else``elif`语句：不要忘记写上冒号`：`！！！！！！！！！！！特点是从上往下判断
        ```py
        age = 3
        if age >= 18:
            print('adult')
        elif age >= 6:
            print('teenager')
        else:
            print('kid')
        ```
  * 再议input
    1. 使用input读取用户的输入，注意`input()`返回的数据类型是`str`
       所以用`number=int(input('please input a numeber'))`


* 循环

  * for...in循环（依次把list或tuple中的每个元素迭代出来）

    ```py
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)
    ```

    `for x in ...`就是把每个元素带入变量x，然后执行缩进块的语句
      * `range(i)`函数，可以生成一个整数数列（注：是小于i的整数）
         ```py
         >>> list(range(5))
         [0, 1, 2, 3, 4]
         ```
  * while循环（只要条件满足，就不断循环）
      记得加上冒号！！

* 使用dict和set（这个我第一遍的时候没有看懂）
都不能放入可变对象！！！！！！！！因为无法保证两个可变对象是否相等

  * dict（查找速度快，在内部计算出对应的存放数据的地址 key-value方式，
  但是占用大量的内存）dict的key是 **不可变对象**！！

     ```py
     >>> d['Adam'] = 67
     >>> d['Adam']
     67
     ```

    * 多次对一个key放入value时，后面的值会取代前面的值
    * 判断key是否存在
      * `in`
        ```py
        >>> 'Thomas' in d
        False
        ```
      * `get`
        ```py
        >>> d.get('Thomas')
        >>> d.get('Thomas', -1)
        -1
        ```
    * 删除一个key`d.pop('bob')`
    * 和list的区别：list查找和插入时间随元素增加而增加，但是占用空间小

  * set（是一组key的组合，但是不存储value，没有重复的key，可看成数学意义上的集合）
    ```py
    >>> s = set([1, 1, 2, 2, 3, 3])
    >>> s
    {1, 2, 3}
    ```
    * 注：重复元素会自动被过滤
    * 添加元素：`s.add(key)`
    * 删除元素：`s.remove(key)`
    * 交集 `s1 & s2`
    * 并集 `s1 | s2`

  * 再议不可变对象
  str是不变对象，list是可变对象
    ```py
    >>> a = 'abc'
    >>> a.replace('a', 'A')
    'Abc'
    >>> a
    'abc'
    ```
    * 注：对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，
    这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。


### 函数
函数就是最基本的一种代码抽象的方式

* 调用函数
  * [Build-in Functions](https://docs.python.org/3/library/functions.html#abs)
  * 数据类型转换
    * `int()`函数把其他数据类型转换为整数
    * 可以给函数名赋给一个变量，相当于给这个函数起了一个别名

* 定义函数（要使用`def`语句
注：要依次写出函数名、括号、括号中的参数和冒号`:`，在缩进块中编写函数体，函数的返回值用
`return`语句返回
  * 执行到`return`时，函数就执行完毕
  * 如果没有`return`语句，函数执行完毕也会返回结果，只是结果为`none`
  * 从文件中导入函数：

            如果已经把`my_abs()`的函数定义保存为`abstest.py`文件，可在该文件
             **当前目录** 下启动py解释器，用`from abstest import my_abs`导入函数
  * 空函数
    * `pass`语句：定义一个什么事也不做的空函数
      ```py
      def nop():
          pass
      ```
      * 用途：在没想好怎么写函数的代码，可以用pass作为占位符，使代码能够跑起来

  * 参数检查!!!!!!!!!
    * 对参数类型进行检查
      ```py
      def my_abs(x):
          if not isinstance (x,(int,float)):
              raise TypeError('bad operand type')
          if x >=0:
              return x
          else:
              return -x
      ```
  * 返回多个值（其实就是返回一个tuple）
    * 导入`math`包：`import math`

* 函数的参数

  * 位置参数：`power(x,n)`
      ```py
      def power(x,n):
        s=1
        while n>0:
            s = s * x
            n = n-1
        return s
      ```    
    * 注：调用函数时，传入的两个值按照顺序依次赋给参数`x`和`n`

  * 默认参数
    `power(x,n)`函数每次调用都需要输入n，但是我们基本上只计算x^2，所以可以把第二个参数
    设为2
    ```py
    def power(x,n=2):
        s=1
        while n>0:
            s=s*x
            n=n-1
        return s
    ```
    * 注： 1. 必选参数在前，默认参数灾后。 2.如何设置默认参数（根据参数的变化大小）
        ```py
        def enroll(name, gender, age=6, city='Beijing'):
        print('name:', name)
        print('gender:', gender)
        print('age:', age)
        print('city:', city)

        ```
        * 注：这样大多数的学生注册时不需要提供年龄和城市，只提供必须的两个参数
        * 当不按顺序提供部分默认参数值时，必须 **写上参数名** !!!
          ```py
          enroll('Adam', 'M', city='Tianjin')
          ```
        * 默认参数必须指向不变对象！！！！！！！！
          ```py
          def add_end(L=None):
          if L is None:
              L = []
          L.append('END')
          return L
          ```      
            * 注：设计`str`、`none`这样的不变对象的意义：对象内部的数据不能修改，
            减少由于修改数据导致的错误。

  * 可变参数（传入的参数可变） 组装list或tuple
####非关键字可变长参数（元组）
“非关键字”“可变长”顾名思义是允许在调用时传入多个“非关键字”参数，python会将这些多出来的参数放入一个元组中。

    * 如果不加*的话，输入的时候要先组装一个tuple或者list
      ```py
      def calc(*numbers):   #在此处加了一个*!!!!!!!!!!!!!!!!!!!!!!
      sum = 0
      for n in numbers:
          sum = sum + n * n
      return sum
      ```
    * 加上`*`可以把list或者tuple的元素变成 **可变参数** 传进函数*


  * 关键字参数  组装dict
####关键字可变长参数（字典）
“关键字”“可变长”顾名思义是允许在调用时传入多个“关键字”参数，python会将这些多出来的<参数名, 参数值>
放入一个字典中。需要注意的是，关键字变量参数应该为函数定义的最后一个参数，带**

    * 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple，
    而关键字函数允许你传入0个或任意个 **含参数名的参数** ，这些关键字参数在函数内部自动
    组装为一个dict。
    * 例子：函数`person`除了必选参数外还接受关键字参数`kw`。
      * 用处：可以扩展函数的功能，如果调用者愿意提供更多的参数，我们也能收到。
      ```py
      def person(name, age, **kw):
      print('name:', name, 'age:', age, 'other:', kw)
      ```
      * 和可变参数类似，也可以先组装出一个dict，然后把dict **转换为关键字参数** 传进去
        ```py
        >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
        >>> person('Jack', 24, city=extra['city'], job=extra['job'])
        name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

        简化：
        >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
        >>> person('Jack', 24, **extra)
        name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

        ```
      * `**extra`表示把`extra`这个dict的所有key-value用关键字参数传入到函数的`**kw`参数
      * 注：`kw`获得的dict时`extra`的一份拷贝，对`kw`的改动不会影响到函数外的`extra`

  * 命名关键字参数（限制关键字参数的名字）

    * 和关键字参数`**kw`不同，命名关键字参数需要一个特殊分隔符`*`，`*`后面的参数被视为
    命名关键字参数。
      ```py
      def person(name, age, *, city, job):
          print(name, age, city, job)
      调用方式如下：
      >>> person('Jack', 24, city='Beijing', job='Engineer')
      Jack 24 Beijing Engineer
      ```
    * 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了：
      ```py
      def person(name, age, *args, city, job):
          print(name, age, args, city, job)
      ```
    * 命名关键字参数 **必须传入参数名**，这和位置参数不同。如果没有传入参数名，调用将报错！！！
    * 命名关键字参数可以有缺省值，从而简化调用：

      ```py
      def person(name, age, *, city='Beijing', job):
        print(name, age, city, job)
      # 由于city具有默认值，在调用时可不传入city参数  

      调用：
      >>> person('Jack', 24, job='Engineer')
      Jack 24 Beijing Engineer

      ```
    * 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个`*`作为特殊分隔符。
    如果缺少`*`，Python解释器将无法识别位置参数和命名关键字参数：
      ```py
      def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
          pass
      ```

  * 参数组合
  在python中定义函数，可以用必选参数，默认参数，可变参数，关键字参数和命名关键字参数，
  这5种参数都可以组合使用，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数、
  关键字参数
    * 定义1个函数：

    ```py
    def f1(a, b, c=0, *args, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

    def f2(a, b, c=0, *, d, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    ```

    ```py
    调用：
    >>> f1(1, 2)
    a = 1 b = 2 c = 0 args = () kw = {}
    >>> f1(1, 2, c=3)
    a = 1 b = 2 c = 3 args = () kw = {}
    >>> f1(1, 2, 3, 'a', 'b')
    a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
    >>> f1(1, 2, 3, 'a', 'b', x=99)
    a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
    >>> f2(1, 2, d=99, ext=None)
    a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

    最神奇的是通过一个tuple和dict，你也可以调用上述函数：
    >>> args = (1, 2, 3, 4)
    >>> kw = {'d': 99, 'x': '#'}
    >>> f1(*args, **kw)
    a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
    >>> args = (1, 2, 3)
    >>> kw = {'d': 88, 'x': '#'}
    >>> f2(*args, **kw)
    a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
    ```
    * 对于任意函数，都可以通过类似`func(*args,**kw)`的形式调用它

上述的函数参数有一点点赘述，而且感觉没有完全理解。所以还要花功夫去多看看！！

[python函数参数总结](http://www.cnblogs.com/yuki-lau/archive/2013/05/28/3103303.html)

[理解 Python 中的 `*args` 和 `**kwargs`](http://kodango.com/variable-arguments-in-python)




* 递归函数

在函数内部，可以调用其他函数，如果一个函数在内部调用自身本身，这个函数就是递归函数
fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
```py
def fact(n):
    if n ==1:
        return 1
    return n* fact(n-1)  #return的时候引入了乘法表达式，所以不是尾递归了
```

理论上所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰

注：防止栈溢出！！！！！！

因为函数调用时通过栈（stack）这种数据结构实现的，
每当进入一个函数调用，栈就会加一层栈帧，每当函数返回时，栈就会减一层栈帧。
递归调用的次数过多，会导致栈溢出。

解决递归调用栈溢出的方法时通过尾递归优化，把循环看成一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，而且，return与i据不能包含表达式。这样，
编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧。

要把`fact(n)`函数改成尾递归方式，主要是把每一步的乘积传入到递归函数中。

```py
使用尾递归的方式：
def fact(n):
    return fact_itsf(n,1)
def fact_itsf(num,product):
    if n==1:
        return product
    return fact_itsf(num-1,product*num)
```
**优点** 如果做了优化，栈不会增长，无论多少次调用也不会导致栈溢出。

**但是** 大多数变成语言没有针对尾递归做优化，py解释器也没有做优化。
所以即使是把上面的函数改成了尾递归方式，也会导致栈溢出。

汉诺塔问题要抽象成用位置参数来模拟搬运！！！！！！！！！！！！！！！


### 高级特性
一行代码能实现的功能，决不写五行代码

* 切片：取一个list或tuple的部分元素
  * 正数切片
      ```py
      比如一个list如下：

      >>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

      取出前三个元素
      >>> L[0:3]   #c从索引[0]开始取，直到索引[3]为止，但不包括索引[3]
      ['Michael', 'Sarah', 'Tracy']
      ```

  * 同样支持倒数切片
      ```py
      >>> L[-2:]
      ['Bob', 'Jack']
      >>> L[-2:-1]  #倒数第一个元素的索引是-1
      ['Bob']
      ```
  * 前10个数，每两个取一个
      ```py
      >>> L[:10:2]
      ```
  * 所有数，每5个取一个
      ```py
      >>> L[::5]
      [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
      ```
  * 什么也不写，复制一个list
      ```py
      >>> L[:]
      [0, 1, 2, 3, ..., 99]
      ```
  * tuple也是一种list，也可用切片操作，但是操作的结果仍然是tuple
      ```py
      >>> (0, 1, 2, 3, 4, 5)[:3]
      (0, 1, 2)
      ```
  * 字符串`'xxx'`也可以看成是一种list，每个元素就是一个字符，只是操作的结果仍然是字符串
      ```py
      >>> 'ABCDEFG'[:3]
      'ABC'
      >>> 'ABCDEFG'[::2]
      'ACEG'
      ```

* 迭代（通过`for...in`完成）

只要是可迭代对象，无论有无下标，都可以迭代。

  * 比如dict就可以迭代
    ```py
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> for key in d:
    ...     print(key)
    ...
    a
    c
    b

    !!!!!如果要迭代value，`for value in d.values()`
    !!!!!如果同时迭代value和key，`for k,v in d.items()`

    ```
  * 迭代字符串
    ```py
    >>> for ch in 'ABC':
    ...     print(ch)
    ...
    A
    B
    C
    ```
  * 如何判断一个对象是否是可迭代对象呢？？（通过collections模块的 **Iterable类型** 判断：）
    ```py
    >>> from collections import Iterable
    >>> isinstance('abc',Iterable) # str是否可迭代
    True
    >>> isinstance(123, Iterable) # 整数是否可迭代
    False
    ```

  * 同时迭代索引和元素本身（利用内置的`enumerate`函数可以把一个list变成 **索引-元素对**）
    ```py
    >>> for i,value in enumerate(['A','B','C']):
    ...     print(i, value)
    ...
    0 A
    1 B
    2 C

    这个for循环里，同时引用了两个变量。
    >>> for x, y in [(1, 1), (2, 4), (3, 9)]:
    ...     print(x, y)
    ...
    1 1
    2 4
    3 9
    ```

* 列表生成式（内置的一个强大的用来创建list的生成式）

  * 生成list[1,2,3,4,5]可以用`list(range(1,11))`
  * 生成`[1x1, 2x2, 3x3, ..., 10x10]`
    ```py
    利用循环：
    L=[]
    for x in range(1,11):
        L.append(x*x)

    嫌循环太麻烦？？那你很棒哦
    使用列表生成式：
    [x*x for x in range(1,11)]       #这个真的很聪明哇！！！！

    ```
  * 写列表生成式时，把要生成的元素`x*x`放在前面，后面跟`for`循环，就可以把list创建出来。

  * `for`循环后面还可以 **加上if判断**
    ```py
    >>> [x*x for x in list(range(1,11)) if x %2 ==0]
    [4,16,36,64,100]
    ```
  * 还可以使用两层循环，可以 **生成全排列**：
    ```py
    >>> [m+n for m in 'ABC' for n in 'DEF']
    ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
    ```

      * ？列出当前目录下所有文件和目录名，可通过一行代码实现
      ```py
      >>>import os
      >>>[d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
      ```
  * 利用迭代生成dict对应同样可以使用列表生成式
    ```py
    使用迭代：
    >>> d={'x':'A','y':'B','z':'C'}
    >>> for k,v in d.items():
    ...    print(k,'=',v)
    ...
    y = B
    x = A
    z = C

    使用列表生成式：
    >>>d={'x':'A','y':'B','z':'C'}
    >>>[k+ '=' +v for k,v in d.items()]
    ['y=B', 'x=A', 'z=C']
    ```
  * 把一个list中的所有字符串变成小写
    ```py
    >>> L = ['Hello', 'World', 'IBM', 'Apple']
    >>> [s.lower() for s in L]
    ['hello','world','ibm','apple']
    ```
  * 练习：list中包含非字符串，添加if使列表生成式正确执行
    ```py
    L = ['Hello', 'World', 18, 'Apple', None]
    print([s.lower() for s in L if isinstance(s,str) == True])
    ```

* 生成器（一边循环一边计算的机制）
* 创建一个generator
  * 注：generato生成的是算法，每次调用函数，就计算出下一个元素的值，直到计算到最后一个元素
  * 把列表生成式的`[]`改成`()`
    ```py
    >>> L = [x * x for x in range(10)]
    >>> L
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    >>> g = (x * x for x in range(10))
    >>> g
    <generator object <genexpr> at 0x1022ef630>

    通过`next()`函数获得generator的下一个返回值
    >>> next(g)
    0
    >>> next(g)
    1
    >>> next(g)
    4
    ```

  * 创建一个generator后基本上永远不会调用`next()`，而是通过`for`循环来迭代它
  不需要关心`StopIteration`的错误
  * 如果`for`循环无法实现，还可以使用函数来实现

  * 函数定义中包含`yield`关键字（当包含yield时，函数就不再是一个普通的函数，而是一个generator）

    * 定义一个斐波拉契数列
      ```py
      用函数表达：
      def fib(max):
          n,a,b=0,0,1
          while n <max:
              print(b)
              a,b = b,a+b
              n=n+1
          return "done"

      用包含yield的generator表达：
      def fib(max):
          n,a,b=0,0,1
          while n <max:
              yield b     # 把print(b)改成了yield b
              a,b = b,a+b
              n=n+1
          return "done"
      ```

    * 这里，最难理解的就是generator和函数的执行流程不一样。
    函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
    而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
    再次执行时从上次返回的yield语句处继续执行。

      * 定义一个generator，依次返回数字1，3，5
      ```py
      def odd():
          print('step1')
          yield 1
          print('step2')
          yield(3)
          print('step3')
          yield(5)
      ```
        * 调用该generator时，首先要生成一个generator对象，然后用`next()`函数不断获得下一个返回值：
        ```py
        >>> o = odd()    # odd不是普通函数，而是generator
        >>> next(o)    # 执行过程中，遇到yield就中断，下次又继续执行
        step 1
        1
        >>> next(o)
        step 2
        3
        >>> next(o)
        step 3
        5
        >>> next(o)      # 执行三次yield后，已经没有yield执行了，所以第四次调用next()就报错
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        StopIteration
        ```

    * 回到fib()函数
    ```Py
    用包含yield的generator表达：
    def fib(max):
        n,a,b=0,0,1
        while n <max:
            yield b     # 把print(b)改成了yield b
            a,b = b,a+b
            n=n+1
        return "done"
    ```    
      * 一般使用`for`循环来迭代
      ```py
      >>> for n in fib(6):
      ...     print(n)
      ...
      1
      1
      2
      3
      5
      8
      ```
      * 但是这样拿不到return的返回值，所以必须捕获`StopIteration`错误，返回值包含在其中的value中
      ```py
      >>> g = fib(6)
      >>> while True:
      ...     try:
      ...         x = next(g)
      ...         print('g:', x)
      ...     except StopIteration as e:
      ...         print('Generator return value:', e.value)
      ...         break
      ...
      g: 1
      g: 1
      g: 2
      g: 3
      g: 5
      g: 8
      Generator return value: done
      ```
  * 这里真的很难懂啊qaq，在写杨辉三角的时候简直。。一筹莫展
  * 扔两个链接
    * [what is the use of the yield keyword in python?What does it do?](http://stackoverflow.com/questions/231767/what-is-the-function-of-the-yield-keyword/231855#231855)
    * [python yield使用浅析](http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)
    * []
