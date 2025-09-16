import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv("C:\\Users\\buğra\\Desktop\\mi.csv", encoding="utf-8")

print(df.columns)
mou=df["Ay"].value_counts().head(10)
mou.plot(kind="bar")
plt.title("aylar")
plt.grid(True)
plt.show()

plt.hist(df["Gün"].dropna(), bins=50)
plt.title("aylar")
plt.grid(True)
plt.show()

da=df["Gün"].value_counts()
da.plot(kind="pie",autopct="%.1f%%")
plt.title("days")
plt.show()
