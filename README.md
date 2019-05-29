# Python Scraper to collect data from Wikipeda:

This python scraper collects data from wikipedia about the top cities in USA. 

## Getting Started

These instructions provide prerequisites necessary to run this program.

## Prerequisites

It needs Jupyter notebook to run the .ipynb script.

```
https://jupyter.readthedocs.io/en/latest/install.html
```

It needs pandas package:

```
pip install pandas

```

install wikipedia library

```
pip install wikipedia
```

## Running the Script:
We can either run the python script, or the jupyter script.
The different parts of the script are below:


### Step0:
Import Necessary libraries

### Step1: 
Read the html table from wikipedia and find DataFrame object: We read HTML tables into a list of DataFrame objects. It finds the table element, does the parsing and creates a DataFrame.
The required column names for each of the information extracted from wikipedia page.
Read the html table and find the DataFrame object related to the list of cities

### Step2:
Cleaning the data:
    a) Remove the first row since the headers has been manually generated.
    b) Remove the [] which can be found in some cities and states, they are links to the corresponding cities. For our purposes we may not need them.
    c) Convert the values having the corresponding units to simply flaoting point numbers. We may want to process the values.

### Step3:
Scrape data from additional sources: I have written this poriton of the script which extracts additional information.
The goal of this portion is to extract the crime rate for the most populus cities.
After extracting the information it combine the information with the previous portion which contains population information.

### Step4: 
Clean data for the additional source information:
Since some cities have digits in their names, I cleaned this dataframe. I found the digits in the city name with regular expression and replaced them.

### Step5:
Merge the two soruces of data: The objective of this portion is to merge the two data frames. I merge the two dataframes by matching the cities and state names.
There is a problem however, for example the New York City is the name on city name and New York in crime data source. So it only filters down to 89 cities after both sources of information.
### Step6:
Step6: Write results into csv files.


## Conclusion



Conclusion: I have written a python scraper which collects information about the US cities by population. 
This reult is shown in us_cities.csv 
I have also added the ifnomration about crime rate in the us cities. 
This result is shown in us_cities_with_crime_rate
Both of the csv files has been tested for uploading to Big Query.


## Authors

* **Mohammad Shafkat Islam** 

