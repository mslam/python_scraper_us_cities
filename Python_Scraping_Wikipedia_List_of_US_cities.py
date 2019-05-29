
# coding: utf-8

# # Mohammad Shafkat Islam
# #### Ph.D. Candidate and Research Assistant
# #### Dept of Electrical and Computer Engineering, The University of Iowa
# #### E-mail: mohammadshafkat-islam@uiowa.edu
# #### Phone: 319-237-5406
# #### LinkedIn: https://www.linkedin.com/in/mshafkat
# #### GitHub: https://github.com/mslam

# # Python Scraping from Wikipedia: 
# This python scraper collects data from wikipedia about the top cities in USA. 
# 
# ### Prerequisites
# 
# It needs Jupyter notebook to run the .ipynb script.
# 
# ```
# https://jupyter.readthedocs.io/en/latest/install.html
# ```
# 
# It needs pandas package:
# 
# ```
# pip install pandas
# 
# ```
# 
# install wikipedia library
# 
# ```
# pip install wikipedia
# 
# ```

# In[ ]:


"""
Step0: Import Necessary libraries:
"""
import pandas as pd
import wikipedia as wp


"""
Step1: Read the html table from wikipedia and find DataFrame object: We read HTML tables into a list of DataFrame objects. It finds the table element, does the parsing and creates a DataFrame.
"""
#The required column names for each of the information extracted from wikipedia page:    
column_names= ["2018 Rank", "City", "State", "2018 estimate","2010 Census", "Change","2016 land area (sq mile)","2016 land area(sq km)","2016 population density (per sq mile)","2016 population density (per sq km)", "location"]    
pd.options.mode.chained_assignment = None 
# Read the html table and find the DataFrame object related to the list of cities.
html = wp.page("List of United States cities by population").html().encode("utf-8")


"""
Step2: Cleaning the data:
    a) Remove the first row since the headers has been manually generated.
    b) Remove the [] which can be found in some cities and states, they are links to the corresponding cities. For our purposes we may not need them.
    c) Convert the values having the corresponding units to simply flaoting point numbers. We may want to process the values.
"""

# read the table and remove the []
us_cities_df = pd.read_html(html, skiprows=1)[4]
us_cities_df = us_cities_df.replace(to_replace ='\[.*', value = '', regex = True)

# clean the data and remove the units from the column values.
list_of_columns_to_be_cleaned = [us_cities_df[6], us_cities_df[7], us_cities_df[8], us_cities_df[9]]
length_of_characters_to_remove = [6,4,6,4]

character_index = 0
for current_column in list_of_columns_to_be_cleaned:
    
    processed_column = current_column
    for i in range (0 ,len(processed_column)):
        
        length_of_current_column_character_to_remove = length_of_characters_to_remove[character_index]
        #print(length_of_current_column_character_to_remove)
        x= str(processed_column[i][:-length_of_current_column_character_to_remove])
        processed_column[i]= x
    character_index +=1
us_cities_df.columns = column_names 
"""
Step3: Scrape data from additional sources: I have written this poriton of the script which extracts additional information.
The goal of this portion is to extrac the crime rate for the most populus cities and combine the information with the previous portion.
"""    
  

# Read the html table and find the DataFrame object related to the list of cities.
crime_column_names = ["State", "City", "Population","Total Violent Crime", "Murder and Nonnegligent manslaughter",
                      "Rape","Robbery","Aggravated assault","Total Property Crime",
                      "Burglary","Larceny-theft","Motor vehicle theft","Arson"]    

crime_rate_html = wp.page("List of United States cities by crime rate").html().encode("utf-8")
crime_rate_df = pd.read_html(crime_rate_html, skiprows=2)[0]

"""
Step4: Clean data for the additional source information:
Since some cities have digits in their names, I cleaned this dataframe. I found the digits in the city name with regular expression and replaced them.
"""
crime_rate_df[1] = crime_rate_df[1].replace(to_replace =r'[0-9]', value = '', regex = True)

crime_rate_df.columns = crime_column_names
crime_rate_df.head()

"""
Step5: Merge the two soruces of data: The objective of this portion is to merge the two data frames. I merge the two dataframes by matching the cities and state names.
There is a problem however, for example the New York City is the name on city name and New York in crime data source. So it only filters down to 89 cities after both sources of information.
"""
merged_df = us_cities_df.merge(crime_rate_df, how = 'inner', on = ['City', 'State'])
merged_df.head()


"""
Step6: Write results into csv files.
"""

us_cities_df.to_csv('us_cities.csv', index=False, encoding = "utf-8")
merged_df.to_csv('us_cities_with_crime_rate.csv', index=False, encoding = "utf-8")
us_cities_df.head()


# Conclusion:
#     I have written a python scraper which collects information about the US cities by population.
#     This reult is shown in us_cities.csv
#     I have also added the ifnomration about crime rate in the us cities.
#     This result is shown in us_cities_with_crime_rate
#     Both of the csv files has been tested for uploading to Big Query.

# In[ ]:



