def drop_stuff(df,pd):
    df.drop(['X', 'Y', 'OBJECTID', 'INCKEY', 'COLDETKEY', 'REPORTNO','STATUS', 'INCDATE', 'INCDTTM','SDOTCOLNUM',
    'SEGLANEKEY', 'CROSSWALKKEY', 'SEVERITYCODE.1', 'SEVERITYDESC', 'LOCATION','INTKEY', 'ST_COLCODE', 'SDOT_COLCODE',
    'EXCEPTRSNCODE', 'EXCEPTRSNDESC', 'PEDROWNOTGRNT', 'SPEEDING', 'INATTENTIONIND'], axis = 1, inplace = True)

def transform(df,pd):
    
    # Transform column from date to week day
    df['WEEKDAY'] = pd.to_datetime(df['INCDATE']).dt.weekday

    # 