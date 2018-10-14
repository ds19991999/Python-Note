
## Python2和Python3的区别

### print和input
Python2等价版本
```python
print "fish"
print ("fish") #注意print后面有个空格
print("fish") #print()不能带有任何其它参数
```
Python3中没有print语句，由print()函数代替,可以有空格
```python
>>> print("fish", "panda", sep='#')
fish#panda
```
在python2.x中raw_input()和input( )，两个函数都存在:
* raw_input()---将所有输入作为字符串看待，返回**字符串类型**
* input()-----只能接收**数字**的输入，在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（int, float ）

python3.x中raw_input()和input( )进行了整合，去除了raw_input()，input()函数接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。

### Unicode
* Python 2 有 ASCII str() 类型，unicode() 是单独的，不是 byte 类型。
* 在 Python 3，我们最终有了 Unicode (utf-8) 字符串，以及一个字节类：byte 和 bytearrays。
*  Python3.X 源码文件默认使用utf-8编码


```python
# Python2
str = "我爱北京天安门"
str
```




    '\xe6\x88\x91\xe7\x88\xb1\xe5\x8c\x97\xe4\xba\xac\xe5\xa4\xa9\xe5\xae\x89\xe9\x97\xa8'




```python
str = u"我爱北京天安门"
str
```




    u'\u6211\u7231\u5317\u4eac\u5929\u5b89\u95e8'




```python
# Python3
str = "我爱北京天安门"
str    
```




    '我爱北京天安门'



### 除法运算
**Python中的除法有两个运算符，/和//**

首先来说`/`除法:
* python 2.x中/除法就是整数相除是一个整数，浮点数相除保留小数部分,最多显示17位



```python
#python2
4/3
```




    1




```python
# python 3.x中/除法对于整数之间的相除，结果也会是浮点数
4/3
```




    1.3333333333333333



对于//除法:
* python 2.x和python 3.x中是一致的,执行floor除法，取比结果小的最大整数


```python
# python2
-1//2
```




    -1




```python
# python3
-1//2
```




    -1



### 异常

Python 3 中我们现在使用 as 作为关键词，捕获异常的语法由 `except exc, var` 改为 `except exc as var`。
* 在2.x时代，所有类型的对象都是可以被直接抛出的，**在3.x时代，只有继承自BaseException的对象才可以被抛出。**
*  2.x raise语句使用逗号将抛出对象类型和参数分开，3.x取消了这种奇葩的写法，直接调用构造函数抛出对象即可。

### xrange

* Python2中xrange()比range()更快
* Python3中不存在xrange(),但range()与之前的xrange()一样快

### 八进制字面量表示

* Python2中，八进制数必须写成0o777或者0777，二进制必须写成0b111，bin()函数用于将一个整数转换成二进制字串
* Python3中，表示八进制字面量的方式只有一种，就是0o1000


```python
# Python2
print 0o1000,01000
```

    512 512



```python
# Python3
print(0o1000)
```

    512



```python
print(01000)
```


      File "<ipython-input-3-d096c5298f8d>", line 1
        print(01000)
                  ^
    SyntaxError: invalid token



### 不等运算符
* Python 2.x中不等于有两种写法 != 和 <>
* Python 3.x中去掉了<>, 只有!=一种写法，习惯上都是!=，不用在意这个

### 去掉了repr表达式\`\`

* Python 2.x 中反引号``相当于repr函数的作用
* Python 3.x 中去掉了``这种写法，只允许使用repr函数，repr一般只在debug的时候才用，多数时候还是用str函数来用字符串描述对象。

### 多个模块被改名

|旧的名字|	新的名字|
|:--------:|:------:|
|`_winreg`	|winreg|
|ConfigParser|	configparser|
|copy_reg|	copyreg|
|Queue|	queue|
|SocketServer|	socketserver|
|repr|	reprlib|

httplib, BaseHTTPServer, CGIHTTPServer, SimpleHTTPServer, Cookie, cookielib被合并到http包内。取消了exec语句，只剩下exec()函数

### 数据类型

* Py3.X去除了long类型，现在只有一种整型int，但它的行为就像2.X版本的long
* 新增了bytes类型，对应于2.X版本的八位串，定义一个bytes字面量的方法如下：


```python
# python3
b = b'china'
type(b)
```




    bytes



* str对象和bytes对象转换：`str -> bytes`----`.encode()` 或者 `bytes -> str`----`.decode()`
* dict的.keys()、.items 和.values()方法返回迭代器，而之前的iterkeys()等函数都被废弃。同时去掉的还有 dict.has_key()，用 in替代它

### map、filter 和 reduce

* Python2.x 的交互下输入 map 和 filter,看到它们两者的类型是 built-in function(内置函数):

```python
# python2中他们都是内置函数，输出都是列表
>>> map
<built-in function map>
>>> filter
<built-in function filter>
>>> map(lambda x:x *2, [1,2,3])
[2, 4, 6]
>>> filter(lambda x:x %2 ==0,range(10))
[0, 2, 4, 6, 8]
>>>
```
```python
# python3中他们变成了类，返回结果变成了可迭代对象
>>> map
<class 'map'>
>>> map(print,[1,2,3])
<map object at 0x10d8bd400>
>>> filter
<class 'filter'>
>>> filter(lambda x:x % 2 == 0, range(10))
<filter object at 0x10d8bd3c8>
>>> f =filter(lambda x:x %2 ==0, range(10))
>>> next(f)
0
>>> next(f)
2
>>> next(f)
4
>>> next(f)
6
```
注意：Python2中，next()函数 and .next()方法都能用，Python3中只有next()函数

### For循环变量和全局命名空间泄漏


```python
# python2
i = 1
print 'before: i =', i
print 'comprehension: ', [i for i in range(5)]
print 'after: i =', i
```

     before: i = 1
    comprehension:  [0, 1, 2, 3, 4]
    after: i = 4



```python
# python3
i = 1
print('before: i =', i)
print('comprehension:', [i for i in range(5)])
print('after: i =', i)
```

    before: i = 1
    comprehension: [0, 1, 2, 3, 4]
    after: i = 1


### 返回可迭代对象，而不是列表


```python
# python2
print range(3)
print type(range(3))
```

    [0, 1, 2]
    <type 'list'>



```python
# python3
print(range(3))
print(type(range(3)))
print(list(range(3)))
```

    range(0, 3)
    <class 'range'>
    [0, 1, 2]


Python 3 中一些经常使用到的不再返回列表的函数和方法：
```python
zip()
map()
filter()
dictionary’s .keys() method
dictionary’s .values() method
dictionary’s .items() method
```

### 参考
* http://t.cn/RVJIxxm
* http://www.runoob.com/python/python-2x-3x.html
