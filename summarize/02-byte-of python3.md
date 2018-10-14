# Byte of Python3 总结

## 格式化字符串

字符串不可变，正则表达式中的字符串应该使用原始字符串`r"strings"`

format方法：

```python
>>> age = 20
>>> name = "ds19991999"
>>> print('{} was {} years old'.format(name,age))
ds19991999 was 20 years old
>>> print('{0} was {1} years old'.format(name,age))
ds19991999 was 20 years old
>>> print("{0:.3f}".format(4.0/3))
1.333
>>> print('{0:_^11}'.format('hello'))
___hello___
>>> print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
Swaroop wrote A Byte of Python
```

指定结尾符号

```python
print('a', end='')
print('b', end=' ')
print('c', end='\n')
```

## 运算符与表达式

运算符与C/C++差异比较大

```python
/ 除，结果是浮点数
// 整除，整数整除结果为int，否则为float,执行floor除法
% 取模，返回除法运算后的余数
<< 左移，2<<2------>10--1000得8
& 按位与，5&3------>101&011得001，结果为1
| 按位或，5|3------>101|011得111，结果为7
^ 按位异或，5^3----->101^011得110，结果为6（相同为0，不同为1）
~ 按位取反 x~ ------>得-(x+1)
not and or
```

`continue`跳出当前循环块剩余语句，继续下一次迭代

## 参数

https://www.douban.com/note/13413855/

`gloabal`语句：定义全局变量，`gloabal x`

      1. `F(arg1,arg2,...)` 传统参数
      2. `F(arg2=<value>,arg3=<value>...)` 默认参数
      3. `F(*arg1)` 可变参数，函数实际参数个数是不一定的，存放在以形参名为标识符的tuple中
      4. `F(**arg1) ` 可变参数，在函数内部将被存放在以形式名为标识符的dictionary中。这时候调用函数**必须采用key1=value1、key2=value2...**的形式。

```python
def addOn(**arg):
	sum = 0
    if len(arg) == 0: return 0
    else:
       for x in arg.itervalues():
          sum += x
    return sum
addOn(x=4,y=5,k=6)
```

注意：在定义或调用这种函数时，顺序不能变

```
def function(arg1,arg2=<value>,*arg3,**arg4)
```

首先按顺序把“arg”这种形式的实参给对应的形参
第二，把“arg=<value>”这种形式的实参赋值给形参
第三，把多出来的“arg”这种形式的实参组成一个tuple给带一个星号的形参
第四，把多出来的“key=value”这种形式的实参转为一个dictionary给带两个星号的形参

* 查看文档字符串`function.__doc__`，也适用于Modules和类

## 模块

* `.pyc`文件是按字节码编译的Byte-Compiled文件，导入模块更快速，独立于运行平台

* `__name__`:

```python
if __name__=="__main__":
	main()
else:
    print("Import from another module")
```

* import的是文件名，一个模块
* dir(模块名)，返回一个包含模块属性名称的列表，dir()返回当前环境下的属性名称列表

## 包

包的结构：

```python
- world/
    - __init__.py
    - asia/
        - __init__.py
        - india/
            - __init__.py
            - foo.py
    - africa/
        - __init__.py
        - madagascar/
            - __init__.py
            - bar.py
```

如上，包的名称为world，asia和afica是它的子包，子包包含india、madagascar等模块

## 数据结构

* list[]、tuple()、dictionary{}、set([])

* 注意a.sort()—list方法，b=sorted(a)—对所有可迭代对象操作，a.reverse()—list方法，`del [0] and a.remove(a[0])`

列表的引用：`a=[1,2,3,4]; b=a`，a和b指向同一个对象，改变a或b，都会改变，b=a[:]，则相当于copy一个对象，a与b不会互相改变

* tuple不可变
* 只能选择不可变的对象作为字典的键值（keys），字典也有`del a[“keys”]

```python
for keys,vals in adic.items():
	print(keys,vals)
```

> 更详细的总结见后续博客更新

一些方法：

```python
time.strftime("Y%m%d%H%M%S%")  返回当前日期与时间
os.system(command_string) 执行系统命令行，执行成功返回0
if not os.path.exists(target_dir): 判断目标路径存不存在
    os.mkdir(target_dir)
seq.replace(" ","_")，序列（字符串）将空格取代为_
```

## 软件开发流程

what——>how——>do it——>test——>use——>maintain

## 面向对象编程

`__init__`方法、类变量和对象变量、装饰器classmethod、继承

## 输入与输出

**Pickle:**将纯Python对象存储在一个文件中，并在稍后取回，这叫持久性(Persistently)存储对象.

```python
pickle.dump(list,file) # 存储到文件
pickle.load(file)#加载文件
```

## 异常

```python
# coding=UTF-8
class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    text = input('Enter something -->')
    if len(text) < 3:
        raise ShortInputException(len(text),3)
     # 其他工作能在此处继续正常运行
    else:
    	print('No exception was raised.)
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was' + 
           {0} long, expected at least {1}')
           .format(ex.length, ex.atleast))

```

`try except finally`

```python
with open("poem.txt") as f:
	for line in f:
		print(line,end='') 
```

## 特殊方法

* 使用元祖返回多个值，`return (a, b)`
* `__init__(self, ...)`
  * 这一方法在新创建的对象被返回准备使用时被调用
* `__del__(self)`
  * 这一方法在对象被删除之前调用（它的使用时机不可预测，所以避免使用它）
* `__str__(self)`
  * 当我们使用 print 函数时，或 str() 被使用时就会被调用。
* ``__lt__(self, other)``
  * 当小于运算符（<）被使用时被调用。类似地，使用时都会有特殊方法被调用。
* `__getitem__(self, key)`
  * 使用 x[key] 索引操作时会被调用。
* `__len__(self)`
  * 当针对序列对象使用内置 len() 函数时会被调用
* lambda 语句:
* 列表推导：

```python
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)
```

* assert 语句：用以断言（Assert）某事是真的，如果其不是真的，就抛出一个错误
* 装饰器