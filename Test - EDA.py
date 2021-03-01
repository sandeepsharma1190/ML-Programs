# Test - EDA

import pandas as pd
df = pd.read_csv('Medical_No_Shows.csv', encoding='latin-1')

# Obtain a description of the dataset. What observations can you make about the data? 

df.describe()

# Get the basic information from the data. What issues/ errors do you notice with regard to the columns and data types?
df.info()

# 5. Convert datatype for 'ScheduledDay' and 'AppointmentDay' to datetime
df = pd.read_csv('Medical_No_Shows.csv', encoding='latin-1', 
                 parse_dates = ['ScheduledDay', 'AppointmentDay'])



df2.info()

df1 = pd.read_csv('Medical_No_Shows.csv', encoding='latin-1', 
                 parse_dates = [3,4], dayfirst=True)
df1.info()

df.ScheduledDay = pd.to_datetime(df.ScheduledDay)
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'], format="%Y-%d-%m %H:%M:%S")

# df[['ScheduledDay','AppointmentDay']].apply(pd.to_datetime, format='%Y-%m-%d %H:%M:%S.%f')

df.iloc[:, 3:5] = df.iloc[:, 3:5].apply(pd.to_datetime, errors='coerce')


# Rename misspelled columns and rename 'No-show' values to ('Show','No show').
## Hint 2: Yes = No show, No = Show
df.rename(columns=lambda x: x.replace('Hipertension', 'Hypertension'), inplace=True)

df.rename(columns = {'Hipertension': 'Hypertension',
                     'Handcap': 'Handicap'}, inplace = True)


change_code = {'Yes': 'No show', 'No':'Show'}
df['No-show'] = [change_code[item] for item in df['No-show']] 

df['No-show'] = df['No-show'].replace(['Yes','No'],['No show','Show'])


# . Obtain the number of unique entries in each column; what observation can be made
df.nunique()


# Drop records where Age < 0
df.drop(df[df.Age < 0].index, inplace=True)


# Convert data types for all categorical variables
''' Hint : Convert to type ('category') for Gender, SMS_received, 
Hypertension and No-show '''
df['Gender'] = df['Gender'].astype('category')
df.info()


df = df.astype({'Gender': 'category', 'SMS_received': 'category',
                'Hypertension':'category', 'No-show':'category'})
df.info()
df2 = pd.read_csv('Medical_No_Shows.csv', encoding='latin-1',
                  parse_dates = ['ScheduledDay', 'AppointmentDay'],
                  dtype={'Gender': 'category', 'SMS_received': 'category',
                  'Hypertension':'category', 'No-show':'category'})

df[['Gender', 'SMS_received', 'Hypertension', 'No-show']] = df[['Gender', 'SMS_received', 'Hypertension', 'No-show']].astype('category')


'''Create two new variables: (1)'WaitingDays' = number of days 
between scheduled and appointment dates and (2) 'WeekDay' = 
week day of appointment. Do these new variables present 
inconsistencies? If so, what inconsistencies are present 
and how are they resolved?'''

# 'WaitingDays' = number of days between scheduled and appointment dates
df['WaitingDays'] = df['AppointmentDay'] - df['ScheduledDay']

# 'WeekDay' = week day of appointment
## Hint 2: WeekDays = apply(lambda x: x.weekday()), then replace_map to assign text description (0:Monday, 1:Tuesday...)

df['WeekDay'] = df['WaitingDays'].dt.dayofweek
df['weekday'] = pd.Series(df.WaitingDays).dt.dayofweek

df['WeekDay'] = df[['AppointmentDay']].apply(lambda x: pd.datetime.strftime(x['AppointmentDay'], '%A'), axis=1)
df.head()

# Create a pie chart to illustrate the number of patients who were present or "no-shows" for their appointment. What percentage of patients were "no-shows"?
import matplotlib.pyplot as plt
df.groupby('No-show').size().plot(kind='pie', autopct='%.2f%%')
plt.show()


import plotly.express as px
df['No-show'] = px.data.tips()
fig = px.pie(df['No-show'], values='No-show', names='No-show')
fig.show()

''' Create a bar chart to illustrate the number of "shows" vs. 
"no shows" by gender. Does this variable have an impact on the 
outcome?'''
    
## Hint 1 : Use the go.bar and py.iplot or sns.countplot
## Hint 2 : You can create two separate bar graphs for Show/No 
show or M/F, then combine (if needed)


import seaborn as sns
sns.set_theme(style="darkgrid")
titanic = sns.load_dataset("titanic")
ax = sns.countplot(x='No-show', data=df)

ax = sns.barplot(x='No-show', y='Gender', data=df)

import plotly.express as px
fig = px.bar(df, x='No-show', y='Gender')
fig.show()
# fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
# fig.show()

import plotly.graph_objects as go
fig = go.Figure([go.Bar(x='No-show', y='Gender', data=df)])
fig.show()






# Checking outliers
sns.stripplot(data = df, y = 'AwaitingTime', jitter = True)
sns.plt.ylim(0, 500)
sns.plt.show()



# Print Unique Values
print("Unique Values in `Gender` => {}".format(df.Gender.unique()))
print("Unique Values in `Scholarship` => {}".format(df.Scholarship.unique()))
print("Unique Values in `Hypertension` => {}".format(df.Hypertension.unique()))
print("Unique Values in `Diabetes` => {}".format(df.Diabetes.unique()))
print("Unique Values in `Alcoholism` => {}".format(df.Alcoholism.unique()))
print("Unique Values in `Handicap` => {}".format(df.Handicap.unique()))
print("Unique Values in `SMSReceived` => {}".format(df.SMSReceived.unique()))



Exploratory_Analysis = ['Gender','Hipertension','Alcoholism','Diabetes']
for r in Exploratory_Analysis :
    print(df.groupby(r)['No-show'].mean())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





