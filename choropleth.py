import json 
import shapely
from shapely.geometry import Point, Polygon
import shapely.speedups
import geopandas, folium

def gen_choro(df, np,pd):
    m = folium.Map(location=[47.70314032, -122.323148],zoom_start= 11 )

    gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.X, df.Y))

    shapely.speedups.enable()

    a = open('D:/personale/MACHINELEARNING/IBM/python for machine learning/Final Project/seattle_districts.json')

    f = json.load(a)



    # Create districts
    df['DISTRICT'] = np.nan

    for i in range(7):
        distr= f['features'][i]['geometry']['coordinates']
        d = []
        for j in range(len(distr[0])):
            d.append(distr[0][j]) 
        
        D = Polygon(d)

        r= np.where(gdf['geometry'].within(D))[0]
        df['DISTRICT'][r] = i

    # Create dataframe for the choropleth
    dis = {'DISTRICT': [1,2,3,4,5,6,7],
        'TOTAL': [6027,11641,8975,6047,6043,6233,11111]
        }
    df1 = pd.DataFrame(dis, columns = ['DISTRICT', 'TOTAL'])
    
    # Generate the choropleth
    m.choropleth(
    geo_data=f,
    data=df1,
    columns=['DISTRICT', 'TOTAL'],
    key_on='feature.properties.district',
    fill_color='YlOrRd', 
    fill_opacity=0.6, 
    line_opacity=0.5,
    legend_name='Accident'
    )

    m