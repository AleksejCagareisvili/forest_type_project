def distance(x, y):
	return (x.astype('int32')**2 + y.astype('int32')**2) ** 0.5

def return_df(df):
	df['distance_HoHy_VeHy'] = distance(df['Horizontal_Distance_To_Hydrology'], df['Vertical_Distance_To_Hydrology'])
	df['distance_HoHy_HoRo'] = distance(df['Horizontal_Distance_To_Hydrology'], df['Horizontal_Distance_To_Roadways'])
	df['distance_HoHy_HoFi'] = distance(df['Horizontal_Distance_To_Hydrology'], df['Horizontal_Distance_To_Fire_Points'])
	df['distance_VeHy_HoRo'] = distance(df['Vertical_Distance_To_Hydrology'], df['Horizontal_Distance_To_Roadways'])
	df['distance_VeHy_HoFi'] = distance(df['Vertical_Distance_To_Hydrology'], df['Horizontal_Distance_To_Fire_Points'])
	df['distance_HoRo-HoFI'] = distance(df['Horizontal_Distance_To_Roadways'], df['Horizontal_Distance_To_Fire_Points'])

	df['minus_HoHy_VeHy'] = abs(df['Horizontal_Distance_To_Hydrology'] - df['Vertical_Distance_To_Hydrology'])
	df['minus_HoHy_HoRo'] = abs(df['Horizontal_Distance_To_Hydrology'] - df['Horizontal_Distance_To_Roadways'])
	df['minus_HoHy_HoFi'] = abs(df['Horizontal_Distance_To_Hydrology'] - df['Horizontal_Distance_To_Fire_Points'])
	df['minus_VeHy_HoRo'] = abs(df['Vertical_Distance_To_Hydrology'] - df['Horizontal_Distance_To_Roadways'])
	df['minus_VeHy_HoFi'] = abs(df['Vertical_Distance_To_Hydrology'] - df['Horizontal_Distance_To_Fire_Points'])
	df['minus_HoRo-HoFI'] = abs(df['Horizontal_Distance_To_Roadways'] - df['Horizontal_Distance_To_Fire_Points'])

	df['sum_HoHy_VeHy'] = df['Horizontal_Distance_To_Hydrology'] + df['Vertical_Distance_To_Hydrology']
	df['sum_HoHy_HoRo'] = df['Horizontal_Distance_To_Hydrology'] + df['Horizontal_Distance_To_Roadways']
	df['sum_HoHy_HoFi'] = df['Horizontal_Distance_To_Hydrology'] + df['Horizontal_Distance_To_Fire_Points']
	df['sum_VeHy_HoRo'] = df['Vertical_Distance_To_Hydrology'] + df['Horizontal_Distance_To_Roadways']
	df['sum_VeHy_HoFi'] = df['Vertical_Distance_To_Hydrology'] + df['Horizontal_Distance_To_Fire_Points']
	df['sum_HoRo-HoFI'] = df['Horizontal_Distance_To_Roadways'] + df['Horizontal_Distance_To_Fire_Points']

	# Создание признаков для Elevation
	df['distance_Elev_VeHy'] = distance(df['Elevation'], df['Vertical_Distance_To_Hydrology'])
	df['distance_Elev_HoHy'] = distance(df['Elevation'], df['Horizontal_Distance_To_Hydrology'])
	df['distance_Elev_HoRo'] = distance(df['Elevation'], df['Horizontal_Distance_To_Roadways'])
	df['distance_Elev_HoFi'] = distance(df['Elevation'], df['Horizontal_Distance_To_Fire_Points'])


	df['minus_Elev_VeHy'] = abs(df['Elevation'] - df['Vertical_Distance_To_Hydrology'])
	df['minus_Elev_HoHy'] = abs(df['Elevation'] - df['Horizontal_Distance_To_Hydrology'])
	df['minus_Elev_HoRo'] = abs(df['Elevation'] - df['Horizontal_Distance_To_Roadways'])
	df['minus_Elev_HoFi'] = abs(df['Elevation'] - df['Horizontal_Distance_To_Fire_Points'])


	df['sum_Elev_VeHy'] = df['Elevation'] + df['Vertical_Distance_To_Hydrology']
	df['sum_Elev_HoHy'] = df['Elevation'] + df['Horizontal_Distance_To_Hydrology']
	df['sum_Elev_HoRo'] = df['Elevation'] + df['Horizontal_Distance_To_Roadways']
	df['sum_Elev_HoFi'] = df['Elevation'] + df['Horizontal_Distance_To_Fire_Points']

	return df
