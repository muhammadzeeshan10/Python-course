import pandas as pd

df=pd.read_csv('Clothing-Review.csv')

print(df.columns)
print(df.head())

import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(data=df,x='Age')
plt.xticks(rotation=90)
plt.show()

plt.subplot()
plt.subplot(1,2,1)
sns.countplot(data=df,x='Recommended IND')
plt.xticks(rotation=90)

plt.subplot()
plt.subplot(1,2,2)
sns.countplot(data=df,x='Rating')
plt.show()

features=['Department Name','Division Name','Review Text']

x=df[features]
y=df['Rating']

def filter(rating):
    return int(rating>3)

def lower(text):
    if isinstance(text,float):
        return '<UNK>'
    else:
        return text.lower()
    
import nltk
nltk.download('all')
from nltk.corpus import stopwords

stop_words=stopwords.words('English')

def remove_stopwords(text):
    no_stop=[]
    for word in text.split(' '):
        if word not in stop_words:
            no_stop.append(word)
    return " ".join(no_stop)

import re
def remove_punctuation(text):
    return re.sub(r'[^a-zA-Z0-9]',' ',text)

x['Department Name']=x['Department Name'].apply(lower)
x['Division Name']=x['Division Name'].apply(lower)
x['Review Text']=x['Review Text'].apply(lower)

x['Department Name']=x['Department Name'].apply(remove_stopwords)
x['Division Name']=x['Division Name'].apply(remove_stopwords)
x['Review Text']=x['Review Text'].apply(remove_stopwords)

x['Department Name']=x['Department Name'].apply(remove_punctuation)
x['Division Name']=x['Division Name'].apply(remove_punctuation)
x['Review Text']=x['Review Text'].apply(remove_punctuation)

from nltk.stem import WordNetLemmatizer
lemm=WordNetLemmatizer()

x['Department Name']=x['Department Name'].apply(lambda x:lemm.lemmatize(x))
x['Division Name']=x['Division Name'].apply(lambda x:lemm.lemmatize(x))
x['Review Text']=x['Review Text'].apply(lambda x:lemm.lemmatize(x))

# merge
x['text']=list(x['Department Name']+x['Division Name']+x['Review Text'])

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,
                                               y,
                                               test_size=.6,
                                               random_state=33)

from nltk.tokenize import word_tokenize
from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer=Tokenizer(num_words=10000,oov_token='<OOV>')
tokenizer.fit_on_texts(x_train)

train_seq=tokenizer.texts_to_sequences(x_train)
test_seq=tokenizer.texts_to_sequences(x_test)

from tensorflow.keras.utils import pad_sequences
train_pad=pad_sequences(train_seq,
                       maxlen=40,
                       truncating="post",
                       padding="post")

test_pad=pad_sequences(test_seq,
                      maxlen=40,
                      truncating="post",
                      padding="post")

from tensorflow import keras    

model = keras.models.Sequential()

model.add(keras.layers.Embedding(10000, 128))
model.add(keras.layers.SimpleRNN(64, return_sequences=True))
model.add(keras.layers.SimpleRNN(64))
model.add(keras.layers.Dense(128, activation="relu"))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(1, activation="sigmoid"))

from keras.metrics import Precision, Recall

METRICS = metrics=['accuracy', 
                   Precision(name='precision'),
                   Recall(name='recall')]


model.compile("rmsprop",
              "binary_crossentropy",
               metrics = METRICS)

history = model.fit(train_pad,
                    y_train,
                    epochs=5,
                    validation_split=0.2)

print("Summary:                  \n" , model.summary())

