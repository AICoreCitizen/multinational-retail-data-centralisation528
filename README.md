# Retail Data Centralisation Project

## Project Description
This project is about a multinational company that sells various goods across the globe.
Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.
In an effort to become more data-driven, the organisation would like to make its sales data accessible from one centralised location.

My first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and 
acts as a single source of truth for sales data.

I will then query the database to get up-to-date metrics for the business.

## File Strcuture of Projects

## Milestone 1 - Set up Github Repo


## Milestone 2 - Extract and Clean data from the data Sources

### Task 1 - Set up a new database to store the data
Initialise a new database locally to store the extracted data.
Set up a new database within pgadmin4 and name it sales_data.
This database will store all the company information once you extract it for the various data sources.

In this task you will be defining the scripts and Classes you will use to extract and clean the data from multiple data sources.
The Class methods won't be defined in this step yet they will be defined when required in the subsequent tasks.

### Task 2 - Initialise 3 Project Classes
Step 1:
Create a new Python script named data_extraction.py and within it, create a class named DataExtractor.
This class will work as a utility class, in it you will be creating methods that help extract data from different data sources.
The methods contained will be fit to extract data from a particular data source, these sources will include CSV files, an API and an S3 bucket.


Step 2:
Create another script named database_utils.py and within it, create a class DatabaseConnector which you will use to connect with and upload data to the database.


Step 3:
Finally, create a script named data_cleaning.py this script will contain a class DataCleaning with methods to clean data from each of the data sources.

### Task 3 - Extract and clean the User data

### Task 4 - Extracting Users and cleaning card details

### Task 5 - Extract and clean the details of each store


### Task 6 - Extract and clean the product details

### Task 7 - Retrieve and clean the orders table

### Task 8 - Retrieve and clean the date events data



## Milestone 3 - Create Database Schema

### Task 1 - Set up a new database to store the data


## Milestone 4 - Querying the Data

### Task 1 - Set up a new database to store the data






