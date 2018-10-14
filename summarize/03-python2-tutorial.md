# Python Tutorial 2.7.14总结

> 参考书籍：http://www.pythondoc.com/pythontutorial27/

## 编码风格

 [**PEP 8**](https://www.python.org/dev/peps/pep-0008) 引入了大多数项目遵循的风格指导，以下是比较实用的编码风格：

- 使用 4 空格缩进，而非 TAB。

  在小缩进(可以嵌套更深)和大缩进(更易读)之间，4 空格是一个很好的折中。TAB 引发了一些混乱，最好弃用。

- 折行以确保其不会超过 79 个字符。

  这有助于小显示器用户阅读，也可以让大显示器能并排显示几个代码文件。

- 使用空行**分隔函数和类**，以及函数中的大块代码。

- 可能的话，**注释独占一行**

- 使用**文档字符串**

- 把空格放到操作符两边，以及逗号后面，但是括号里侧不加空格：`a = f(1, 2) + g(3, 4)`。

- 统一函数和类命名。

  推荐**类名**用 **`驼峰命名`，函数和方法名用 `小写_和_下划线`**。总是用 `self` 作为方法的第一个参数。

- 不要使用花哨的编码，如果你的代码的目的是要在国际化 环境。Python 的默认情况下，UTF-8，甚至普通的 ASCII 总是工作的最好。

- 同样，也不要使用非 ASCII 字符的标识符，除非是不同语种的会阅读或者维护代码。

## 数据结构

### 列表常用函数

|                       对象方法                       | 描述                                                         |
| :--------------------------------------------------: | :----------------------------------------------------------- |
|                  `list.append`(*x*)                  | 把一个元素添加到链表的结尾（入栈）                           |
|                  `list.pop`([*i*])                   | 从链表的指定位置删除元素，**并将其返回**，如果没有指定索引，`a.pop()` 返回最后一个元素。（出栈） |
| `list.sort`(*cmp=None*, *key=None*, *reverse=False*) | 对链表中的元素就地进行排序                                   |
|                   `list.reverse`()                   | 就地倒排链表中的元素                                         |
|                  `list.remove`(*x*)                  | 删除链表中值为 *x* 的第一个元素。如果没有这样的元素，就会返回一个错误。 |
|               `list.insert`(*i*, *x*)                | 在指定位置插入一个元素                                       |
|                  `list.index`(*x*)                   | 返回链表中第一个值为 *x* 的元素的索引，如果没有匹配的元素就会返回一个错误 |
|                  `list.count`(*x*)                   | 返回 *x* 在链表中出现的次数                                  |
|                  `list.extend`(*L*)                  | 将一个给定列表中的所有元素都添加到另一个列表中，相当于 `a[len(a):] = L` |

队列实现`collections.deque()`，`append()`和`popleft()`

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### 函数式编程工具

对于链表： [filter()](https://docs.python.org/2.7/library/functions.html#filter)，[map()](https://docs.python.org/2.7/library/functions.html#map) 以及 [reduce()](https://docs.python.org/2.7/library/functions.html#reduce)

* `filter(function, sequence)` 返回一个 sequence(序列)，包括了给定序列中所有调用`function(item)` 后返回值为 true 的**元素(**如果可能的话，会返回相同的类型)—返回x

```python
>>> def f(x): return x % 3 == 0 or x % 5 == 0
...
>>> filter(f, range(2, 25))
[3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]
```

* `map(function, sequence)` 为每一个元素依次调用 `function(item)` 并将**返回值**组成一个链表返回—返回y

```python
>>> def cube(x): return x*x*x
...
>>> map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

* `reduce(function, sequence)` 返回一个单值，首先以序列的前两个元素调用函数 *function*，再以返回值和第三个参数调用，依次执行下去。

```python
>>> def add(x,y): return x+y
...
>>> reduce(add, range(1, 11))
55
```

列表推导式：

```python
squares = [x**2 for x in range(10)]
```

### 元组和序列

元组不可变`>>> singleton = 'hello',    # <-- note trailing comma`

### 集合

集合是一个无序不重复元素的集，基本功能包括关系测试和消除重复元素

```python
>>> a = set('abracadabra')
>>> a                                  # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

### 字典

创建字典：

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

### 循环技巧

在**序列**中循环时，索引位置和对应值可以使用 [enumerate()](https://docs.python.org/2.7/library/functions.html#enumerate) 函数同时得到:

```
list = ['tic', 'tac', 'toe']
>>> for i, v in enumerate(list):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

多个循环，使用`zip()`整体打包循环：

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print 'What is your {0}?  It is {1}.'.format(q, a)
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

遍历字典时，使用 `iteritems()` 方法可以同时得到键和对应的值。:

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.iteritems():
...     print k, v
...
gallahad the pure
robin the brave
```

* `not` 具有最高的优先级，`or` 优先级最低，所以 `A and not B or C` 等于 `(A and (notB)) or C`

## 模块

- 以 [-O](https://docs.python.org/2.7/using/cmdline.html#cmdoption-O) 参数调用 Python 解释器时，会生成优化代码并保存在 `.pyo` 文件中。现在的优化器没有太多帮助；它只是删除了断言( [assert](https://docs.python.org/2.7/reference/simple_stmts.html#assert))语句。使用 [-O](https://docs.python.org/2.7/using/cmdline.html#cmdoption-O) 参数，*所有* 的字节码([bytecode](https://docs.python.org/2.7/glossary.html#term-bytecode))都会被优化；`.pyc` 文件被忽略，`.py` 文件被编译为优化代码。
- 向 Python 解释器传递两个 [-O](https://docs.python.org/2.7/using/cmdline.html#cmdoption-O) 参数([-OO](https://docs.python.org/2.7/using/cmdline.html#cmdoption-OO))会执行完全优化的二进制优化编译，这偶尔会生成错误的程序。现在的优化器，只是从字节码中删除了 `__doc__` 符串，生成更为紧凑的 `.pyo` 文件。因为某些程序依赖于这些变量的可用性，你应该只在确定无误的场合使用这一选项。
- 来自 `.pyc` 文件或 `.pyo` 文件中的程序不会比来自 `.py` 文件的运行更快；`.pyc` 或 `.pyo` 文件只是在它们加载的时候更快一些。
- 通过脚本名在命令行运行脚本时，不会将为该脚本创建的二进制代码写入 `.pyc` 或 `.pyo` 文件。当然，把脚本的主要代码移进一个模块里，然后用一个小的启动脚本导入这个模块，就可以提高脚本的启动速度。也可以直接在命令行中指定一个 `.pyc`或 `.pyo` 文件。
- 对于同一个模块(译者：这里指例程 spam.py)，可以只有 `spam.pyc` 文件(或者 `spam.pyo`，在使用 [-O](https://docs.python.org/2.7/using/cmdline.html#cmdoption-O) 参数时)而没有 `spam.py` 文件。这样可以打包发布比较难于逆向工程的 Python 代码库。
- [compileall](https://docs.python.org/2.7/library/compileall.html#module-compileall) 模块可以为指定目录中的所有模块创建 `.pyc` 文件(或者使用 [-O](https://docs.python.org/2.7/using/cmdline.html#cmdoption-O) 参数创建 `.pyo` 文件)。

### 包

包内引用：包中使用了子包结构，可以按绝对位置从相邻的包中引入子模块

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

## 输入与输出

### 格式化输出

* 函数 [str()](https://docs.python.org/2.7/library/functions.html#str) 用于将值转化为适于人阅读的形式，而 [repr()](https://docs.python.org/2.7/library/functions.html#repr) 转化为供解释器读取的形式，某对象没有适于人阅读的解释形式的话，[str()](https://docs.python.org/2.7/library/functions.html#str) 会返回与 [repr()](https://docs.python.org/2.7/library/functions.html#repr) 等同的值。

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
```

* [str.rjust()](https://docs.python.org/2.7/library/stdtypes.html#str.rjust) ,它把字符串输出到一列，并通过向左侧填充**空格**来使其右对齐；切割操作，例如：`x.ljust(n)[:n]`，[str.zfill()](https://docs.python.org/2.7/library/stdtypes.html#str.zfill) 它用于向数值的字符串表达左侧**填充 0**

* [str.format()](https://docs.python.org/2.7/library/stdtypes.html#str.format) 已经复习过

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

* 旧式的字符串格式化

```python
>>> import math
>>> print 'The value of PI is approximately %5.3f.' % math.pi
The value of PI is approximately 3.142.
```

## 文件读写

* `f.read(size)`读取若干数量的数据并以字符串形式返回其内容，*size* 是可选的数值，指定字符串长度。如果没有指定 *size* 或者指定为负数，就会读取并返回整个文件。

* `f.readline()` 从文件中读取单独一行，字符串结尾会自动加上一个换行符( `\n` )，只有当文件最后一行没有以换行符结尾时，这一操作才会被忽略。
* `f.readlines()` 返回一个列表，其中包含了文件中所有的数据行。
* `f.write(string)` 方法将 string 的内容写入文件，**并返回写入字符的长度**
* `f.tell()` 返回一个整数，代表文件对象在文件中的指针位置，该数值计量了自文件开头到指针处的比特数。
* `f.seek(offset,from_what)`改变文件对象指针，指定的引用位置移动 *offset* 比特，引用位置由 *from_what* 参数指定，默认为0

### 使用 [json](https://docs.python.org/2.7/library/json.html#module-json) 存储结构化数据

标准模块 [json](https://docs.python.org/2.7/library/json.html#module-json) 可以接受 Python 数据结构，并将它们转换为字符串表示形式；此过程称为 **序列化**。从字符串表示形式重新构建数据结构称为 **反序列化**。

> JSON 格式经常用于现代应用程序中进行数据交换。许多程序员都已经熟悉它了，使它成为相互协作的一个不错的选择。

```python
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'
```

[dumps()](https://docs.python.org/2.7/library/json.html#json.dumps) 函数的另外一个变体 [dump()](https://docs.python.org/2.7/library/json.html#json.dump)，直接将对象序列化到一个文件。所以如果 `f` 是为写入而打开的一个 [文件对象](https://docs.python.org/2.7/glossary.html#term-file-object)，我们可以这样做:`json.dump(x, f)`

`x = json.load(f)`：重新解码对象。

## 错误和异常

```python
try:
    raise ...
except Exception as e:
    ...
finally:
    ...
```

## 类

### 迭代器

大多数容器对象都可以用 [for](https://docs.python.org/2.7/reference/compound_stmts.html#for) 遍历:

在后台，[for](https://docs.python.org/2.7/reference/compound_stmts.html#for) 语句在容器对象中调用 [iter()](https://docs.python.org/2.7/library/functions.html#iter)。 该函数返回一个定义了 [next()](https://docs.python.org/2.7/library/stdtypes.html#iterator.next) 方法的迭代器对象，它在容器中逐一访问元素。没有后续的元素时，[next()](https://docs.python.org/2.7/library/stdtypes.html#iterator.next) 抛出一个 [StopIteration](https://docs.python.org/2.7/library/exceptions.html#exceptions.StopIteration) 异常通知 [for](https://docs.python.org/2.7/reference/compound_stmts.html#for) 语句循环结束。以下是其工作原理的示例:

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<iterator object at 0x00A1DB50>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
    next(it)
StopIteration
```

### 给自己的类定义迭代器

定义一个 [`__iter__()`](https://docs.python.org/2.7/reference/datamodel.html#object.__iter__) 方法，使其返回一个带有 [next()](https://docs.python.org/2.7/library/stdtypes.html#iterator.next) 方法的对象。如果这个类已经定义了 [next()](https://docs.python.org/2.7/library/stdtypes.html#iterator.next)，那么 [`__iter__()`](https://docs.python.org/2.7/reference/datamodel.html#object.__iter__) 只需要返回 `self`:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

### 生成器

 [yield](https://docs.python.org/2.7/reference/simple_stmts.html#yield) 语句，每次 [next()](https://docs.python.org/2.7/library/functions.html#next) 被调用时，生成器回复它脱离的位置(它记忆语句最后一次执行的位置和所有的数据值)。当发生器终结时，还会自动抛出 [StopIteration](https://docs.python.org/2.7/library/exceptions.html#exceptions.StopIteration)异常。

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> from math import pi, sin
>>> sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

>>> unique_words = set(word  for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```

## Python标准库概览

### 操作系统接口

```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python27'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0

# 文件管理
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
>>> shutil.move('/build/executables', 'installdir')

# 从目录通配符搜索中生成文件列表
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

### random

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(xrange(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```

### 互联网访问

用于处理从 urls 接收的数据的 [urllib2](https://docs.python.org/2.7/library/urllib2.html#module-urllib2) 以及用于发送电子邮件的 [smtplib](https://docs.python.org/2.7/library/smtplib.html#module-smtplib):

```python
>>> import urllib2
>>> for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
...     line = line.decode('utf-8')  # Decoding the binary data to text.
...     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
...         print line

<BR>Nov. 25, 09:43:32 PM EST

# 需要在 localhost 运行一个邮件服务器 
>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```

### 日期和时间

```python
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

### 数据压缩

[zlib](https://docs.python.org/2.7/library/zlib.html#module-zlib)，[gzip](https://docs.python.org/2.7/library/gzip.html#module-gzip)，[bz2](https://docs.python.org/2.7/library/bz2.html#module-bz2)，[zipfile](https://docs.python.org/2.7/library/zipfile.html#module-zipfile) 以及 [tarfile](https://docs.python.org/2.7/library/tarfile.html#module-tarfile)

```
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

### 性能度量

[timeit](https://docs.python.org/2.7/library/timeit.html#module-timeit) 

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```

> 更多细节见：http://www.pythondoc.com/pythontutorial27/stdlib2.html