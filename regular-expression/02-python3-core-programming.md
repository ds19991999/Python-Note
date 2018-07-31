# Python3核心编程之正则表达式

* **“搜索”（searching），即在字符串任意部分中搜索匹配的模式**；
* **“匹配”（matching）是指判断一个字符串能否从起始处全部或者部分地匹配某个模式**

### 元字符

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716094709.png)

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716094822.png)

### 择一匹配模式

择一匹配的管道符号（|），从多个模式中选择其一进行匹配

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716095325.png)

### 匹配任意单个字符

**点号或者句点（.）符号匹配除了换行符\n 以外的任何字符**（Python 正则表达式有一个编译标记[S 或者 DOTALL]，该标记能够推翻这个限制，使点号能够匹配换行符）

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716095730.png)

### 从字符串起始或者结尾或者单词边界匹配

指定用于**搜索**的模式，匹配字符串的开始位置，就必须使用脱字符（^）或者特殊字符\A，美元符号（$）或者\Z将用于匹配字符串的末尾位置

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716100816.png)

\b 将用于匹配一个单词的边界，\B 将匹配出现在一个单词中间的模式，即不是边界

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716101815.png)

### 创建字符集

方括号[ ]，能够匹配一对方括号中包含的任何字符，相当于逻辑或

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716102235.png)

### 限定范围和否定

方括号中两个符号中间用连字符（-）连接，用于指定一个字符的范围

脱字符（^）紧跟在左方括号后面，这个符号就表示不匹配给定字符集中的任何一个字符。

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716102747.png)

### 使用闭包操作符实现存在性和频数匹配

* 星号操作符（*）将匹配其左边的正则表达式出现**零次或者多次**的情况（编译原理中，该操作称为 Kleene 闭包）
* 加号（+）操作符将匹配**一次或者多次**出现的正则表达式
* 问号（？）操作符将匹配**零次或者一次**出现的正则表达式
* 大括号操作符（{}），指定匹配次数，如{4}，{3，9}

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716103500.png)

### 表示字符集的特殊字符

* \d 表示匹配任何十进制数字
* \w能够用于表示全部字母数字的字符集，相当于[A-Za-z0-9_]的缩写形式
* \s 可以用来表示空格字符
* 上述字符的大写版本表示不匹配

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716221431.png)

### 使用圆括号指定分组

* 圆括号（）：
  * 对正则表达式进行分组
  * 匹配子组

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716105427.png)

### 扩展表示法

* （?…）实现一个前视（或者后视）匹配，或者条件检查

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180716110325.png)
