'''
Developer_="Arunav Pratap Shandeelya"
_College_="IIIT Bhubaneswar"
_Mentor_="Dr. Rakesh Chandra Balbantray"
_Project_="Sentence Compression Using LSTM Architecture of word Cateogrization"
_Version_="1.0"
_Status_="Under Development"

Aim: A prtotype to summarize the long phrase sentences
Contributor: Arunav Shandilya
			Sthita Pragyan Pujari

This model is for 3 word window architecture (3 word at each time step)
'''

import os
import numpy as np
import argparse
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.layers import LSTM
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from config import DATA_PATH
np.random.seed(0)

parser = argparse.ArgumentParser()
parser.add_argument('--glove_file', default='/data/embeddings/glove.840B.300d.txt')
parser.add_argument('--original', default='/data/train/google-original-sentence.txt', help='raw input sentences')
parser.add_argument('--compressed', default='/data/train/google-compressed-sentence.txt', help='target sentences')
parser.add_argument('--epoch',type=int, default=5, help='number of iterations')
arg = parser.parse_args()

X=[]
with open(DATA_PATH + arg.original,'r',encoding="utf8") as f:
	for i in f:
		if i=='\n':
			continue
		X.append(i.strip().split())


all_words = set(w for words in X for w in words)
all_words.add("#2103")

glove= {}
total_words=[]
with open(DATA_PATH + arg.glove_file, "rb") as infile:
    for line in infile:
        parts = line.split()
        word = parts[0].decode("utf8")
        if (word in all_words):
            nums=np.array(parts[1:], dtype=np.float32)
            total_words.append(word)
            glove[word] = nums
    words_np=list(all_words-set(total_words))
    #print(words_np)
    for word in words_np:
        if word=="#2103":
            continue
        glove[word]=np.ones((300,1))
    glove["#2103"]=np.zeros((300,1))


Y=[]
f3 = open(DATA_PATH + arg.compressed,"r",encoding="utf8")
for i in f3:
	if i=='\n':
		continue
	Y.append(i.strip().split())

Y1=[]
for i in range(len(X)):
	a=set(Y[i])
	words=X[i]
	for j in words:
		if j in a:
			Y1.append(1)
		else:
			Y1.append(0)

X1=[]
for i in range(len(X)):
    for j in range(len(X[i])):
        str1=  " "
        if j==0:
            str1=str1+"#2103 #2103 "+str(X[i][j])
        elif j==1:
            str1=str1+"#2103 "+str(X[i][j-1])+" "+str(X[i][j])
        else:
            str1=str1+str(X[i][j-2])+" "+str(X[i][j-1])+" "+str(X[i][j])
        X1.append(str1.strip())

tokenizer = Tokenizer(num_words=22600)
tokenizer.fit_on_texts(list(all_words))
X1=tokenizer.texts_to_sequences(X1)
X1=pad_sequences(X1,maxlen=3,padding="post",value=0)

X_train, X_test, y_train, y_test = train_test_split(X1,Y1, test_size=0.3, shuffle=False)

embedding_matrix = np.zeros((len(all_words), 300))
for word, i in tokenizer.word_index.items():
    embedding_vector = glove.get(word)
    if embedding_vector is not None:
        embedding_matrix[i,:] = list(embedding_vector)

model = Sequential()
model.add(Embedding(len(all_words),300,weights=[embedding_matrix],input_length=3,trainable=False))
model.add(LSTM(3,return_sequences=True))
model.add(LSTM(3))
model.add(Dense(3,activation='relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, y_train, epochs=10, batch_size=16)
scores = model.evaluate(X_test, y_test, verbose=0)
print (scores)