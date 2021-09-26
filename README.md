# power_data_analytics_tools
 Code for analysis of electric power data, written in python.
 
# About
This repository contains code for some basic analysis, forecast, and cleanup of electric power generation and consumption data. This code was written as a part of Science Internship Program (SIP) 2021 at UC Santa Cruz by Alexandra 'Alex' Weiss, Michaela Chou, and Pranav Amarnath, and the project was mentored by Shourya Bose.

The code is organized in modules, which can be found in the folder 'modules'. All datasets used for this project can be found in the folder 'datasets', and was sourced from the open internet. The description of the modules and datasets follow. Please see the description of the modules for knowing about their respective authors.

## Modules

**Module 1**: This module contains code for linear regression of power demand data. Subfolders '1a', '1b', and '1c' in the main folder each contain code which essentially do the same aforementioned thing, but have been wrriten by different people.  
**Datasets Used**: Dataset 1  
**Authorship**:  
'1a' - Alex  
'1b' - Michaela  
'1c' - Pranav

**Module 2**: This module contains code which tries to find optimal polynomial degree for regression in power demand data. This is done by computing the polynomial degree which results in the lowest loss over the dataset.  
**Datasets Used**: Dataset 1  
**Authorship**: Alex

**Module 3**: This module contains code which essentially does the same task as module2, i.e. find the optimal degree for polynomial regression. However, as compared to module2, instead of calculating the loss over the entire dataset, the dataset is split into training and test, and loss is only calculated over the test dataset.  
**Datasets Used**: Dataset 1  
**Authorship**: Alex

**Module 4**: This module contains code to test ARIMA as an alternative to polynomial regression for predicting power demand data. For each of a collection of 9 CA counties, this code calculates which of the two methods gives the lowest validation loss. If the method is polynomial regression then the optimal polynomial degree is computed, and if the method is ARIMA, then the optimal ARIMA parameters (p,d,q) is computed.  
**Datasets Used**: Dataset 1  
**Authorship**: Alex

**Module 5**: This module contains code which does a multivariate linear regression to forecast power demand in 9 CA counties. The features used are population, GDP, revenue collected by county, rainfall, and the year itself.  
**Datasets Used**: Datasets 1,2,3,4  
**Authorship**: Michaela

**Module 6**: This module contains code which increases the resolution of the power generation data in dataset5 from 1 hour to half an hour. The increase in result is achieved through interpolation.  
**Datasets Used**: Dataset 5  
**Authorship**: Michaela

** Module 7**: This module contains code to carry out ARIMA forecasting on the power generation data from dataset5.  
**Datasets Used**: Dataset 5  
**Authorship**: Michaela

**Module 8**: This module contains code to carry out multivariate linear regression of power demand data using data from dataset1, dataset2, and dataset3. The 'extra' folder in the module also contains different code snippets used to clean up the aforementioned data for use in multivariate regression.  
**Datasets Used**: Datasets 1,2,3  
**Authorship**: Pranav

**Module 9**: This module contains two different subfolders, '9a' and '9b'. '9a' contains code to download from the internet and clean up the power generation data contained in dataset 5. '9b' contains code to use interpolation to fill up some blocks of data which are missing in the original online data source.  
**Datasets Used**: Dataset 5  
**Authorship**: Pranav

**Module 10**: This module contains code to measure the robustness of ARIMA as a prediction method against missing data. A plot is computed comparing the validation loss of ARIMA versus probability of dropping any given point i.i.d (independent and identically distributed) from the training dataset. As expected, as the probability of dropping points increases, the ARIMA validation loss increases.  
**Datasets Used**: Dataset 5  
**Authorship**: Pranav

## Datasets

**Dataset1**: Annual power demand of different CA counties over the years 1990-2019.  
**Files**:  
data1.csv - power demand for Alameda, San Mateo, Los Angeles 1990-2019  
data2.csv - power demand for Merced, Santa Clara, Riverside 1990-2019  
data3.csv - power demand for San Diego, Santa Barbara, Santa Cruz 1990-2019  
Source(s): http://www.ecdms.energy.ca.gov/elecbycounty.aspx

**Dataset 2**: Population of various CA counties from 1990-2019  
**Files**:  
CA_pop_data_1990_1999.txt - population of various CA counties from 1990-1999  
CA_pop_data_2000_2009.xls - population of various CA counties from 2000-2009  
CA_pop_data_2010_2019.xlsx - population of various CA counties from 2010-2019  
**Source(s)**:  
https://www.census.gov/library/publications/1992/dec/cp-1.html  
https://www2.census.gov/programs-surveys/popest/tables/2000-2010/intercensal/county/co-est00int-01-06.xls  
https://www2.census.gov/programs-surveys/popest/tables/2010-2019/counties/totals/co-est2019-annres-06.xlsx  

**Dataset 3**: Revenue raised by various CA counties from 2003-2019  
**Files**:  
USA_county_revenue_per_capita_data_2003_2019.csv - revenue raised by various CA countirs from 223-2019  
**Source(s)**: https://counties.bythenumbers.sco.ca.gov/#!/year/default

**Dataset 4**: Anuual GDP and rainfall of various counties in CA from 1990-2019  
**Files**:  
gdp_by_county.xlsx - annual GDP of various CA counties 1990-2019  
rainfall_by_county.xlsx - annual rainfall level (inches) of various CA counties 1990-2019  
**Source(s)**: [to be updated]

**Dataset 5**: Amount of energy generated by various generation sources in CA 6/1/18-7/13/21  
**Files**:  
power_generation_processed.xlsx - energy generation data 6/1/18-13/7/21 in 1 hour resolution  
**Source(s)**: http://www.caiso.com/market/Pages/ReportsBulletins/RenewablesReporting.aspx
