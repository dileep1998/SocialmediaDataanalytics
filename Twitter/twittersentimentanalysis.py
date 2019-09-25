from textblob import TextBlob
import unidecode
import pandas as pd

# Tweeter search with keyword
df=pd.read_csv("/home/dileep/my_flask_app/result.csv")
counter = 0
x=df.shape
tweet=df['text']
for a in tweet:
    text = a
    text = unidecode.unidecode(text)   
    text_blob = TextBlob(text)
    polarity = text_blob.polarity
    subjectivity = text_blob.subjectivity
    print(polarity)
    counter = counter + 1
    if (counter == x[0] ):
        break







