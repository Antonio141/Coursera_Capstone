import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import folium
# from sklearn.model_selection import train_test_split
# import scipy.optimize as opt
# from sklearn.linear_model import LogisticRegression

import geopandas
import choropleth
import clean_data
import model

# Call the dataframe
# df.to_csv('D:/personale/MACHINELEARNING/IBM/capstone/df_district_2.csv')

df = pd.read_csv('D:/personale/MACHINELEARNING/IBM/capstone/file_for_graphs.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Map
# choropleth.gen_choro(df,np,pd)

#Cleaningdata
# clean_data.drop_stuff(df,pd,np)
# clean_data.transform(df,pd,np)
# clean_data.dummies(df,pd)


# df.drop(['JUNCTIONTYPE', 'SDOT_COLDESC', 'UNDERINFL', 'ST_COLDESC','HITPARKEDCAR', 'geometry','Unnamed: 0','Unnamed: 0.1'], axis = 1, inplace = True)
# df.drop('Unnamed: 0', axis = 1, inplace = True)
# df['PERSONCOUNT'][df['PERSONCOUNT']>= 6] = 'Six or more'

# df['PERSONCOUNT'].replace( \
# to_replace=(0,1,2,3,4,5), \
# value=('Zero','One','Two','Three','Four','Five'), \
# inplace=True)

temp= df.groupby(['ROADCOND'])['SEVERITYCODE'].value_counts(normalize=True).mul(100).rename('percentage').reset_index().sort_index()

plt.figure(figsize=(7,7))
chart = sns.barplot(data = temp, x = 'percentage', y= 'ROADCOND', hue= 'SEVERITYCODE', linewidth=2,
palette='PuOr')
# , order=('Zero','One','Two','Three','Four','Five','Six or more')
chart.set_title('SEVERITY BY ROAD CONDITIONS', weight='bold')
chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right')
chart.set_yticklabels(chart.get_yticklabels(), rotation=0, horizontalalignment='right', style='italic')
chart.set_xlabel('Percentage')
chart.set_ylabel('Road Conditions')
chart.set_xbound(upper=115)
# chart.set_ybound(lower=-1,upper=10)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

total=100
new_value=0.5
for p in chart.patches:
        percent = '{:.1f}%'.format(100 * p.get_width()/total)
        x =  p.get_width() + .5
        y = p.get_y() + p.get_height() - .15 
        chart.annotate(percent, (x, y), fontsize=10, color='k', weight='bold', style='italic')

# df['PERSONCOUNT'].replace( \
# value=(0,1,2,3,4,5,'6 or more'), \
# to_replace=('Zero','One','Two','Three','Four','Five','Six or more'), \
# inplace=True)

plt.show()