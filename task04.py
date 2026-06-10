import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

df = pd.read_csv("sales_clean.csv")

# TODO 1: 年月ごとの売上金額を合計してください
sales = df.groupby("年月")["売上金額"].sum()

# TODO 2: 折れ線グラフを作ってください
plt.figure(figsize=(15,5))
plt.title("月別売上")
plt.plot(sales,marker="o")
plt.xlabel("月")
plt.ylabel("売上")
plt.ticklabel_format(style="plain",axis="y")
plt.show()