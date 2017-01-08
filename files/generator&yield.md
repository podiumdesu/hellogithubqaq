[what is the use of the yield keyword in python?What does it do?](http://stackoverflow.com/questions/231767/what-is-the-function-of-the-yield-keyword/231855#231855)
==
[中文版](http://pyzh.readthedocs.io/en/latest/the-python-yield-keyword-explained.html)

To understand what yield does, you must understand what *generators* are. And before generators come iterables.

#### Iterables

When you create a list, you can read its items one by one. Reading its items one by one is called iteration:
```py
>>> mylist = [1, 2, 3]
>>> for i in mylist:
...    print(i)
1
2
3
```
mylist is an iterable. When you use a list comprehension, you create a list, and so an iterable:
```py
>>> mylist = [x*x for x in range(3)]
>>> for i in mylist:
...    print(i)
0
1
4
```
Everything you can use "`for... in...`" on is an iterable; `lists`, `strings`, files...

These iterables are handy because you can read them as much as you wish, but you store all the values in memory and this is not always what you want when you have a lot of values.

#### Generators

Generators are iterators, but **you can only iterate over them once**. It's because they do not store all the values in memory, **they generate the values on the fly:**
```py
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4
```
It is just the same except you used `()` instead of `[]`. BUT, you **cannot** perform `for i in mygenerator` a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.

#### Yield

`Yield` is a keyword that is used like `return`, except the function will return a generator.
```py
>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
```
Here it's a useless example, but it's handy when you know your function will return a huge set of values that you will only need to **read once**.

To master `yield`, you must understand that **when you call the function, the code you have written in the function body does not run. The function only returns the generator object**, this is a bit tricky :-)

Then, your code will be run each time the `for` uses the generator.

Now the hard part:

The first time the `for` calls the generator object created from your function, it will **run the code in your function from the beginning until it hits yield**, then it'll return the first value of the loop. Then, each other call will run the loop you have written in the function one more time, and return the next value, until there is no value to return.

The generator is considered empty once the function runs but does not hit yield anymore. It can be because the loop had come to an end, or because you do not satisfy an "if/else" anymore.


[python yield使用浅析](http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)
==

简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。


我们可以得出以下结论：
一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
