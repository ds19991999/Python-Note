#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

# 生成三角函数
x = np.linspace(-np.pi,np.pi)
c,s = np.cos(x),np.sin(x)

# 设置图像大小
f = plt.figure(figsize=(10,6), dpi=80)

# 画图，指定颜色，线宽，类型
plt.plot(x, c, 'b-', 
         x, s, 'r-', linewidth=2.5)

# 设置显示范围
plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(c.min() * 1.1, c.max() * 1.1)

#######################################移动坐标轴############################################
# 得到轴的句柄
ax = plt.gca()
# ax.spines参数表示四个坐标轴线
# 将右边和上边的颜色设为透明
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 将 x 轴的刻度设置在下面的坐标轴上、设置位置
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))

# 将 y 轴的刻度设置在左边的坐标轴上、设置位置
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
############################################################################################

# 设置刻度及其标识,标识和刻度对应
p = plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], 
           ['$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$', '$\pi$'], fontsize ='xx-large')
p = plt.yticks([-1.,-0.5,0,0.5, 1.], 
           ['$-1.$','$-0.5$', '$0$','$0.5$ ','$+1.$'], fontsize ='xx-large')

# 加入图例frameon表示图例周围是否需要边框
legend = plt.legend([r'$\cos(x)$', r'$sin(x)$'],
               loc='upper left', frameon=True)

#----------------------------数据点、虚线、文本、显示特殊点值------------------------------#
# 数据点
t = 2*np.pi/3
# 蓝色曲线
plt.plot([t,t],[0,np.cos(t)],
         color='blue',linewidth=2.5,linestyle="--")
# 该点处的cos值
plt.scatter([t,],[np.cos(t),],50,color='blue')
# 在该点处显示文本
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',# 文本
             xy = (t,np.sin(t)),# 数据点坐标位置
             xycoords='data',# 坐标相对干数据
             xytext=(+10,+30),# 文本位置坐标
             textcoords='offset points',# 坐标相对干数据点的坐标
             fontsize=16,# 文本大小
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))# 箭头样式

# 红色虚线
p = plt.plot([t,t],[0,np.sin(t)], 
             color ='red', linewidth=2.5, linestyle="--")
# 该点处的 sin 值
p = plt.scatter([t,],[np.sin(t),], 50, color ='red')
# 显示文本
p = plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
#------------------------------------------------------------------------------------------#

# 设置坐标轴刻度文本
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    # 这里是关键语句
    # label.set_bbox(dict(facecolor='black', edgecolor='None', alpha=0.65 ))
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))

# 显示网格
plt.grid(True)

# 在脚本中需要加上这句才会显示图像
plt.show()