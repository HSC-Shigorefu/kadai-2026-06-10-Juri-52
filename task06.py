import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import setuptools


df = pd.read_csv("sales_clean.csv")

# TODO 1: 単価の分布をヒストグラムで表示してください
# ヒント:
# ヒストグラムは、数値データがどの範囲に多いかを見るためのグラフです。
# plt.hist(データ, bins=数) を使います。
# bins は棒の数です。
plt.hist(df["単価"],bins=30)

# TODO 2: グラフのタイトルを設定してください
plt.title("単価分布")

# TODO 3: x軸の名前を設定してください
plt.xlabel("単価")

# TODO 4: y軸の名前を設定してください
plt.ylabel("件数")

plt.show()