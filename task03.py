import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

df = pd.read_csv("sales_clean.csv")

# TODO 1: 店舗ごとの売上金額を合計してください
sales = df.groupby("店舗")["売上金額"].sum()

# TODO 2: 売上が多い順に並べ替えてください
sales = sales.sort_values(ascending=False)

# TODO 3: 横棒グラフを作ってください
plt.figure(figsize=(10,5))
plt.title("店舗別売上")
sales = sales.sort_values()
plt.barh(sales.index,sales.values)
plt.xlabel("売上")
plt.ylabel("カテゴリ")
plt.ticklabel_format(style="plain",axis="x")
plt.show()