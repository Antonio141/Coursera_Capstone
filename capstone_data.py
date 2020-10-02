import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import folium
import geopandas
import choropleth
import clean_data

# Call the dataframe
df = pd.read_csv('D:/personale/MACHINELEARNING/IBM/capstone/Data-Collisions.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Map
# choropleth.gen_choro(df,np,pd)

#Cleaningdata
clean_data.drop_stuff(df,pd)
print(df.info())

