import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv("C:\\Users\\buğra\\Desktop\\mi.csv", encoding="utf-8")

print(df.columns)


"""  
plt.hist(df["Gün"].dropna(), bins=50)
plt.title("Günler")
plt.grid(True)
plt.show()

da=df["Gün"].value_counts()
da.plot(kind="pie",autopct="%.1f%%")
plt.title("days")
plt.show()

sns.barplot(x=da.index , y=da.values, palette="viridis")
plt.title("gün")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()

mou=df["Ay"].value_counts().head(10)
sns.barplot(x=mou.index, y=mou.values, palette="viridis")
plt.title("en çok geçen aylar")
plt.grid(True)
plt.show()

mou.plot(kind='pie', autopct="%.1f%%")
plt.title("Aylar")
plt.show()

konu=df["konu"].value_counts().head(10)
konu.plot(kind="pie", autopct="%.1f%%")
plt.title("konu")
plt.show()

sns.barplot(x=konu.index , y=konu.values , palette="viridis")
plt.title("konu")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()


kimden=df["kimden"].value_counts().head(10)
kimden.plot(kind='pie', autopct="%.1f%%")
plt.title("Kimden")
plt.show()

kimden.plot(kind='bar')
plt.title("kimden")
plt.grid(True)
plt.show()

sns.barplot(x=kimden.index , y=kimden.values , palette="viridis")
plt.title("kimden ")
plt.grid(True)
plt.xticks(rotation=90)
plt.show() 

kimden=df["kimden"].value_counts().head(10)
kimden.plot(kind='pie', autopct="%.1f%%")
plt.title("Kimden")
plt.show()

kimden.plot(kind='bar')
plt.title("kimden")
plt.grid(True)
plt.show()

sns.barplot(x=kimden.index , y=kimden.values , palette="viridis")
plt.title("kimden ")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()

içerik=df["İçerik türü"].value_counts().head(20)
içerik.plot(kind="pie", autopct="%.1f%%")
plt.title("içerik")
plt.show()

sns.barplot(x=içerik.index , y=içerik.values , palette="viridis")
plt.title("içerik türü")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()



saat=df["Saat"].value_counts().head(20)
sns.barplot(x=saat.index , y=saat.values , palette="viridis")
plt.title("saatler")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()



saat.plot(kind="pie")
plt.title("saat")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()



df.sort_values(by="Ay", ascending=True)
df.sort_values(by="Ay", ascending=False) # büyükden küçüğe  


df.sort_values(by="yıl", ascending=False)
df.sort_values(by="yıl", ascending=True)
df.sort_values(by="Saat", ascending=False)
df.sort_values(by="Saat", ascending=True)

"""  


