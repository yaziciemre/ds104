
#: Imports
import numpy as np
import ast
import pandas as pd
import json

# 01: Read the input file
# NOTE, might be splited by ";"
# NOTE, might have utf-8 problem
# NOTE, might have mixed type problem
df = pd.read_csv("sampled_user_cars_data.csv")

# 02: Delete the unnecessary COLUMNS
# NOTE, uniques! if they do not have any information
# NOTE, delete mostly empty
# NOTE, delete incorrect
# NOTE, identical
# NOTE, unnecessary
del df['vin']
del df['sp_id']
del df['bed_height']
del df['listing_id']
del df['trimId']
del df['engine_cylinders']
del df['dealer_zip']
del df['city']

# QUICK LOOKUP
for c in df:
	ratio = round(len(df[df[c].isnull()]) / len(df), 3)
	if ratio > 0.95:
		del df[c]

# 03: Deal with nulls
df['main_picture_url'] = df['main_picture_url'].isnull()
df['back_legroom'] = df['back_legroom'].replace('--', None)
df['bed_length'] = df['bed_length'].replace('--', None)
df['length'] = df['length'].replace('--', None)
df['height'] = df['height'].replace('--', None)
df['front_legroom'] = df['front_legroom'].replace('--', None)
df['fuel_tank_volume'] = df['fuel_tank_volume'].replace('--', None)
df['width'] = df['width'].replace('--', None)
df['wheelbase'] = df['wheelbase'].replace('--', None)
df['maximum_seating'] = df['maximum_seating'].replace('--', None)
df['torque'] = df['torque'].replace('nan', None)
df['power'] = df['power'].replace('--', None)

# 04: Transofmration
def replacer1( value ):
	if value == None:
		return None
	return float(str(value).replace(' in', ''))

def replacer2( value ):
	if value == None:
		return None
	return float(str(value).replace(' gal', ''))

def replacer3( value ):
	if value == None:
		return None
	if str(value) == 'nan':
		return None
		#400 lb-ft @ 4,400 RPM
	# VERY IMPORTANT
	return float(str(value).split(" @ ")[1].replace(',', '.').replace(' RPM', ''))


def replacer4( value ):
	if value == None:
		return None
	if str(value) == 'nan':
		return None
		#400 lb-ft @ 4,400 RPM
	# VERY IMPORTANT
	return float(str(value).split(" ")[0])

def replacer5( value ):
	if value == None:
		return None
	if str(value) == 'nan':
		return None
	return float(str(value).replace(' seats', ''))

df['length'] = df['length'].apply( replacer1 )
df['height'] = df['height'].apply( replacer1 )
df['back_legroom'] = df['back_legroom'].apply( replacer1 )
df['bed_length'] = df['bed_length'].apply( replacer1 )
df['front_legroom'] = df['front_legroom'].apply( replacer1 )
df['fuel_tank_volume'] = df['fuel_tank_volume'].apply( replacer2 )
df['width'] = df['width'].apply( replacer1 )
df['wheelbase'] = df['wheelbase'].apply( replacer1 )
df['maximum_seating'] = df['maximum_seating'].apply( replacer5 )

# 05: Replacements
for c in ['fleet', 'frame_damaged', 'franchise_dealer', 
	'has_accidents', 'isCab', 'is_cpo', 'is_new', 'main_picture_url',
	'theft_title', 'salvage']:
	df[c] = df[c].replace({"False": 0, "True": 1, True: 1, False: 0})

#: 06: Parsing
def parser1( value ):
	if value == None:
		return []
	if str(value) == 'nan':
		return []
	if str(value) == "":
		return []
	return ast.literal_eval(value) 

df['major_options'] = df['major_options'].apply(parser1)
df['major_options_count'] = df['major_options'].apply(lambda value: len(value))

# 07: Spliting
df['torque_rpm'] = df['torque'].apply( replacer3 ) * 1000
df['torque'] = df['torque'].apply( replacer4 )

df['power_rpm'] = df['power'].apply( replacer3 )
df['power'] = df['power'].apply( replacer4 )

# 08: Remove some parts!
# df = df.select_dtypes(include = ['object'])

# 09: Text processing
for c in ['exterior_color', 'listing_color', 'interior_color']:
	df[c] = df[c].str.lower()

# Is it black or not
df['interior_color'] = df['interior_color'].apply(lambda value: 'black' in str(value))
df['interior_color'] = df['interior_color'].astype(int)

df['exterior_color'] = df['exterior_color'].apply(lambda value: 'black' in str(value))
df['exterior_color'] = df['exterior_color'].astype(int)

df['listing_color'] = df['listing_color'].apply(lambda value: 'black' in str(value))
df['listing_color'] = df['listing_color'].astype(int)


# 10: Is it in?
df['sp_name'] = df.apply(lambda x: x['make_name'] in x['sp_name'], axis=1)

# 11: Downcast -- Narrow down
def downcast1( value ):
	if value == None:
		return None
	if str(value) == 'None' or str(value) == 'NaN':
		return None
	if str(value) == 'nan':
		return None

	value = value.replace(' Automatic', '')
	value = value.replace(' Manual', '')
	value = value.replace('Continuously Variable Transmission', '')
	value = value.replace(' Dual Clutch', '')
	value = value.replace(' Overdrive', '')
	value = value.replace(' CVT', '')
	value = value.replace('Manual', '')
	return value

df['transmission_display'] = df['transmission_display'].apply(downcast1)
del df['transmission_display']

# 12: Dummy
df = pd.get_dummies(df, columns = ['transmission'])


"""
for c1 in df:
	for c2 in df:
		if c1 < c2:
			if c1 != 'test' and c2 != 'test':
				df['test'] = ( df[c1] == df[c2] ).astype(int)
				r = df['test'].mean()
				if r > 0.60:
					print(c1, c2, r)
"""

# 13: As numeric
for c in ['exterior_color', 'interior_color', 'sp_name', 'listing_color', 'transmission_A','transmission_CVT','transmission_Dual Clutch','transmission_M']:
	df[c] = df[c].astype(int)

# FOR NOW, WE SKIP SOME CATEGORICA VARIABLES
df = df.select_dtypes(exclude = ['object'])

# 14: Fill
# NOTE, with mean
for c in ['back_legroom', 'city_fuel_economy', 'engine_displacement', 
	'front_legroom', 'fuel_tank_volume', 'height','highway_fuel_economy','horsepower',
	'length', 'maximum_seating', 'mileage', 'power',
	'seller_rating','torque','wheelbase','width','torque_rpm','power_rpm']:
	df[c] = df[c].fillna( df[c].mean() )







# NOTE, null or not
for c in ['bed_length']:
	df[c] = df[c].isnull()
	df[c] = df[c].astype(int)

# NOTE, with zero
for c in ['fleet', 'frame_damaged', 'has_accidents', 'isCab', 'is_cpo', 'salvage', 'theft_title']:
	df[c] = df[c].fillna(0)

# NOTE, with 1
df['owner_count'] = df['owner_count'].fillna(1)

# 15: Remove inter correlated
del df['length']
del df['exterior_color']
del df['horsepower']
del df['fleet']
del df['highway_fuel_economy']

# 16: Re-scale the features
df['year'] = 2021 - df['year']

for c in df:
	cc = df[c].corr(df['price'])
	cc = int(cc * 100)
	if abs(cc) <= 10:
		del df[c]


#: 99: Save to see
df.to_csv("week14_processed.csv", index = False)
