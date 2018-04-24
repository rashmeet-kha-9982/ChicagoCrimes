#Remove columns "Location Description and Location - Redundant Columns"
import pandas as pd
f=pd.read_csv("E:\Rashmeet_SJSU\Sem II\CS- 185C -02 Big Data\Project\Crimes_-_2018.csv")
keep_col = ['ID','Case Number','Date','Block','IUCR','Primary Type','Description','Arrest','Domestic','Beat','District','Ward','Community Area','FBI Code','X Coordinate','Y Coordinate','Year','Updated On','Latitude','Longitude']
new_f = f[keep_col]

#Check for and replace null values with 0
new_f.isnull().sum()
mod = new_f.fillna("0")
mod.isnull().sum()

#Remove unwanted commas from Description column
desc = mod["Description"].str.replace(","," ")
mod["Description"]= desc.values	
temp = pd.DataFrame()	

#Extract data subset corresponding to years 2017 & 2018
for y in range(2017, 2019):
	temp = temp.append(mod[mod.Year == y])
	
#Save modified data to a new csv
temp.to_csv("crimeTest4.csv",index=False)