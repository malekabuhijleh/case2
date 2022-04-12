import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import tabulate

df = pd.read_csv('casestudy.csv')

df2015 = df.query("year == 2015")
df2016 = df.query("year == 2016")
df2017 = df.query("year == 2017")

data = {'year': [2015,2016,2017],
        'Total_revenue': [df2015['net_revenue'].sum(),df2016['net_revenue'].sum(),df2017['net_revenue'].sum()],
        'New_customers_Revenue': [0,df2016[~df2016['customer_email'].isin(df2015['customer_email'])]['net_revenue'].sum(),df2017[~df2017['customer_email'].isin(df2016['customer_email'])]['net_revenue'].sum()],
        'Existing_customer_revenue': [df2015['net_revenue'].sum(),df2016['net_revenue'].sum(),df2017['net_revenue'].sum()],
        'Existing_customer_revenue_Prior_year':[0,df2015['net_revenue'].sum(),df2016['net_revenue'].sum()],
        'Existing_customer_growth': [0,df2016['net_revenue'].sum()-df2015['net_revenue'].sum(),df2017['net_revenue'].sum()-df2016['net_revenue'].sum()],
        'Total_customers': [df2015['customer_email'].count(),df2016['customer_email'].count(),df2017['customer_email'].count()],
        'Total_customers_previous_year': [0,df2015['customer_email'].count(),df2016['customer_email'].count()],
        'New_customers': [0,df2016[~df2016['customer_email'].isin(df2015['customer_email'])]['customer_email'].count(),df2017[~df2017['customer_email'].isin(df2016['customer_email'])]['customer_email'].count()],
        'Lost_customers':[0, df2015[~df2015['customer_email'].isin(df2016['customer_email'])]['customer_email'].count(),df2016[~df2016['customer_email'].isin(df2017['customer_email'])]['customer_email'].count()]
        }
table = pd.DataFrame(data)
print(table[['year', 'Total_revenue']])
print(table[['year', 'New_customers_Revenue']])
print(table[['year', 'Existing_customer_growth']])
print(table[['year', 'Existing_customer_revenue']])
print(table[['year', 'Existing_customer_revenue_Prior_year']])
print(table[['year', 'Total_customers']])
print(table[['year', 'Total_customers_previous_year']])
print(table[['year', 'New_customers']])
print(table[['year', 'Lost_customers']])





#Data Visuslization
fig = pd.DataFrame({'New Customers': [table['New_customers'][0],table['New_customers'][1],table['New_customers'][2]],
                   'Lost Customers':[table['Lost_customers'][0],table['Lost_customers'][1],table['Lost_customers'][2]]})

sns.set(rc = {'figure.figsize':(10,6)})
g = sns.lineplot(data=fig)
g.set_xticks(range(3))
g.set_xticklabels(['2015', '2016', '2017'])
plt.show()
#Growth VS Year
fig1 = pd.DataFrame({'Existing_customer_growth': [table['Existing_customer_growth'][0],table['Existing_customer_growth'][1],table['Existing_customer_growth'][2]]})
sns.set(rc = {'figure.figsize':(10,6)})
g = sns.lineplot(data=fig1)
g.set_xticks(range(3))
g.set_xticklabels(['2015', '2016', '2017'])
g.set_xlabel("year")
g.set_ylabel("Growth")
plt.show()