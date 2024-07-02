from matplotlib import pyplot as plt
from matplotlib import font_manager

# 数据点
a = ["猩球崛起3:终极之战", "敦刻尔克", "蜘蛛侠:英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

# 设置字体
my_font = font_manager.FontProperties(family='Source Han Sans CN', size=14)

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=300)

# 绘图
bar_width = 0.2
x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]

plt.bar(x_14, b_14, width=bar_width, label='9月14日')
plt.bar(x_15, b_15, width=bar_width, label='9月15日')
plt.bar(x_16, b_16, width=bar_width, label='9月16日')

# 设置刻度
plt.xticks(x_15, a, fontproperties=my_font)

# 设置轴标签
plt.xlabel("电影名称", fontproperties=my_font)
plt.ylabel("票房（单位：万元）", fontproperties=my_font)

# 设置图例
plt.legend(prop=my_font)

# 设置标题
plt.title("9月14-16日票房对比", fontproperties=my_font)

plt.show()