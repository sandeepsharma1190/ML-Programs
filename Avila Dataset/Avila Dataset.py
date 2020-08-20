# Avila Dataset
# UCI Rep - https://archive.ics.uci.edu/ml/datasets/Avila
# C:\Users\sshar127\Desktop\New folder\Healthy people\avila

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv('avila-training.txt', sep=',', header=None)
test_ds = pd.read_csv('avila-test.txt', sep=',', header=None)

dataset.columns[dataset.isna().any()]
test_ds.columns[test_ds.isna().any()]

dataset.describe()
### Correlation=======================================================
corrmat = dataset.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
g=sns.heatmap(dataset[top_corr_features].corr(),annot=True,cmap="RdYlGn")
#===============================================================
X_train = dataset.drop(10, axis='columns')
y_train = dataset[10]

# test
X_test = test_ds.drop(10, axis='columns')
y_test = test_ds[10]

# ======================== Random Forest========================
from sklearn.ensemble import RandomForestClassifier
obj = RandomForestClassifier()
obj.fit(X_train,y_train)

# Prediction
y_pred = obj.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print (accuracy_score(y_test,y_pred))
0.9839992334962154
ac = accuracy_score(y_test,y_pred)
print ("{0:.0%}".format(ac))    # 98%

# ======================== XG Boost========================
from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
ac = accuracy_score(y_test,y_pred)
print ("{0:.0%}".format(ac)) # 88%

# ======================== Decision Tree ========================
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
ac = accuracy_score(y_test,y_pred)
print ("{0:.0%}".format(ac)) # 97%

======================== Decision Tree =======================
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
ac = accuracy_score(y_test,y_pred)
print ("{0:.0%}".format(ac))    75%
