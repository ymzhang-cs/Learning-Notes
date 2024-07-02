from matplotlib import pyplot as plt
from matplotlib import font_manager

# 使用Matplotlib绘制气温散点图

# 数据点
data_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22, 23]
data_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12, 13, 6]

x_3 = range(1, 32)
x_10 = range(51, 82)

# 设置字体
my_font = font_manager.FontProperties(family='Source Han Sans CN', size=14)

# 设置图片大小
plt.figure(figsize=(14, 10), dpi=300)

# 绘图
plt.scatter(x_3, data_3, label="3月份")
plt.scatter(x_10, data_10, label="10月份")

# 绘制网格
plt.grid(alpha=0.5)

# 设置刻度
_x = list(x_3) + list(x_10)
_x_label = ["3月{}日".format(i) for i in x_3]
_x_label += ["10月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3], _x_label[::3], rotation=45, fontproperties=my_font)

# 设置轴标签
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度", fontproperties=my_font)

# 设置图例
plt.legend(prop=my_font)

# 设置标题
plt.title("3月份和10月份每天最高气温散点图", fontproperties=my_font)

plt.show()
