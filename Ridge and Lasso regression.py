# Ridge and Lasso regression (Regularization Hypertuning techniques)

# We use Ridge and Lasso regression method to convert high variance to low variance

'''y^ means best fit line (y = mx+c)
y is salary on experience (y value on x),

Lets say sum of residual is 0, means, y and y^ both are equal and creating 
a best fit line, This is for training dataset, lets say we have some other 
points in Test set, but now values are different than training sets and 
y-y^ != 0, this is called overfitting.'''


from sklearn.datasets import load_boston

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=load_boston()
print (df)

dataset = pd.DataFrame(df.data)
print(dataset.head())

dataset.columns=df.feature_names
dataset.head()

# Dependent feature
df.target.shape

# creating a new column as price and putting the target values there
dataset["Price"]=df.target
dataset.head()

X=dataset.iloc[:,:-1] ## independent features
y=dataset.iloc[:,-1] ## dependent features

#### Linear Regression and Model training
# "neg_mean_squared_error" more nearer to 0, model performs well
# cv=5 means 5 cross velidations
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
lin_regressor=LinearRegression()
mse=cross_val_score(lin_regressor,X,y,scoring='neg_mean_squared_error',cv=5)
print (mse)
mean_mse=np.mean(mse)
print(mean_mse)

#=======================Ridge Regression================================
# we can use lambda values from GridSearchCV
# y = (mx + c) + lambda X (slope)**2
# for multiple slops, we can use [lambda X [(slope)**2]+ [(slope2)**2]...n]
'''m is slop and is very steep (high value), we are penalizing slop using 
ridge regression. Penalizing means, we are decreasing steepness of the 
slop. with [lambda * (slope)**2].'''


from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
ridge=Ridge()
parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}
ridge_regressor=GridSearchCV(ridge,parameters,scoring='neg_mean_squared_error',cv=5)
ridge_regressor.fit(X,y)

print(ridge_regressor.best_params_)
print(ridge_regressor.best_score_)


#=======================Lasso Regression================================
# # y = (mx + c) + lambda X |slope|
# |slope| = doesn't mean, values will be +ve always #magnitude slope
# for multiple slops, we can use [lambda X [|slope|+ |slope2|...|n|]
'''Meagnitude means, Low values will automatically be removed. Best fit 
live will keep moving towards 0. After sometime, all values will become 
0 for Lasso.'''
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
lasso=Lasso()
parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}
lasso_regressor=GridSearchCV(lasso,parameters,scoring='neg_mean_squared_error',cv=5)

lasso_regressor.fit(X,y)
print(lasso_regressor.best_params_)
print(lasso_regressor.best_score_)

# ======== Splitting the datasets=============================================
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# ==========Prediction for both Lasso and Ridge regression==============================
prediction_lasso=lasso_regressor.predict(X_test)
prediction_ridge=ridge_regressor.predict(X_test)

# ==========Distplot for both Lasso and Ridge regression==============================
import seaborn as sns
sns.distplot(y_test-prediction_lasso)
sns.distplot(y_test-prediction_ridge)

















