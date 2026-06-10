import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools

df = pd.read_csv("sales_clean.csv")

# TODO 1: 支払方法ごとの件数を数えてください
count = df["支払方法"].value_counts()

# TODO 2: 円グラフを作ってください
plt.figure(figsize=(5,5))
plt.title("支払方法使用率")
plt.pie(count,labels=count.index,autopct="%1.1f%%",startangle=90)
plt.show()