# Principles of Data Science – Assignment 1

## Overview

This Python program analyzes and visualizes Kenya’s 2019 Census data on the distribution of households growing various crops and rearing livestock or poultry.
The goal is to explore agricultural patterns across counties and sub-counties.

## Dataset

The dataset used in this project is:

```
distribution-of-households-growing-other-crops-by-type-county-and-sub-county-2019-census-volume-.csv

You can find it in kaggle through: https://www.kaggle.com/datasets/osiroski/distirbution-of-crop-production-kenya-2019-census
```

## How It Works

1. **Loads** the dataset using `pandas`
2. **Cleans** any missing or inconsistent data
3. **Summarizes** agricultural activity by county/sub-county
4. **Visualizes** key distributions using `matplotlib` and `seaborn`

## Visualizations

The script generates several plots to explore the data:

1. **Top 10 Counties/Sub-counties by Cattle Count**
   Displays the regions with the highest cattle populations.

2. **Stacked Bar Chart – Livestock Distribution**
   Shows the proportion of cattle, goats, sheep, and chicken across the top 10 counties.

3. **Poultry and Fish Production Distribution**
   Illustrates the scale of indigenous chicken, layers, broilers, and fish farming activities.

## Libraries Used

* **pandas** – For data loading and cleaning
* **matplotlib** – For plotting visualizations
* **seaborn** – For clean and modern graph styling


## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Install the required libraries:

   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Run the script:

   ```bash
   python datascienceass1.py
   ```
4. View the generated visualizations in pop-up windows.


## Author

**Timothy**
Principles of Data Science – Year 4, Semester 1
