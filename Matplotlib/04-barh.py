from matplotlib import pyplot as plt
from matplotlib import font_manager


# 数据点

film_names = [
    "云边有个小卖部",
    "海关战线",
    "寂静之地：入侵日",
    "头脑特工队2",
    "来福大酒店",
    "我才不要和你做朋友呢",
    "出发",
    "排球少年!! 垃圾场决战",
    "加菲猫家族",
    "扫黑·决不放弃",
    "唤醒者",
    "再会长江",
    "沙漏",
    "绝地战警：生死与共",
    "谈判专家",
    "疯狂的麦克斯：狂暴女神",
    "传说",
    "机器人之梦",
    "走走停停",
    "永不消逝的电波"
]

cumulative_box_office = [
    37655.52,
    8419.10,
    8127.45,
    18333.11,
    4677.43,
    20093.90,
    141.43,
    11885.12,
    17624.44,
    19138.08,
    205.58,
    864.37,
    2795.49,
    3532.15,
    15592.12,
    5943.01,
    24.67,
    1011.94,
    10222.43,
    110.03
]

# sort by cumulative box office
film_names = [film for _, film in sorted(zip(cumulative_box_office, film_names))]
cumulative_box_office = sorted(cumulative_box_office)

_x = range(len(film_names))
_y = cumulative_box_office

# 设置字体
my_font = font_manager.FontProperties(family='Source Han Sans CN', size=14)

# 设置图片大小
plt.figure(figsize=(20, 12), dpi=150)

# 绘图
plt.barh(_x, _y, height=0.5, color='orange')

# 设置刻度
plt.yticks(_x, film_names, fontproperties=my_font)

# 设置轴标签
plt.ylabel("电影名称", fontproperties=my_font)
plt.xlabel("累计票房/万元", fontproperties=my_font)

# 设置标题
plt.title("2024年电影票房", fontproperties=my_font)

plt.show()