# Credit Card Fraud Detection

# Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import tensorflow as tf

dataset = pd.read_csv('creditcard.csv')

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

X.isna().sum()
y.isna().sum()

X.drop('Time', axis = 1, inplace = True)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X['Amount'] = sc.fit_transform(X['Amount'].values.reshape(len(X['Amount']),1))
# data = data.drop(['Amount'],axis=1)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)


# Random Forest
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)
pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, pred)
print (cm)
accuracy_score(y_test, pred)
# 0.9995962220427653

######### Decision Tree
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, pred)
print (cm)
accuracy_score(y_test, pred)
# 0.9991397773954567

######### ANN
# creating Input
ann = tf.keras.models.Sequential()

# Creating first layer
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# Creating second layer
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# Creating output layer
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Compiling the ANN
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


# Training the ANN on the Training set
ann.fit(X_train, y_train, batch_size = 32, epochs = 100)

# # testing data on 1 member
# ann.predict(sc.transform([[1,0,0,600,1,40,3,60000,2,1,1,50000]]))
# print(ann.predict(sc.transform([[1,0,0,600,1,40,3,60000,2,1,1,50000]]))> 0.5)

# Part 4 - Making the predictions and evaluating the model==================
# Predicting the Test set results
y_pred = ann.predict(X_test)
y_pred1 = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred1)
print(cm)
accuracy_score(y_test, y_pred1)
# 0.9994733330992591