import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def fill_na_by_percentage(df, col):
    r, _ = np.where(df[[col]].isna())
    
    r = np.unique(r)
    r= r.tolist()
    l = len(r)
    if l != 0:
        ad = df[col].value_counts(normalize = True)
        # print(ad)
        for i in range(len(ad)):
            L = int(np.floor(l * ad[i]))
            try:
                df[col].fillna(ad.keys()[i], limit = L, inplace = True )
            except:
                r, _ = np.where(df[[col]].isna())
                r = np.unique(r).tolist()
                l = len(r)
                if l > 0:
                    df[col].fillna(ad.keys()[i], limit = l, inplace = True )
                print('Function terminated')
                return
    else:
        print('No nan values in column')
        return

df = pd.read_csv('D:/personale/MACHINELEARNING/IBM/capstone/Data-Collisions.csv', low_memory = False)
print(df.info())
df['WEEKDAY'] = pd.to_datetime(df['INCDATE']).dt.weekday
df.groupby('WEEKDAY')['SEVERITYCODE'].value_counts(normalize= True)

df.drop(['X', 'Y', 'OBJECTID', 'INCKEY', 'COLDETKEY', 'REPORTNO', 
'STATUS', 'INCDATE', 'INCDTTM', 'SDOTCOLNUM','SEGLANEKEY', 'CROSSWALKKEY', 'SEVERITYCODE.1', 'SEVERITYDESC', 'LOCATION','INTKEY', 'ST_COLCODE', 'SDOT_COLCODE',
'EXCEPTRSNCODE', 'EXCEPTRSNDESC', 'PEDROWNOTGRNT', 'SPEEDING', 'INATTENTIONIND'], axis = 1, inplace = True)

r, _ = np.where(df[['SDOT_COLDESC', 'ST_COLDESC', 'COLLISIONTYPE', 'HITPARKEDCAR']].isna())
r = np.unique(r).tolist()


mask_other = (df['COLLISIONTYPE'].isnull()) & (df['SDOT_COLDESC'] == 'MOTOR VEHICLE STRUCK OBJECT IN ROAD')

mask_angles = (df['COLLISIONTYPE'].isnull()) & (df['SDOT_COLDESC'] == 'MOTOR VEHICLE STRUCK MOTOR VEHICLE, FRONT END AT ANGLE')

mask_parked = (df['COLLISIONTYPE'].isnull()) & (df['SDOT_COLDESC'] == 'DRIVERLESS VEHICLE STRUCK MOTOR VEHICLE REAR END') & (df['ST_COLDESC'] == 'One parked--one moving')

mask_rear = (df['COLLISIONTYPE'].isnull()) & (df['SDOT_COLDESC'] == 'MOTOR VEHICLE STRUCK MOTOR VEHICLE, REAR END')

mask_pedestrian = (df['SDOT_COLDESC']=='MOTOR VEHCILE STRUCK PEDESTRIAN') & \
    (df['COLLISIONTYPE'].isnull())

mask_cycles = (df['SDOT_COLDESC']=='MOTOR VEHICLE STRUCK PEDALCYCLIST, FRONT END AT ANGLE') & (df['COLLISIONTYPE'].isnull())

mask_parked1 = (df['SDOT_COLDESC']=='MOTOR VEHICLE STRUCK MOTOR VEHICLE, LEFT      SIDE SIDESWIPE') & (df['COLLISIONTYPE'].isnull()) & (df['HITPARKEDCAR'] == 'Y') 

mask_sideswipe = (df['SDOT_COLDESC']=='MOTOR VEHICLE STRUCK MOTOR VEHICLE, LEFT SIDE SIDESWIPE') & (df['COLLISIONTYPE'].isnull()) & (df['HITPARKEDCAR'] == 'N')

mask_other1 = (df['SDOT_COLDESC']=='MOTOR VEHICLE RAN OFF ROAD - NO COLLISION') &  (df['COLLISIONTYPE'].isnull())

mask_other2 = (df['SDOT_COLDESC'] == 'NOT ENOUGH INFORMATION / NOT APPLICABLE') & \
(df['COLLISIONTYPE'].isnull())

mask_other3 = (df['SDOT_COLDESC'] == 'MOTOR VEHICLE RAN OFF ROAD - HIT FIXED OBJECT') & (df['COLLISIONTYPE'].isnull())

mask_parked2 = (df['SDOT_COLDESC'] == 'MOTOR VEHICLE STRUCK MOTOR VEHICLE, LEFT SIDE AT ANGLE') & (df['COLLISIONTYPE'].isnull()) & (df['HITPARKEDCAR'] == 'Y')

mask_other4 = (df['SDOT_COLDESC'] == 'MOTOR VEHICLE STRUCK MOTOR VEHICLE, LEFT SIDE AT ANGLE') & (df['COLLISIONTYPE'].isnull()) & (df['HITPARKEDCAR'] == 'N')

mask_other5 = (df['SDOT_COLDESC'] == 'MOTOR VEHICLE OVERTURNED IN ROAD') & \
     (df['COLLISIONTYPE'].isnull())

mask_sideswipe1 = (df['SDOT_COLDESC']=='MOTOR VEHICLE STRUCK MOTOR VEHICLE, RIGHT SIDE \
# SIDESWIPE') & (df['COLLISIONTYPE'].isnull()) 

mask_cycles1 = \
(df['SDOT_COLDESC']=='PEDALCYCLIST STRUCK MOTOR VEHICLE FRONT END AT ANGLE')  | \
(df['SDOT_COLDESC']=='PEDALCYCLIST STRUCK MOTOR VEHICLE REAR END')            | \
(df['SDOT_COLDESC']=='PEDALCYCLIST STRUCK MOTOR VEHICLE LEFT SIDE SIDESWIPE') | \
(df['SDOT_COLDESC']=='MOTOR VEHICLE STRUCK PEDALCYCLIST, LEFT SIDE SIDESWIPE')| \
(df['SDOT_COLDESC']=='PEDALCYCLIST OVERTURNED IN ROAD')                       & \
(df['COLLISIONTYPE'].isnull()) 

mask_parked3 = \
(df['SDOT_COLDESC'] == 'MOTOR VEHICLE STRUCK MOTOR VEHICLE, RIGHT SIDE AT ANGLE')   | \
(df['SDOT_COLDESC']=='DRIVERLESS VEHICLE STRUCK MOTOR VEHICLE FRONT END AT ANGLE') | \
(df['SDOT_COLDESC']=='DRIVERLESS VEHICLE STRUCK MOTOR VEHICLE REAR END')           | \
(df['SDOT_COLDESC'] == 'MOTOR VEHICLE STRUCK MOTOR VEHICLE, LEFT SIDE SIDESWIPE')   & \
(df['COLLISIONTYPE'].isnull()) 

mask_other6 =\
(df['SDOT_COLDESC']=='DRIVERLESS VEHICLE RAN OFF ROAD - HIT FIXED OBJECT') | \
(df['SDOT_COLDESC']=='MOTOR VEHICLE STRUCK TRAIN') & \
(df['COLLISIONTYPE'].isnull())

mask_parked4 = \
(df['SDOT_COLDESC'] == 'MOTOR VEHICLE STRUCK MOTOR VEHICLE, RIGHT SIDE SIDESWIPE') & \
(df['HITPARKEDCAR'] == 'Y')  & \
(df['COLLISIONTYPE'].isnull()) 

mask_sideswipe2 = \
(df['SDOT_COLDESC'] == 'MOTOR VEHICLE STRUCK MOTOR VEHICLE, RIGHT SIDE SIDESWIPE') & \
(df['HITPARKEDCAR'] == 'N')  & \
(df['COLLISIONTYPE'].isnull()) 

df['COLLISIONTYPE'][mask_other] = 'Other'
df['COLLISIONTYPE'][mask_angles] = 'Angles'
df['COLLISIONTYPE'][mask_parked] = 'Parked Car'
df['COLLISIONTYPE'][mask_rear] = 'Rear Ended'
df['COLLISIONTYPE'][mask_pedestrian] = 'Pedestrian'
df['COLLISIONTYPE'][mask_cycles] = 'Cycles'
df['COLLISIONTYPE'][mask_parked1] = 'Parked'
df['COLLISIONTYPE'][mask_sideswipe] = 'Sideswipe'
df['COLLISIONTYPE'][mask_other1] = 'Other'
df['COLLISIONTYPE'][mask_other2] = 'Other'
df['COLLISIONTYPE'][mask_other3] = 'Other'
df['COLLISIONTYPE'][mask_parked2] = 'Parked Car'
df['COLLISIONTYPE'][mask_other4] = 'Other'
df['COLLISIONTYPE'][mask_other5] = 'Other'
df['COLLISIONTYPE'][mask_sideswipe1] = 'Sideswipe'
df['COLLISIONTYPE'][mask_cycles1] = 'Cycles'
df['COLLISIONTYPE'][mask_parked3] = 'Parked Car'
df['COLLISIONTYPE'][mask_other6] = 'Other'
df['COLLISIONTYPE'][mask_parked4] = 'Parked Car'
df['COLLISIONTYPE'][mask_sideswipe2] = 'Sideswipe'

r= np.where(df['COLLISIONTYPE'].isna())[0]
r = np.unique(r).tolist()
len(r)

mask_block= (df['JUNCTIONTYPE'] == 'Mid-Block (not related to intersection)') | \
    (df['JUNCTIONTYPE'] == 'Mid-Block (but intersection related)') | \
    (df['JUNCTIONTYPE'] == 'Ramp Junction') | \
    (df['JUNCTIONTYPE'] == 'Driveway Junction') | \
    (df['JUNCTIONTYPE'] == 'Unknown') & \
    (df['ADDRTYPE'].isnull())

mask_intersection= (df['JUNCTIONTYPE'] == 'At Intersection (intersection related)') | \
       (df['JUNCTIONTYPE'] == 'At Intersection (but not related to intersection)') \
        & (df['ADDRTYPE'].isnull())


df['ADDRTYPE'][mask_block] = 'Block'
df['ADDRTYPE'][mask_intersection] = 'Intersection'


lista = ['LIGHTCOND', 'ROADCOND', 'UNDERINFL', 'WEATHER', 'ADDRTYPE']

for i in lista:
    fill_na_by_percentage(df,i)

print(df.info())
pd.get_dummies(data = df, columns='WEATHER')
