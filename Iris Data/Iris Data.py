# Iris Data

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
dir(iris)

# Checking feature and target names
iris.feature_names
iris.target_names

# Creating dataframe
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df1 = pd.DataFrame(iris.data)   # For numbers as columns

# Setting a target variable from Iris table
df['target'] = iris.target

# Splitting dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop(['target'],axis='columns'),
                                                    iris.target,test_size=0.2)

# ========================== or========================================================
# Independent and dependent variable
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y,test_size=0.2)

# Random Forest with default estimators
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train1, y_train1)
model.score(X_test1,y_test1)

# Random forest with 40 estimators
model = RandomForestClassifier(n_estimators=40)
model.fit(X_train1, y_train1)
model.score(X_test1,y_test1)

# With SVM
from sklearn.svm import SVC
model = SVC()
model.fit(X_train1, y_train1)
model.score(X_test1, y_test1)

# With Kernel SVM
from sklearn.svm import SVC
model = SVC(kernel='linear')
model.fit(X_train1, y_train1)
model.score(X_test1, y_test1)

# Training the Decision Tree Classification model on the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train1, y_train1)
classifier.score(X_test1, y_test1)














