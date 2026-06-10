import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

df = pd.read_csv("sales_clean.csv")

# TODO 1: 割引率と売上金額の散布図を作ってください
plt.scatter(df["割引率"],df["売上金額"])
plt.xlabel("割引率")
plt.ylabel("売上金額")
plt.grid(True)
plt.show()

# TODO 2: 割引率と数量の散布図を作ってください
plt.scatter(df["割引率"],df["数量"])
plt.xlabel("割引率")
plt.ylabel("数量")
plt.grid(True)
plt.show()

# TODO 3: 単価率と売上金額の散布図を作ってください
plt.scatter(df["単価"],df["売上金額"])
plt.xlabel("単価")
plt.ylabel("売上金額")
plt.grid(True)
plt.show()

# ヒント:
# 散布図は、2つの数値の関係を見るためのグラフです。
# plt.scatter(xのデータ, yのデータ) を使います。