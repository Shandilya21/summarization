import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.layers import LSTM
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
np.random.seed(0)



X1,Y=[],[]
with open("original.txt",'r',encoding="utf8") as f:
	for i in f:
		if i=='\n':
			continue
		#X.append(i.strip())
		X1.append(i.strip().split())
X=[]
X1=pad_sequences(X1,dtype=str,maxlen=150,padding="post",value=1)

for i in range(len(X1)):
	str1=" "
	for j in X1[i]:
		if j=="1.0":
			str1+=" NAW"
		else:
			str1+=" "+j
	X.append(str1.strip())
#print(X)


all_words = set(w for words in X for w in words.split())
glove= {}
total_words=[]
with open("glove.840B.300d.txt", "rb") as infile:
    for line in infile:
        parts = line.split()
        word = parts[0].decode("utf8")
        if (word in all_words):
            nums=np.array(parts[1:], dtype=np.float32)
            total_words.append(word)
            glove[word] = nums
    total_words.append("NAW")
    words_np=list(all_words-set(total_words))
    glove["NAW"]=np.zeros((300,1))
    #print(words_np)
    for word in words_np:
    	glove[word]=np.ones((300,1))
X=[]
X1=pad_sequences(X1,dtype=str,maxlen=150,padding="post",value=1)

for i in range(len(X1)):
	str1=" "
	for j in X1[i]:
		if j=="1.0":
			str1+=" NAW"
		else:
			str1+=" "+j
	X.append(str1.strip())
#print(X)


test,test1=[],[]
with open("test.txt") as f:
	for i in f:
		if i=='\n':
			continue
		test.append(i.strip())
		test1.append(i.strip().split())
#test1=np.array(test1)

with open("compressed.txt",'r',encoding='utf8') as f:
	for i in f:
		if i=='\n':
			continue
		Y.append(i.strip().split())
#print(X)
Y1=[]
for i in range(len(X)):
	words_bin=[]
	a=set(Y[i])
	words=X[i].split()
	for j in words:
		if j in a:
			words_bin.append(1)
		else:
			words_bin.append(0)
	Y1.append(words_bin)
Y1=pad_sequences(Y1,maxlen=150,padding="post",value=0)
#print(Y1)




tokenizer = Tokenizer(num_words=22600)
tokenizer.fit_on_texts(list(all_words))
X=tokenizer.texts_to_sequences(X)
#X=pad_sequences(X,maxlen=150,padding="post",value=)

X_train, X_test, y_train, y_test = train_test_split(X,Y1, test_size=0.3, shuffle=False)

embedding_matrix = np.zeros((len(all_words)+1, 300))
for word, i in tokenizer.word_index.items():
	embedding_vector = glove.get(word)
	if embedding_vector is not None:
		embedding_matrix[i,:] = list(embedding_vector)

model = Sequential()
model.add(Embedding(len(all_words)+1,300,weights=[embedding_matrix],input_length=150,trainable=False))
model.add(LSTM(150,dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(150))
model.add(Activation('sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, y_train, epochs=1, batch_size=10)


scores = model.evaluate(X_test, y_test, verbose=0)
preds=model.predict(test)
preds=np.array(preds,dtype=np.float32)
preds=preds>0.4
preds=preds*1
print(preds.shape)


for i in range(preds.shape[0]):
	for j in range(len(test1[i])):
		a=test1[i]
		if preds[i,j]==1:
			print(a[j],end=" ")
	print("\n")
