def drop_stuff(df,pd):
    df.drop(['X', 'Y', 'OBJECTID', 'INCKEY', 'COLDETKEY', 'REPORTNO','STATUS', 'INCDATE', 'INCDTTM','SDOTCOLNUM',
    'SEGLANEKEY', 'CROSSWALKKEY', 'SEVERITYCODE.1', 'SEVERITYDESC', 'LOCATION','INTKEY', 'ST_COLCODE', 'SDOT_COLCODE',
    'EXCEPTRSNCODE', 'EXCEPTRSNDESC', 'PEDROWNOTGRNT', 'SPEEDING', 'INATTENTIONIND'], axis = 1, inplace = True)

def transform(df,pd,np):
    
    ################################## Transform column from date to week day ##################################
    # df['WEEKDAY'] = pd.to_datetime(df['INCDATE']).dt.weekday

    ################################## Transform weather column ################################################
    df['WEATHER'].replace(
    to_replace= ('Sleet/Hail/Freezing Rain', 'Blowing Sand/Dirt', 'Severe Crosswind','Partly Cloudy', 'Snowing', np.nan),
    value='Other', inplace=True)
    
    df['WEATHER'].replace(to_replace= np.nan, value='Unknown', inplace=True) 

    ################################## Transform Road Conditions column ########################################
    df['ROADCOND'].replace(to_replace= np.nan,value='Unknown', inplace=True)
    df['ROADCOND'].replace(to_replace=('Dry', 'Wet'), value='Dry/Wet', inplace=True)
    df['ROADCOND'].replace(to_replace=('Ice', 'Snow/Slush'), value='Ice/Snow', inplace=True)
    df['ROADCOND'].replace(to_replace=('Standing Water', 'Sand/Mud/Dirt', 'Oil'), value='Other', inplace=True)

    ################################## Transform Light Conditions column #######################################
    df['LIGHTCOND'].replace(to_replace= np.nan,value='Unknown', inplace=True)
    df['LIGHTCOND'].replace(to_replace=('Dawn', 'Dusk', 'Daylight'), value='Light', inplace=True)
    df['LIGHTCOND'].replace(to_replace=('Dark - Street Lights On', 'Dark - No Street Lights',
    'Dark - Street Lights Off', 'Dark - Unknown Lighting'), value='Dark', inplace=True)

    ################################## Transform Address Column ################################################
    df['ADDRTYPE'].replace(to_replace=np.nan, value='Alley', inplace=True)

    ################################## Transform Collision Type Column #########################################
    # Pedestrian
    mask_pedestrian = \
    (df['COLLISIONTYPE'].isnull()) & \
    (df['SDOT_COLDESC'].str.contains('PEDESTRIAN'))

    df['COLLISIONTYPE'][mask_pedestrian] = 'Pedestrian'

    # Cyclist
    mask_cyclist = \
    (df['COLLISIONTYPE'].isnull()) & \
    (df['SDOT_COLDESC'].str.contains('PEDALCYCLIST'))

    df['COLLISIONTYPE'][mask_cyclist] = 'Cycles'

    # Angles 
    mask_angles = \
    (df['COLLISIONTYPE'].isnull()) & \
    (df['SDOT_COLDESC'].str.contains('ANGLE'))

    df['COLLISIONTYPE'][mask_angles] = 'Angles'

    # Rear End 
    mask_rearend = \
    (df['COLLISIONTYPE'].isnull()) & \
    (df['SDOT_COLDESC'].str.contains('REAR END'))

    df['COLLISIONTYPE'][mask_rearend] = 'Rear Ended'

    # Sideswipe
    mask_sideswipe = \
    (df['COLLISIONTYPE'].isnull()) & \
    (df['SDOT_COLDESC'].str.contains('SIDESWIPE'))

    df['COLLISIONTYPE'][mask_sideswipe] = 'Sideswipe'

    # Other 
    df['COLLISIONTYPE'].fillna('Other', inplace=True)

    # Final Adjustments
    df['COLLISIONTYPE'].replace(to_replace=('Head On', 'Rear Ended'), value= 'Front/Rear', inplace=True)
    df['COLLISIONTYPE'].replace(to_replace=('Pedestrian', 'Cycles'),  value= 'Ped/Cyc',    inplace=True)
    df['COLLISIONTYPE'].replace(to_replace=('Angles', 'Left Turn'),   value= 'Angle/Left', inplace=True) 

    ################################## Vehicle Column ##########################################################
    df['VEHCOUNT'][df['VEHCOUNT']>3] = 3

    ################################## Pedestrian Column #######################################################
    df['PEDCOUNT'][df['PEDCOUNT']>1] = 1

    ################################## Cyclist Column ##########################################################
    df['PEDCYLCOUNT'][df['PEDCYLCOUNT']>1] = 1

    ################################## Persons Column ##########################################################
    df['PERSONCOUNT'][df['PERSONCOUNT']>= 6] = '6 or more'
    df['PERSONCOUNT'][df['PERSONCOUNT']== 0] = '0'
    df['PERSONCOUNT'][df['PERSONCOUNT']== 3] = '3'
    df['PERSONCOUNT'][(df['PERSONCOUNT']==4)|(df['PERSONCOUNT']==5)] = '4/5'
    df['PERSONCOUNT'][(df['PERSONCOUNT']==1)|(df['PERSONCOUNT']==2)] = '1/2'

    ################################## Drop Useless Columns ####################################################
    df.drop(['JUNCTIONTYPE', 'SDOT_COLDESC', 'UNDERINFL', 'ST_COLDESC','HITPARKEDCAR', 'geometry'], axis = 1, inplace = True)

    
def dummies(df,pd):
    df.drop('Unnamed: 0', axis = 1, inplace = True)

    df = pd.get_dummies(df, columns= ['COLLISIONTYPE'])
    df = pd.get_dummies(df, columns= ['ADDRTYPE'])
    df = pd.get_dummies(df, columns= ['WEATHER'])
    df = pd.get_dummies(df, columns= ['LIGHTCOND'])
    df = pd.get_dummies(df, columns= ['ROADCOND'])
    df = pd.get_dummies(df, columns= ['PERSONCOUNT'])
    df = pd.get_dummies(df, columns= ['DISTRICT'])

    df['VEHCOUNT'].replace( to_replace=(0,1,2,3), value=('0','1','2','3 or more'), inplace = True)
    df = pd.get_dummies(df, columns= ['VEHCOUNT'])
    
    df['WEEKDAY'].replace(to_replace=(0,1,2,3,4,5,6), value=('0','1','2','3','4','5','6'), inplace=True)
    df = pd.get_dummies(df, columns= ['WEEKDAY'])


def fill_na_by_percentage(df,np, col):
    r = np.where(df[[col]].isna())[0]
    # r = np.unique(r).tolist()
    l = len(r)
    if l != 0:
        ad = df[col].value_counts(normalize = True)
        # print(ad)
        for i in range(len(ad)):
            L = int(np.floor(l * ad[i]))
            try:
                df[col].fillna(ad.keys()[i], limit = L, inplace = True )
            except:
                r = np.where(df[[col]].isna())[0]
                # r = np.unique(r).tolist()
                l = len(r)
                if l > 0:
                    df[col].fillna(ad.keys()[i], limit = l, inplace = True )
                print('Function terminated')
                return
    else:
        print('No nan values in column')
        return