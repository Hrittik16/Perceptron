import pandas as pd
import random


def random_bmi_generator():
	bmi = []
	for i in range(2500):
		overweight_bmi = random.uniform(25.0, 29.9)
		obese_bmi = random.uniform(30.0, 50.0)
		bmi.append(overweight_bmi)
		bmi.append(obese_bmi)
	return bmi


def prepare_bmi_dataset():
	# read height and weight data
	df = pd.read_csv("data/height_weight.csv")

	# convert inches to meters (1 inch = 0.0254 meters)
	for i in range(df['Height(Inches)'].size):
		df.at[i, 'Height(Inches)'] = df['Height(Inches)'][i]*0.0254
	
	# convert pounds to kilogram (1 lb = 0.45359237 kgs)
	for i in range(df['Weight(Pounds)'].size):
		df.at[i, 'Weight(Pounds)'] = df['Weight(Pounds)'][i]*0.45359237

	# rename the columns
	df.rename(columns={'Height(Inches)': 'Height(m)',
					   'Weight(Pounds)': 'Weight(Kgs)'},
					   inplace=True)

	# calculate bmi (bmi = weight(in kgs)/height^2(in m))
	bmi = []
	category = []
	for i in range(df['Height(m)'].size):
		val = df['Weight(Kgs)'][i]/(df['Height(m)'][i]*df['Height(m)'][i])
		bmi.append(val)

	# randomly generate overweight and obese bmi data
	more_bmi = random_bmi_generator()
	bmi.extend(more_bmi)

	# randomly shuffle bmi list
	random.shuffle(bmi)

	# add weight categories to bmi
	for i in range(len(bmi)):
		if bmi[i] < 18.5:
			category.append("Unhealthy")
		elif bmi[i] < 25.0:
			category.append("Healthy")
		else:
			category.append("Unhealthy")

	# write bmi and category to bmi.csv
	new_df = pd.DataFrame()
	new_df['BMI']  = bmi
	new_df['CATEGORY'] = category
	new_df.to_csv('data/bmi.csv')
	

if __name__ == "__main__":
	# don't need to run prepare_bmi_dataset() again because bmi data is stored in bmi.csv
	# prepare_bmi_dataset()
	pass
