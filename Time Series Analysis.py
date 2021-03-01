# Time Series Analysis

import pandas as pd
import numpy as np

dataframe = pd.read_csv('daily-total-female-births-CA.csv', parse_dates=['date'])
dataframe['date'].dtype

# To pull info for a particualr month (Applicable on Data Frames only)
dataframe[(dataframe['date'] > '1959-01-01') & (dataframe['date'] <= '1959-01-21')]

dataframe.describe()

# Loading Data as a series
series = pd.read_csv('daily-total-female-births-CA.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)

# To pull info for a particualr month (Applicable on Data series only)
print(series['1959-01'])
series.describe()


# Feature Engineering
features = dataframe.copy()

features['year'] = dataframe['date'].dt.year
features['month'] = dataframe['date'].dt.month
features['day'] = dataframe['date'].dt.day

# Lagfeature can shift values ahead
# Default value is 1
features['lag2'] =  dataframe['births'].shift(2)
features['lag3'] =  dataframe['births'].shift(365)
features['lag4'] =  dataframe['births'].shift(0)
features['lag5'] =  dataframe['births'].shift()

features.drop(['lag4', 'lag5'], axis = 1, inplace = True)

# Window features - To get mean, max from 2 values
# window = 2 = number of periods we want to consider
features['Roll_mean'] = dataframe['births'].rolling(window = 2).mean()
features['Roll_max'] = dataframe['births'].rolling(window = 3).max()
features['Roll_median'] = dataframe['births'].rolling(window = 3).median()
features['Roll_std'] = dataframe['births'].rolling(window = 3).std()

# Expanding features
features['Expand_max'] = dataframe['births'].expanding().max()

# Downsampling and Upsampling
# Downsampling is to convert high frequency data to low frequency data
# Upsampling is to convert low frequency data to high frequency data

























