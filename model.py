import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow
from tensorflow.keras.layers import Dropout
from tensorflow.keras.models import load_model
import pickle as pkl

dataset = pd.read_csv('dataset/Heart-data.csv')
print(dataset.shape)
X = dataset.iloc[:, 1:14].values
y = dataset.iloc[:, 14].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

ann = tensorflow.keras.models.Sequential()
ann.add(tensorflow.keras.layers.Dense(units=13, activation='relu'))
ann.add(tensorflow.keras.layers.Dense(units=24, activation='relu'))
ann.add(Dropout(0.5))
ann.add(tensorflow.keras.layers.Dense(units=1, activation='sigmoid'))
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

history = ann.fit(X_train, y_train, batch_size = 32,verbose=1, epochs = 120, validation_data=(X_test,y_test))

pkl.dump(sc,open('scaler.pkl','wb'))
ann.save('Model.h5')


# print("TRAIN Accuracy is: {}".format(history.history.get('accuracy')[-1]*100))
# print("Accuracy is: {}".format(history.history.get('val_accuracy')[-1]*100))

