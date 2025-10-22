import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


#loading the dataset
df = pd.read_csv('distribution-of-households-growing-other-crops-by-type-county-and-sub-county-2019-census-volume-.csv')
df.head() #confiremed that it was loaded successfully


#basic info about the dataset
print(df.info())
print(df.describe())


#checking for missing values and filling the gaps
print("Missing values per column:\n", df.isnull().sum())
df = df.fillna(0)

#so if some columns are too incomplete, i dropped them here
threshold = len(df) * 0.5  # keep columns that have at least 50% data
df = df.dropna(thresh=threshold, axis=1)



#Making all column names lowercase and replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

#Triming spaces from text fields
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

#Converting numeric columns properly
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].replace({',': ''}, regex=True)
        try:
            df[col] = df[col].astype(float)
        except:
            pass



#removing duplicate rows
duplicates = df[df.duplicated()]
print("Number of duplicates:", len(duplicates))
df = df.drop_duplicates()



#saving the cleaned dataset
df.to_csv("cleaned_kenya_crop_data.csv", index=False)
print("Cleaned dataset saved successfully!")









#extras:visualization
# Load dataset
df = pd.read_csv("cleaned_kenya_crop_data.csv")

#Top 10 Counties/Sub-counties by total Households
plt.figure(figsize=(12, 6))
top_counties = df.sort_values(by="total", ascending=False).head(10)
sns.barplot(x="total", y="county/sub_county", data=top_counties, hue="county/sub_county", dodge=False, legend=False, palette="viridis")
plt.title("Top 10 Counties/Sub-counties by Total Households")
plt.xlabel("Total Households")
plt.ylabel("County/Sub-county")
plt.tight_layout()
plt.show()

#omparing main farming activities across Kenya
selected_columns = [
    "farming", 
    "crop_production", 
    "livestock_production", 
    "aquaculture", 
    "fishing", 
    "irrigation"
]

activity_totals = df[selected_columns].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=activity_totals.values, y=activity_totals.index, hue=activity_totals.index, dodge=False, legend=False, palette="mako")
plt.title("Total Households by Main Farming Activities (Kenya 2019)")
plt.xlabel("Total Households")
plt.ylabel("Activity Type")
plt.tight_layout()
plt.show()

#Heatmap showing livestock and poultry types by region
subset_columns = [
    "county/sub_county", 
    "indigenous_cattle", 
    "exotic_cattle_0dairy", 
    "exotic_cattle_0beef",
    "sheep", 
    "goats", 
    "indigenous_chicken", 
    "exotic_chicken_layers", 
    "exotic_chicken_broilers"
]

subset = df[subset_columns].set_index("county/sub_county")

plt.figure(figsize=(14, 10))
sns.heatmap(subset, cmap="YlGnBu", cbar_kws={"label": "Household Count"})
plt.title("Distribution of Livestock and Poultry by County/Sub-county")
plt.xlabel("Animal Type")
plt.ylabel("County/Sub-county")
plt.tight_layout()
plt.show()

