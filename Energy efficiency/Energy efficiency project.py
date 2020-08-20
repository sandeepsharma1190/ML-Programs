# Energy efficiency project
# https://archive.ics.uci.edu/ml/datasets/Energy+efficiency

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_excel('ENB2012_data.xlsx')
x = dataset.iloc[:,:-2].values
y = dataset.iloc[:,-2].values
# y = y.reshape(len(y),1)
# z = dataset.iloc[:,-1].values

# to check null counts
dataset.info(null_counts = True)

# Splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 0)

# Standardization
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler ()
# sc_y = StandardScaler ()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)
# y_train = sc_y.fit_transform(y_train)
# y_test = sc_y.transform(y_test)

# SVR================================
from sklearn.svm import SVR
reg_SVR = SVR(kernel = 'rbf')
reg_SVR.fit(X_train, y_train)
pred_SVR = reg_SVR.predict(X_test)
# Score
from sklearn.metrics import r2_score
r2_score(y_test, pred_SVR)
# Score: - 0.9173454554833214

# Decision Tree=======================
from sklearn.tree import DecisionTreeRegressor
reg_DT = DecisionTreeRegressor()
reg_DT.fit(X_train, y_train)
pred_DT = reg_DT.predict(X_test)
# Score
from sklearn.metrics import r2_score
r2_score(y_test, pred_DT)
# 0.9963805458046613

# Random Forest=======================
from sklearn.ensemble import RandomForestRegressor
reg_rf = RandomForestRegressor()
reg_rf.fit(X_train, y_train)
pred_rf = reg_rf.predict(X_test)
# Score
from sklearn.metrics import r2_score
r2_score(y_test, pred_rf)
# 0.99681072145248

#============ Linear Regression=======================
# Splitting the dataset
from sklearn.model_selection import train_test_split
X_train1, X_test1, y_train1, y_test1 = train_test_split(x,y,test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
reg_Lr = LinearRegression()
reg_Lr.fit(X_train1, y_train1)
pred_LR = regressor.predict(X_test1)
# Score
from sklearn.metrics import r2_score
r2_score(y_test1, pred_LR)
# -4.494131624391723 (With Data Standardization)
# -4.825728515204113 (Without Data Standardization)
# ================================================================================

#============ Polynomial feature ======================
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures()
X_poly = poly_reg.fit_transform(X_train)
reg_Lr1 = LinearRegression()
reg_Lr1.fit(X_poly, y_train)
pred_poly = reg_Lr1.predict(poly_reg.transform(X_test))
# Score
from sklearn.metrics import r2_score
r2_score(y_test, pred_poly)
# 0.9938601822693144