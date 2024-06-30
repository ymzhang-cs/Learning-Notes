import pandas as pd

pd.set_option('display.max_columns', None)

data = pd.read_csv("datasets/directory.csv")

# Group by

# grouped = data['Brand'].groupby(by=[data["Country"], data["State/Province"]]).count()

grouped = data.groupby(by=["Country", "State/Province"])['Brand'].count()

print(grouped)

CN_data = data[data["Country"] == "CN"]

province_count = CN_data["State/Province"].value_counts()

print(province_count)