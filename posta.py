import email #  mail içeriğini okumak için 
import imaplib #ımap protokolu ile  mail sunucusuna bağlanmayı sağlar 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from email.header  import decode_header
from email.utils import parsedate_to_datetime
import pandas as pd
depo=[]

email_name="uysalbugra134@gmail.com"
uygulama_şifresi="**********"
ımap="imap.gmail.com"
# ssl üzerinden güvenli bağlantı kurar  ve giriş yapar 
mail=imaplib.IMAP4_SSL(ımap)
mail.login(email_name, uygulama_şifresi)


# gelen kutusunu aç
mail.select("inbox")

status , messages= mail.search(None, "ALL") #kriterlere uygun  mail ıd si döndürür 

mail_id=messages[0].split() #  gelen ıd  listesini parçalara ayırır 

for i in mail_id[-1000:]: # son 10 mail için
    i=i.decode()
    status, msg_data=mail.fetch(i , "(RFC822.HEADER)") # sadece mail başlıklarını alır 
    raw_msg=msg_data[0][1]
    msg=email.message_from_bytes(raw_msg) # çıkan bytes versini   okunabilir hale çeviri 

    dt=parsedate_to_datetime(msg["Date"])


    depo.append({ "kimden":msg["From"], "Kime":msg["To"] , "konu":msg["Subject"],  "tarih":msg["Date"] ,"Saat":dt.strftime("%H:%M") , "Gün": dt.strftime("%A"), "Ay":dt.month , "yıl":dt.year , "İçerik türü":msg["Content-Type"]})


df=pd.DataFrame(depo)



df.to_csv("C:\\Users\\buğra\\Desktop\\mi.csv")


print(df.info())
print(df.dtypes)
print(df.shape)
print(df.columns)
print(df.index)
print(df.head())
print(df.tail())
print(df.describe)
print(df.nunique())
print(df.memory_usage())
print(df.value_counts()) # tüm satırların tekrar sayılarını verir
print(df.duplicated().sum()) # kaç tane  tekrar eden satır var
print(df.isnull().sum())

