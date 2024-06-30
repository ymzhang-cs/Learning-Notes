from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib
import random

# Demos of Matplotlib
# https://matplotlib.org/stable/gallery/index.html

# 绘制气温变化折线图 plot

# 数据点，要求可迭代
x = range(2, 26, 2)
y_1 = [random.randint(20, 35) for i in range(12)]
y_2 = [random.randint(20, 35) for i in range(12)]

#############################################
# 绘图部分
#############################################

############
# 设置图片大小
############
# 若figsize=(5, 5), dpi=300，则分辨率为1500x1500
# dpi大小同时决定了文字大小和线条宽度

plt.figure(figsize=(10, 8), dpi=300)

############
# 设置字体
############

# 方法1：matplotlib.rc

# font = {
#     'family': 'Microsoft YaHei',
#     'weight': 'normal',
#     'size': '11'
# }
# matplotlib.rc('font', **font)

# 方法2：font_manager
# 要在加入文字时写上 fontproperties 属性指向该变量

my_font = font_manager.FontProperties(family='Source Han Sans CN',
                                      size=14)

#######################
# 设置刻度
#######################

# 设置x轴刻度
# 传入的是显示所有刻度的可迭代对象
_x = x
_x_label = [f"{i}时" for i in _x]
plt.xticks(_x, _x_label, rotation=0, fontproperties=my_font)

# 设置y轴刻度
plt.yticks(range(20, 36)[::2], fontproperties=my_font)

#######################
# 添加坐标轴标题
#######################
plt.xlabel("时间/h", fontproperties=my_font)
plt.ylabel("温度/℃", fontproperties=my_font)
plt.title("气温变化情况", fontproperties=my_font)

#######################
# 绘制网格
#######################

plt.grid(alpha=0.4)     # alpha设置不透明度

#######################
# 绘制折线
#######################
plt.plot(x, y_1,
         label='海淀',
         color='r',         # (r,g,b), w, (c,m,y,k), #abcdef
         linestyle='--',    # -, --, -., :, ''留空或空格
         linewidth=2,
         alpha=0.7)
plt.plot(x, y_2, label='东城')

# 显示图例，文字来自plot的label
plt.legend(prop=my_font, loc='best')    # loc用来设置图例的位置，best表示自适应

#######################
# 导出图像
#######################
plt.savefig('./01.png')
plt.savefig('./01.svg')     # SVG矢量图

#######################
# 展示图形，notebook里可以不写
#######################
plt.show()
