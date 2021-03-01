# Test

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

gdp_ds = pd.read_csv('C:\\Users\\sshar127\\Desktop\\New folder\\Test\\GDP\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv', skiprows = 4)
# gdp.head()
gdp_ds1 = gdp_ds.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
# country_index = gdp_ds1.set_index('Country Name')


popluation_ds = pd.read_csv('C:\\Users\\sshar127\\Desktop\\New folder\\Test\\Population\\API_SP.POP.TOTL_DS2_en_csv_v2_1345178.csv', skiprows = 4)
# popluation_ds.head()
popluation_ds = popluation_ds.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)

income_info_ds = pd.read_csv('C:\\Users\\sshar127\\Desktop\\New folder\\Test\\GDP\\Metadata_Country_API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv', 
                             usecols=('Country Code', 'IncomeGroup'))

#1.	What was the GDP per capita of Bangladesh in 1975?=============================
gdp = gdp_ds.at[18, '1975']
population = popluation_ds.at[18, '1975']
gdp_per_capita = gdp/population
print (gdp_per_capita)
print ("{:.2f}".format(gdp_per_capita))

# ====================================================================================

# 2. What is the average GDP of all countries that start with the letter B in 1999?
b_countries = gdp_ds[gdp_ds['Country Name'].str.startswith('B')]
mean_gdp = b_countries['1999'].mean()
b_population = popluation_ds[popluation_ds['Country Name'].str.startswith('B')]
mean_population = b_population['1999'].mean()
b_countries_gdp_per_capita = mean_gdp/mean_population
print ("{:.2f}".format(b_countries_gdp_per_capita))
# ====================================================================================

# 3. What years do we have complete data (GDP and Population) for Iran?
iran_gdp = gdp_ds1.loc[110,:]
iran_pop = popluation_ds.loc[110,:]
iran_data = pd.concat([iran_gdp, iran_pop], axis = 1)
iran_data1 = iran_data.dropna()

# ====================================================================================

# 4. Which country had the highest YoY population growth in 1985?
country = popluation_ds.loc[:, 'Country Name']
pop_1985_percentage = popluation_ds.loc[:, ['1985']].pct_change()
concate1 = pd.concat([country, pop_1985_percentage], axis = 1)
YoY_pop_growth = concate1.max()
print (YoY_pop_growth)
# ====================================================================================
# 5. Which county had the 3rd highest 5 year population growth in 2012?
country = popluation_ds.loc[:, 'Country Name']
pop_2012_5yr_percentage = popluation_ds.loc[:, ['2008', '2009', '2010', '2011', '2012']].pct_change()
pop_2012_5yr_percentage['mean'] = pop_2012_5yr_percentage.mean(axis = 1)
concate2 = pd.concat([country, pop_2012_5yr_percentage], axis = 1)
pop5yr_2012 = concate2.nlargest(3, ['mean']) 
third_highest = pop5yr_2012.iloc[2,:]
print (third_highest)
# ====================================================================================

# 6. What was the average GDP per capita of each region (for reference, the regions are below) in 2000? 
gdp_dst = gdp_ds.transpose()
gdp_dst = gdp_dst.rename(columns=gdp_dst.iloc[0])
gdp_dst.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], inplace = True)
gdp_dst = gdp_dst.loc['2000', ['Latin America & Caribbean', 'South Asia', 'Sub-Saharan Africa', 'Europe & Central Asia', 'Middle East & North Africa', 'East Asia & Pacific', 'North America']]

gdp_popt = popluation_ds.transpose()
gdp_popt = gdp_popt.rename(columns=gdp_popt.iloc[0])
gdp_popt.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], inplace = True)
gdp_popt = gdp_popt.loc['2000', ['Latin America & Caribbean', 'South Asia', 'Sub-Saharan Africa', 'Europe & Central Asia', 'Middle East & North Africa', 'East Asia & Pacific', 'North America']]

gdp_per_capita_2 = gdp_dst/gdp_popt
print (gdp_per_capita_2)

# =====================================================================================================
# 8. What is the minimum, maximum and 60th percentile GDP of each of the income groups (for reference, the income groups are below) in 2016: 
# a. High Income
# b. Low Income
# c. Lower Middle Income
# d. Upper Middle Income 
merge_data = pd.merge(gdp_ds, income_info_ds, on = 'Country Code', how= 'inner')
merge_data.drop(['Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 64'], axis = 1, inplace = True)
merge_data = merge_data[pd.notnull(merge_data['IncomeGroup'])]
mean_group1 = merge_data.groupby('IncomeGroup').mean()
mean_group1['perc 60'] = np.percentile(mean_group1, 60, axis=1)
mean_group1['perc Min'] = np.percentile(mean_group1, 1, axis=1)
mean_group1['perc Max'] = np.percentile(mean_group1, 100, axis=1)
percentile_grp = mean_group1.loc[:,['perc 60', 'perc Min', 'perc Max']]
# =====================================================================================================
# 9. What is the average GDP of each of the following income groups in each decade from 1960 – 2010.
# Groups was not mentioned in test
# High Income
# Low Income
# Lower Middle Income
# Upper Middle Income 

merge_data = pd.merge(gdp_ds, income_info_ds, on = 'Country Code', how= 'inner')
merge_data.drop(['Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 64'], axis = 1, inplace = True)
merge_data = merge_data[pd.notnull(merge_data['IncomeGroup'])]
mean_group = merge_data.groupby('IncomeGroup').mean()
mean_group['Mean'] = mean_grp2.mean(axis = 1)
# =====================================================================================================

# 10. Plot the share of GDP by region by year in a stacked bar chart
income_info_ds2 = pd.read_csv('C:\\Users\\sshar127\\Desktop\\New folder\\Test\\GDP\\Metadata_Country_API_NY.GDP.MKTP.CD_DS2_en_csv_v2_1345540.csv', 
                             usecols=('Country Code', 'Region'))
merge_data2 = pd.merge(gdp_ds, income_info_ds2, on = 'Country Code', how= 'inner')
merge_data2.drop(['Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 64'], axis = 1, inplace = True)
merge_data2 = merge_data2[pd.notnull(merge_data2['Region'])]

mean_group2 = merge_data2.groupby('Region').mean()
mean_group2.plot.bar(stacked=True)
# =====================================================================================================



















