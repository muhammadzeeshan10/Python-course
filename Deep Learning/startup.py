# import pandas as pd
# df=pd.read_csv('Startups in 2021 end.csv')

# print(df)
# print(df.columns)

# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.countplot(data=df,x='Valuation ($B)')
# plt.xticks(rotation=90)
# plt.show()

# def filter_val(rating):
#     return int(rating>2)

# x=df[['Company','City','Industry']]
# y=df['Valuation ($B)'].apply(filter_val)

# def lower(text):
#     if isinstance(text,float):
#         return '<UNK>'
#     else:
#         return text.lower()
    

# x['Company']=df['company'].apply(lower)
# x['City']=df['City'].apply(lower)
# x['Industry']=df['Industry'].apply(lower)


# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# stop_words=stopwords.words('English')

# def remove_stopwords(text):
#     no_stops=[]

#     for word in text.split():
#         if word not in stop_words:
#             no_stops.append(text)
#     return " ".join(no_stops)
    

# x['Company']=df['company'].apply(remove_stopwords)
# x['City']=df['City'].apply(remove_stopwords)
# x['Industry']=df['Industry'].apply(remove_stopwords)

# import re 
# def remove_punctuation(text):
#     return re.sub(r'[^a-zA-Z0-9]',' ',text)


# x['Company']=x['company'].apply(remove_punctuation)
# x['City']=x['City'].apply(remove_punctuation)
# x['Industry']=x['Industry'].apply(remove_punctuation)


# from nltk.stem import WordNetLemmatizer
# lemm=WordNetLemmatizer()

# x['Company']=df['company'].apply(lambda x:lemm.lemmatize(x))
# x['City']=df['City'].apply(lambda x:lemm.lemmatize(x))
# x['Industry']=df['Industry'].apply(lambda x: lemm.lemmatize(x))

# x['text']=x['City']+" "+x['Company']+" "+x['Industry']


# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test=train_test_split(x['text'],
#                                                y,
#                                                test_size=.6,
#                                                random_state=25)


# from tensorflow.keras.preprocessing.text import Tokenizer
# tokenizer=Tokenizer(no_words=10000,oov_token='<oov>')
# tokenizer.fit_on_texts(x_train)
# train_seq=tokenizer.texts_to_sequences(x_train)
# test_seq=tokenizer.texts_to_sequences(x_test)

# from tensorflow.keras.utils import pad_sequences
# train_pad=pad_sequences(train_seq,
#                         maxlen=40,
#                         truncating='post',
#                         padding='post')


# test_pad=pad_sequences(test_seq,
#                         maxlen=40,
#                         truncating='post',
#                         padding='post')


# from tensorflow import keras

# model=keras.models.sequential()

# model.add(keras.layers.Embadding(10000,128))
# model.add(keras.layers.simpleRNN(64,return_sequences=True))
# model.add(keras.layers.SimpleRNN(64))
# model.add(keras.layers.Dense(128, activation="relu"))
# model.add(keras.layers.Dropout(0.4))
# model.add(keras.layers.Dense(1, activation="sigmoid"))


# from keras.metrics import Recall,Precision

# MKETRICES=metrices=['accuracy',Precision(name='precision'),
#                     Recall(name='recall')]

# model.compile("rmsprop",
#               "binary_crossentropy",
#                metrics = MKETRICES)

# history = model.fit(train_pad,
#                     y_train,
#                     epochs=5,
#                     validation_split=0.2)

# print("Summary:                  \n" , model.summary())

# -------------------------
# 1️⃣ Import Libraries
# -------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences
from tensorflow import keras
from keras.metrics import Precision, Recall

# -------------------------
# 2️⃣ Load CSV
# -------------------------
df = pd.read_csv('Startups in 2021 end.csv')
print(df.head())
print(df.columns)

# -------------------------
# 3️⃣ Clean 'Valuation ($B)' column
# -------------------------
df['Valuation ($B)'] = df['Valuation ($B)'].str.replace('$','', regex=False).astype(float)

# -------------------------
# 4️⃣ Plot Valuation counts
# -------------------------
sns.countplot(data=df, x='Valuation ($B)')
plt.xticks(rotation=90)
plt.show()

# -------------------------
# 5️⃣ Binary target (>2B)
# -------------------------
def filter_val(rating):
    return int(rating > 2)

x = df[['Company', 'City', 'Industry']]
y = df['Valuation ($B)'].apply(filter_val)

# -------------------------
# 6️⃣ Text Preprocessing
# -------------------------
# Lowercase
def lower(text):
    if isinstance(text, float):
        return '<UNK>'
    return text.lower()

x['Company'] = x['Company'].apply(lower)
x['City'] = x['City'].apply(lower)
x['Industry'] = x['Industry'].apply(lower)

# Stopwords removal
nltk.download('stopwords')
stop_words = stopwords.words('english')

def remove_stopwords(text):
    words = [word for word in text.split() if word not in stop_words]
    return " ".join(words)

x['Company'] = x['Company'].apply(remove_stopwords)
x['City'] = x['City'].apply(remove_stopwords)
x['Industry'] = x['Industry'].apply(remove_stopwords)

# Remove punctuation
def remove_punctuation(text):
    return re.sub(r'[^a-zA-Z0-9 ]', ' ', text)

x['Company'] = x['Company'].apply(remove_punctuation)
x['City'] = x['City'].apply(remove_punctuation)
x['Industry'] = x['Industry'].apply(remove_punctuation)

# Lemmatization
lemm = WordNetLemmatizer()
x['Company'] = x['Company'].apply(lambda t: lemm.lemmatize(t))
x['City'] = x['City'].apply(lambda t: lemm.lemmatize(t))
x['Industry'] = x['Industry'].apply(lambda t: lemm.lemmatize(t))

# Combine text
x['text'] = x['City'] + " " + x['Company'] + " " + x['Industry']

# -------------------------
# 7️⃣ Train-test split
# -------------------------
x_train, x_test, y_train, y_test = train_test_split(
    x['text'], y, test_size=0.6, random_state=25
)

# -------------------------
# 8️⃣ Tokenizer & Padding
# -------------------------
tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
tokenizer.fit_on_texts(x_train)

train_seq = tokenizer.texts_to_sequences(x_train)
test_seq = tokenizer.texts_to_sequences(x_test)

train_pad = pad_sequences(train_seq, maxlen=40, padding='post', truncating='post')
test_pad = pad_sequences(test_seq, maxlen=40, padding='post', truncating='post')

# -------------------------
# 9️⃣ Build RNN Model
# -------------------------
model = keras.models.Sequential()
model.add(keras.layers.Embedding(10000, 128))
model.add(keras.layers.SimpleRNN(64, return_sequences=True))
model.add(keras.layers.SimpleRNN(64))
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(1, activation='sigmoid'))

# Metrics
METRICS = ['accuracy', Precision(name='precision'), Recall(name='recall')]

# Compile model
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=METRICS)

# -------------------------
# 🔟 Train Model
# -------------------------
history = model.fit(train_pad, y_train, epochs=5, validation_split=0.2)

# -------------------------
# 1️⃣1️⃣ Model Summary
# -------------------------
print(model.summary())
