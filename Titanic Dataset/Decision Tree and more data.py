# Decision Tree and more data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Regression - Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split (X,y, test_size = 0.2,
                                                     random_state = 0)

# Data Standardization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

######### Decision tree
from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor(random_state = 0)
reg.fit(X_train,y_train)
pred = reg.predict (X_test)
# Model Score
from sklearn.metrics import r2_score
r2_score(y_test, pred)
# 0.8972339515645668


######### Random Forest
from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor(random_state = 0)
reg.fit(X_train,y_train)
pred = reg.predict (X_test)
# Model Score
from sklearn.metrics import r2_score
r2_score(y_test, pred)
# 0.9504552436821897

######### Polynomial
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures()
X_poly = poly_reg.fit_transform(X_train)

lin_reg = LinearRegression()
lin_reg.fit(X_poly, y_train)

# poly_reg.predict(poly_reg.fit_transform(X_test))
pred = lin_reg.predict (poly_reg.fit_transform(X_test))
from sklearn.metrics import r2_score
r2_score(y_test, pred)
# 0.9417367873260147













