The e-mails in my e-mail address have 'from', 'To', 'subject', 'date', 'Time', 'Day', 'Month', 'year' and 'Content type I extract the data with Python, transfer them to Excel and visualize them.

## Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import email   
import imaplib 
from email.header  import decode_header
from email.utils import parsedate_to_datetime

## columns
['kimden', 'Kime', 'konu', 'tarih', 'Saat', 'Gün', 'Ay','yıl', 'İçerik türü']
