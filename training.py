import pandas as pd
import numpy as np
from sklearn import linear_model
import math


#  Data preeprocessing (Handle Missing Values)

df = pd.read_csv('college_2.csv')

# _NO2 = df.NO2.median()
# df.NO2 = df.NO2.fillna(_NO2)

# _wind_speed = df.wind_speed.median()
# df.wind_speed = df.wind_speed.fillna(_wind_speed)


# _road_dens = df.road_dens.median()
# df.road_dens = df.road_dens.fillna(_road_dens)

# _pp_dens = df.pp_dens.median()
# df.pp_dens = df.pp_dens.fillna(_pp_dens)

# _earth_no2 = df.earth_no2.median()
# df.earth_no2 = df.earth_no2.fillna(_earth_no2)

# df.to_csv('college_2.csv', index=False)


# training model

# reg = linear_model.LinearRegression()
# reg.fit(df[['wind_speed', 'road_dens', 'pp_dens', 'earth_no2']], df.NO2)

# print(reg.coef_)
# # [-1.05050221e+02 -5.40138834e-02  1.60809930e+00  1.05491448e+02]
# print(reg.intercept_)
# # 511.7305174172126

trainingData = df[['NO2', 'wind_speed', 'road_dens', 'pp_dens', 'earth_no2']]
trainingData.to_csv('trainingData.csv', float_format='{:f}'.format, index=False)
