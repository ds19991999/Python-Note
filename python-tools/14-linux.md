# Linux基本命令

## 1.放大缩小命令行字体

> 放大`"ctrl"+"shift"+"+"`，缩小`"ctrl"+"-"`

## 2.文件夹操作
```
>`ls 显示当前文件夹的文件或文件夹`
>`cd /~	进入文件夹`
>`pwd	当前路径（绝对路径）`
>`cd ..	跳到上一级文件夹（一个点则表示当前路径）`
>`clear	清屏`
>`cd -  跳到上次操作路径`
>`"Tab"	代码补全（按两次的话会显示同首字母文件）`
>// **ls相关命令**
>`ls -a	显示当前隐藏文件`
>`ls -l	以列表的形式显示当前文件夹下的文件`
>`ls -lh	以列表的形式显示当前文件大小`
>`ls -alh	显示所有文件大小（包括隐藏文件大小）`
>//建立文档
>`touch world.txt	创建一个txt文档，建文档时不要后缀名也行`
>//创建目录
>`mkdir A/B/C  haha 创建haha文件夹`
>`tree 以目录树的形式显示文件的结果`
>//删除目录 rmdir
>`rmdir haha 删除空目录`
>//删除文件
>`rm text.txt 删除文件`
>`rm 目录-haha -r 递归删除文件夹`
>`rm text.txt -i 交互式删除文件`
>`rm a/* -r 删除a文件夹中所有文件或文件夹`
>//链接文件
>`ln 源文件 -链接文件 //建立硬链接`
>`ln -s 源文件 -链接文件 //软链接`
>//grep查找文件（指定文件查找内容）
>`grep -n '      ' text.txt //-n命令显示行号，-i忽略大小写`
>`grep -n '^a' text.txt //^a是以a开头,'a$'是以a结尾`
>`grep -n '[tT]' text.txt 满足t或T`
```

```
//复制 cp
cp hello.py 01.py //复制hello.py到01.py
//-r 递归复制
cp o* a/ -a
cp o* a/ -r
```
```
//mv移动文件（剪切）/重命名
mv a d
mv ab.txt bc.txt //相当于重命名
mv ab.txt bc.txt -i //交互式移动
```
```
//打包 tar
tar -cvf text.tar * //-v表示进度，text.tar是压缩文件名，*表示所有文件
//解压
tar -xvf text.tar
//压缩 gzip
gzip text.tar
//解压
gzip -d xxx.tar.gz
//比较实用的
tar -zcvf text.tar.gz * //打包
tar -zxvf text.tar.gz //解压
tar -zxvf text.tar.gz -c text/  //解压到指定路径
//zip压缩
unzip -d 解压路径
```
## 3.通配符的巧妙使用
```
> `ls *.txt   显示当前文件下所有后缀名为.txt的文件`
> `ls *.*	显示带有后缀名的文件名`
> `ls *.t?t 显示后缀名为t?t的文件`
> `ls *.t[xn]t 显示txt或者tnt文件`
> `ls *.t[a-f]t 显示tat、tbt、...、tft的文件`
> `ls \*a "\"转义字符，显示*a文件`
> `ls *a	显示～a的文件`
```

## 4.重定向
```
>`ls > text.txt 将ls输出的结果显示在text.txt中`
>`ls >> text.txt 在原来的text.txt的末尾显示ls的输出结果`
```

## 5.分屏显示：more

>`cat显示文件内容，不会分屏`
>`more text.txt`
>`gedit text.txt 打开text.txt文件`
>`ls -alh | more 一行执行多行命令"|"`

## 6.查看帮助文档

```
ls --help
man //eg man ls
man 2|3 print //man+函数名显示函数相关信息
history //显示终端输入命令历史记录
```
```
//查找文件：find(指定路径找文件)
find 路径 -name '0*'
find ./ -name '...' 当前文件夹下查找
```
## 7.Linux相关命令

```
ifconfig //查询本机ip(linux)
ipconfig //查询本机ip(windows)

//ping
ping 192.168.17.76 测试网络连接是否正常

//ssh 远程登录
ssh python@192.168.17.76
ssh 用户名@ip

who 查看当前系统有那些人登录
whami 查找当前登录用户
exit 登出

useradd 添加用户帐号
sudo useradd Alien -m -d /home/alien // -m自动创建家目录文件夹，-d家目录名
ctrl+a  ctrl+e  //快速跳到行首行尾

//设置密码 passwd
sudo passwd alien
//切换用户
su alien //此时还在当前目录
su - alien //跳到alien家目录

//删除用户
userdel abc(用户名)
userdel -r abc(用户名) 删除用户和用户目录所有文件

//查看用户组
groupmod
cat /etc/group

//添加用户及指定用户组
useradd Alien -m -d /home/alien -g ...
//修改用户组
usermod -g 用户组 用户名
username -a -g 用户组 用户名
sudo usermod -a -G adm 用户名
sudo username -a -G sudo 用户名

//修改文件权限chmod 
//r(1)w(2)x(4)
chmod u+x text.txt
chmod o+x text.txt
chmod u=rwx 2.py
chmod a=r 2.py
chmod a=  2.py
chmod 444 2.py
sudo 777 myshare -R 修改myshare及内部所有权限

car //查看日历
date //查看时间
//date 0102030420180410(月日时分年秒)

//查看进程ps
ps -aux 查看所有进程
top //动态显示当前系统程序员资源占用情况
kill pid
kill -9 10367

//关机重启
reboot //重启
shutdown -r now //重新启动
shutdown -h now //立刻关机
shutdown -h 20:25 //今天20：25关机
shutdown -h +10 //10min后关机
int 0 //关机
int 1 //重启

//检查磁盘空间：df
df -m //单位M
//查看目录占用空间
du -h //合适的单位
```
## 8.Vi命令

```
//vi模式：1.命令模式;2.编辑模式;3.末行模式
1----2 //i/a/o
2----1 //ESC
1----3 //：
3----1 //ESC

shift +Z+Z //保存退出

3----  //shift+:
q! //不保存强制退出 
wq //保存退出
x 保存退出
X 加密

自动补全
ctrl +n 
ctrl +p

//光标
I 左 A（a）右
O 上 o 下

//命令模式
hjkl 控制上下左右
M 中间位置
L 当前屏幕最后一行
yy 复制，8yy从当前光标所在行开始复制8行
p 复制
dd 剪切，8dd从当前光标所在行开始剪切8行
u 撤销
ctrl + r反撤销
G 跳到最后一行
2G 跳到第二行
w 向右跳
{ 往回跳
} 往下跳
ctrl +d 向下跳半屏
ctrl +u向上跳半屏
ctrl +f向下跳一屏
ctrl +b向上跳一屏
```
## 9.Linux目录介绍

```
/lost+fount:系统错误异常文件存放处
/mut:/media:光盘默认挂载点，/mut/cdrom也行
/opt:主机额外软件摆放目录
/proc:此目录下数据都在内存中，不占用磁盘空间
/sbin、/usr/sbin、/usr/local/sbin：放置系统管理员使用可执行命令
/tmp:程序执行时临时存放文件目录
/srv:服务启动时需要访问的数据目录
/usr:应用程序存放目录
/usr/bin:存放应用程序
/usr/share:存放共享数据
/usr/lib：程序运行必须的库函数
/usr/local：存放软件升级包
/usr/share/doc:系统说明文件存放目录
/usr/share/man:程序说明文件存放目录
/var:日志文件，系统执行过程中经常变化的文件
/var/log/message:所有的登录文件存放目录
/var/spool/mail:邮件存放目录
/var/run:程序或服务启动后，其PID存放在该目录下
```



