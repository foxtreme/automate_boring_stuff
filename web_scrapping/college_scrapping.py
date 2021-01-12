import pandas as pd
import threading

QC_INSTITUTIONS = "quebec_institutions.csv"
BC_INSTITUTIONS = "british_columbia_institutions.csv"
AB_INSTITUTIONS = "alberta_institutions.csv"
ON_INSTITUTIONS = "ontario_institutions.csv"

df = pd.read_csv(ON_INSTITUTIONS, encoding="ISO-8859-1")
cities = df['City'].unique()
city_dict = {}

for c in cities:
    institutions = []
    for institution in df[df['City'] == c]['Name']:
        institutions.append(institution)
    city_dict[c] = institutions

sorted(city_dict)

