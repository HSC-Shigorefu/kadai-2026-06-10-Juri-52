import pandas as pd

# =========================================
# task01: 売上データをきれいにする
# =========================================

df = pd.read_csv("sales_dirty.csv")
print(df.shape)
print(df.columns)

# TODO 1: 欠損値の数を表示してください
print(df.isna().sum())

# TODO 2: 重複している行を削除してください
df = df.drop_duplicates(keep="last")

# TODO 3: 店舗、カテゴリなどの前後の空白を削除してください
df["店舗"] = df["店舗"].str.strip()
df["カテゴリ"] = df["カテゴリ"].str.strip()
df["商品名"] = df["商品名"].str.strip()
df["支払方法"] = df["支払方法"].str.strip()
df["担当者"] = df["担当者"].str.strip()

# TODO 4:　単価の「¥」、NaNなどを削除してください。また、単価の「,」を削除してください
df["単価"] = df["単価"].astype(str).str.replace({"¥":"",",":""},regex=False)
df["単価"] = pd.to_numeric(df["単価"],errors="coerce")

# TODO 5: 数量を数値に変換してください
df["数量"] = pd.to_numeric(df["数量"],errors="coerce")

# TODO 6: 割引率の欠損値を 0 にしてください
df["割引率"] = df["割引率"].fillna(0)

# TODO 7: 数量の欠損値を 1 にしてください
df["数量"] = df["数量"].fillna(1)

# TODO 8: 単価の欠損値を単価の中央値で補完してください
# ヒント:
# 中央値は、データを小さい順に並べたときに真ん中にある値です。
# 平均値よりも、極端に高い値・低い値の影響を受けにくいです。
# pandas では .median() を使うと中央値を計算できます。
# 例:# df["価格"].median()
df["単価"] = df["単価"].fillna(df["単価"].median())

# TODO 9:　店舗、カテゴリ、商品名、支払方法の欠損値を「不明」にしてください
df["店舗"] = df["店舗"].fillna("不明")
df["カテゴリ"] = df["カテゴリ"].fillna("不明")
df["商品名"] = df["商品名"].fillna("不明")
df["支払方法"] = df["支払方法"].fillna("不明")

# TODO 10: 日付を datetime 型に変換し、日付が変換できなかった行を削除してください。
df["日付"] = pd.to_datetime(df["日付"],errors="coerce", format="mixed")
df = df.dropna(subset=["日付"])

# TODO 11: 売上金額という新しい列を作ってください
# 計算式: 単価 × 数量 × (1 - 割引率 / 100)
df["売上金額"] = round(df["単価"] * df["数量"] * (1 - df["割引率"] / 100))

# TODO 12: 年月という新しい列を作ってください
# 例: 2024-01
# ヒント:
# 下の例は「日」単位で取り出す例です。
# 年月だけを取り出したい場合は、どこを変えればよいか考えてください。
# D は Day（日）の意味です。
# M は Month（月）の意味です。
# 例:
# df["日"] = df["日付"].dt.to_period("D").astype(str)
df["年月"] = df["日付"].dt.to_period("M").astype(str)

# TODO 14: 完成したデータの最初の5行を表示してください
print(df.head(5))

# TODO 15: 欠損値の数をもう一度表示してください
print(df.isna().sum())

print(df)
df.to_csv("sales_clean.csv",index=False)
