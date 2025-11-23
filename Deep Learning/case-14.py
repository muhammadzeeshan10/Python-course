import pandas as pd
df=pd.read_csv('Clothing-Review.csv')

print(df)
print(df.head())
print(df.columns)

import seaborn as sns
import matplotlib.pyplot as plt

# Remove Empty row each column in df
df=df[df['Class Name'].isnull()==False]
print(df)

# Show Complete Rating of CSV file
sns.countplot(data=df ,x='Class Name')
plt.xticks(rotation=90)
plt.show()

# Show Specific column 
sns.countplot(data=df,x='Rating')
plt.show()

plt.subplot()
plt.subplot(1,2,1)
sns.countplot(data=df,x='Rating')

plt.subplot()
plt.subplot(1,2,2)
sns.countplot(data=df, x='Recommended IND')
plt.show()



features=['Class Name', 'Title', 'Review Text']

x=df[features]
y=df['Rating']

# Here Apply filter Function
y=y.apply(filter)

def filter(rating):
    return int(rating>3)

#  check type {isinstance}
def tolower(text):
    if isinstance(text,float):
        return '<UNK>'
    else:
        return text.lower()

import nltk
nltk.download('all') 
from nltk.corpus import stopwords


stop_words=stopwords.words("english")

# remove stop word apply for loop in each sentence
def remover_stopwords(text):
    no_stop=[]
    for word in text.split(' '):
        if word not in stop_words:
            no_stop.append(word)
    return  " ".join(no_stop)

# Import re ko hmm punctuation remove krnatye kai liyee used krtaye ha
import re
def remove_punctuation(text):
    return re.sub(r'[^a-zA-Z0-9]',' ',text)


x['Title']=x['Title'].apply(tolower)
x['Title']=x['Title'].apply(remover_stopwords)

x['Review Text']=x['Review Text'].apply(tolower)
x['Review Text']=x['Review Text'].apply(remover_stopwords)


#  used Lemmatizer to convert word like beautiful to beauty
from nltk.stem import WordNetLemmatizer
lemm=WordNetLemmatizer()

x['Title']=x['Title'].apply(lambda x:lemm.lemmatize(x))
x['Review Text']=x['Review Text'].apply(lambda x:lemm.lemmatize(x))


x['Title']=x['Title'].apply(remove_punctuation)
x['Review Text']=x['Review Text'].apply(remove_punctuation)

# Merge
x['Text']=list(x['Title']+x['Review Text']+x['Class Name'])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x['Text'],y,
                                               test_size=.5,
                                               random_state=38)

from nltk.tokenize import word_tokenize

from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer=Tokenizer(num_words=10000,oov_token='<OOV>')
tokenizer.fit_on_texts(x_train)

train_seq = tokenizer.texts_to_sequences(x_train)
test_seq = tokenizer.texts_to_sequences(x_test)
# train_seq = training data sequences (already tokenized numbers)

# maxlen=40 = har sentence ki final length 40 hogi

# padding="post" = agar sentence 40 se chhota hai → baaki jagah pe 0 lagayega (baad mein)

# truncating="post" = agar sentence 40 se zyada lamba hai → sentence ko aakhir se cut karega

from tensorflow.keras.utils import pad_sequences
train_pad = pad_sequences(train_seq,
                          maxlen=40,
                          truncating="post",
                          padding="post")
test_pad = pad_sequences(test_seq,
                         maxlen=40,
                         truncating="post",
                         padding="post")

import tensorflow
from tensorflow import keras
model = keras.models.Sequential()
#  Embedding convert into vector shape
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
                    epochs=5)

print("Summary:                  \n" , model.summary())

