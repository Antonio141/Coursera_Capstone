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

df = pd.read_csv('D:/personale/MACHINELEARNING/IBM/capstone/df_district_4.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Map
# choropleth.gen_choro(df,np,pd)

#Cleaningdata
# clean_data.drop_stuff(df,pd,np)
# clean_data.transform(df,pd,np)
# clean_data.dummies(df,pd)

# col = 'DISTRICT'
# clean_data.fill_na_by_percentage(df,np, col)

# df.drop(['JUNCTIONTYPE', 'SDOT_COLDESC', 'UNDERINFL', 'ST_COLDESC','HITPARKEDCAR', 'geometry','Unnamed: 0','Unnamed: 0.1'], axis = 1, inplace = True)
df.drop('Unnamed: 0', axis = 1, inplace = True)


# df.to_csv('D:/personale/MACHINELEARNING/IBM/capstone/df_district_4.csv')

# print(df.info())
model.predict(df,np)

# df['SEVERITYCODE'].replace(to_replace=(1,2), value=(0,1))

# y = df['SEVERITYCODE']

# df.drop('SEVERITYCODE', axis= 1, inplace= True)

# X_train, X_test, y_train, y_test = train_test_split( df, y, test_size=0.2, random_state=4)



# # C = 1/lambda (Regularization Parameter) solver: Method of resolution of the algorithm
# LR = LogisticRegression(C=0.01, solver='liblinear').fit(X_train,y_train)
# yhat = LR.predict(X_test)
# yhat_prob = LR.predict_proba(X_test)

# lr_a = metrics.accuracy_score(y_test, yhat)
# print('Logistic Regression accuracy: ', lr_a)
