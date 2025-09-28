#!/usr/bin/env python
# coding: utf-8

# # {Teen Pregnancy and Sex Education in the US}📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 <!-- Answer Below -->
# 
# I am addressing the problem of teen pregnancy in the United States and examining if and how it relates to a lack of sex education. 

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->
# 
# The specific question I am seeking to answer with this project is: "Is there a correlation between lack of sex education and increased teen pregnancy?"

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->
# 
# An answer could be expressed with a visualization such as a table or a bar chart showcasing the states with the highest and lowest teen pregnancy numbers, their overall population, and  their policies surrounding sex education. 
# 
# The answer itself would be: "Yes/No, there is/isn't strong evidence to suggest increased teen pregnancy directly correlates to a lack of sex education." 

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->
# 
# My datasets are:
# - CDC Wonder (https://wonder.cdc.gov/controller/datarequest/D149;jsessionid=C8DCABB90CDF366055F96EA1D525 and https://wonder.cdc.gov/controller/datarequest/D192;jsessionid=70DEF061E23E358712E1506B71DF). This is a query based data source that allows you to view birth rates with different filters. I have imported the 2016-2024 and 2024-2025 natality datasets. 
# 
# - The United States Census (https://data.census.gov/table?q=teen+population+by+state&y=2024). This is united states census data filtered to focus on teens aged 15-19. 
# 
# - Parents Defending Education: Sex Education Laws By State (https://actionpde.org/sex-education-laws-by-state/). This is a website showcasing sex education laws by state. I have downloaded the website data as a PDF and extracted the raw text using pdfplumber. 
# 
# I will relate these datasets by state. When applicable, I will also use year, "Mandate Sex Ed" (Sex Education Laws By State), and age. 

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->
# 
# My approach will be to:
# - Calculate the average and raw teen pregnancy rate per state using census population numbers and CDC natality data. 
# 
# - Extract data from the Sex Education Laws by State site and convert it into a usable table, including whether sex education is required and how comprehensive it is. 
# 
# - Connect datasets by year and when applicable "Mandata Sex Ed" and/or age. 
# 
# - Explore visualizations to illustrate the data and results. 

# In[ ]:


# Start your code here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import pdfplumber


# Importing my sources: 

#Census data: 
census = pd.read_csv("ACSST1Y2024.S0902-2025-09-28T050122.csv")
#Birth data from 2016-2024
BirthData20162024 = pd.read_csv("Natality, 2016-2024 expanded.csv")
#Birth data from 2023 to July 2025
BirthData2025 = pd.read_csv("Provisional Natality, 2023 through Last Month.csv")

# using pdfplumber to extract text from PDE-Action_-Sex-Education-State-Laws_v2-1.pdf, which will later be used to create a dataframe
with pdfplumber.open("PDE-Action_-Sex-Education-State-Laws_v2-1.pdf") as pdf:
    first_page = pdf.pages[0]
    pdf_text = first_page.extract_text()


# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[2]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

