
# 回顾Python数据类型

> Python支持面向对象的编程模式，这意味这Python在解决问题的过程中重点是数据.

## 基本类型

* 内置的原子数据类型:主要的内置数字类，int和float;bool;


```python
False or True
```




    True




```python
not (False or True)
```




    False



* 内置的集合数据类型：
    * 有序集合`List[];string;tuple()`;
    * 无序集合`dict{},set{}`;


```python
myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)
```

    [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    [[1, 2, 45, 4], [1, 2, 45, 4], [1, 2, 45, 4]]
    


```python
# 与sort方法合用有效果
myList.sort()
myList
```




    [1, 2, 4, 45]




```python
myList.reverse()
print myList
```

    [45, 4, 2, 1]
    

* `split`方法，没有指定参数则以空格字符作为分割点，如`Tab,space,\n`，指定参数则以该参数作为分隔点，该参数不会打印输出


```python
myName = 'dsdshahahads'
myName.split('s')
```




    ['d', 'd', 'hahahad', '']



* 列表和字符串之间的主要区别是，列表可以被修改，而字符串不能;
* 元组不可修改
* set是一个无序的， 为空或是更多不可变Python数据对象集合。
* 集合中的值不允许重复，以逗号分隔，写在大括号中。空集合由set()表示。集合是异构的并且可以被分配给一个变量


```python
{3,6,"cat",4.5,False,6,6,6,6,6,6,6}
```




    {False, 3, 4.5, 6, 'cat'}



## 输入与输出


```python
aName = input("Please enter your name ")
print("Your name in all capitals is",aName.upper(),
      "and has length", len(aName))
```

    Please enter your name  'ds'
    

    Your name in all capitals is 'DS' and has length 4
    


```python
# Python3支持，Python2不支持
print("Hello","World", sep = "***")
print("Hello","World", end = "***")
```

    Hello***World
    Hello World***

## 控制结构

* 两种数据结构：迭代和选择
    * 迭代：`while,for`
    * 选择：`if elif else`

## 异常 


```python
import math
try:
    anumber = int(input("Please enter an integer "))
    print(math.sqrt(anumber))
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(anumber)))
```

    Please enter an integer  -3
    

    Bad Value for square root
    Using absolute value instead
    1.73205080757
    


```python
import math
try:
    anumber = int(input("Please enter an integer "))
    print(math.sqrt(anumber))
except Exception as msg:
    print msg
```

    Please enter an integer  -33
    

    math domain error
    

## 定义函数


```python
def f(x):
    x *= x
    if not x < 100:
        return x
    else:
        return f(x)
```


```python
f(5)
```




    625




```python
f(f(3))
```




    43046721



## 类


```python
def gcd(m,n):
    """取余的公约数求法"""
    while m%n != 0:
        m,n = n,m%n
    return n

class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
        """
        覆盖__eq__方法，通过相同的值创建深相等,而不是相同的引用
        即"=="，返回bool值
        """
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
```

    7/6
    False
    

## 面向对象编程详见专题笔记

## 总结

* 计算机科学是解决问题的研究。
* 计算机科学使用抽象作为表示过程和数据的工具。
* 抽象的数据类型允许程序员通过隐藏数据的细节来管理问题领域的复杂性。
* Python是一种强大但易于使用的面向对象语言。
* 列表、元组和字符串都是用Python有序集合构建的。
* 字典和集合是无序的数据集合。
* 类允许程序员实现抽象的数据类型。
* 程序员可以重写标准方法，并创建新的方法。
* 类可以被组织成层次结构。
* 类构造器应该总是调用其父节点的构造函数，然后继续使用自己的数据和行为。
