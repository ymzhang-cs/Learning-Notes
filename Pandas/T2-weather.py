"""
当前有北上广深沈五地空气质量数据，绘制五个城市PM2.5的随时间变化的折线图
"""

import pandas as pd

pd.set_option('display.max_columns', None)

############################
# 1. 读取数据
############################

file_paths = ["datasets/weather/BeijingPM20100101_20151231.csv",
              "datasets/weather/GuangzhouPM20100101_20151231.csv",
              "datasets/weather/ShanghaiPM20100101_20151231.csv",
              "datasets/weather/ChengduPM20100101_20151231.csv",
              "datasets/weather/ShenyangPM20100101_20151231.csv"]

city_names = ['北京', '广州', '上海', '成都', '沈阳']

############################
# 2. 数据预处理
############################

df_list = []

for file_path in file_paths:
    # 读取数据
    df = pd.read_csv(file_path)

    # 处理时间
    df['datetime'] = pd.to_datetime(
        df['year'].astype(str)+'-'+df['month'].astype(str)+'-'+df['day'].astype(str)+' '+df['hour'].astype(str)+':00:00')

    df.set_index('datetime', inplace=True)

    df_list.append(df)