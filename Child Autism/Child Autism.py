# Child Autism

# https://archive.ics.uci.edu/ml/datasets/Autism+Screening+Adult

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats



dataset = pd.read_csv('Autism-Child-Data.txt')

cleanup_nums = {'gender': {'m':1, 'f':0},
                'jundice': {'yes': 1, 'no': 0},
                'austim': {'yes': 1, 'no': 0},
                'used_app_before': {'yes': 1, 'no': 0},
                'Class/ASD': {'YES': 1, 'NO': 0}}

dataset.replace(cleanup_nums, inplace=True)

dataset = dataset.rename(columns = {'gender': 'Male'})

dataset = dataset.replace('?', np.nan)

# Checking NaN Values
dataset.isna().sum()

dataset.age = dataset.age.fillna(dataset.age.median())
dataset.age = dataset.age.astype(int)

dataset1 = dataset.drop(['age_desc', 'ethnicity', 'relation', 'country'], axis = 1)
# dataset_new = dataset.select_dtypes(exclude=[object])

(mu, sigma) = stats.norm.fit(dataset1['age'])
print( '\n mu = {:.2f} and sigma = {:.2f}\n'.format(mu, sigma))

### Correlation=======================================================
corrmat = dataset_new.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
g=sns.heatmap(dataset_new[top_corr_features].corr(),annot=True,cmap="RdYlGn")

#skewness and kurtosis age
print("Skewness: %f" % dataset1['age'].skew())
print("Kurtosis: %f" % dataset1['age'].kurt())

#skewness and kurtosis result
print("Skewness: %f" % dataset1['result'].skew())
print("Kurtosis: %f" % dataset1['result'].kurt())

#skewness and kurtosis result
print("Skewness: %f" % dataset1['Class/ASD'].skew())
print("Kurtosis: %f" % dataset1['Class/ASD'].kurt())

# Dependent and Independent variable
X = dataset_new.drop('Class/ASD', axis = 1)
y = dataset_new.loc[:,'Class/ASD']

# Data Splitting
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)


from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)


from sklearn.metrics import accuracy_score, confusion_matrix
cm = confusion_matrix (y_test, y_pred)
print (cm)
print (accuracy_score(y_test, y_pred))

# 100%
#===========================