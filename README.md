# Retail Data Centralisation Project

## Project Description
This project is about a multinational company that sells various goods across the globe.
Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.
In an effort to become more data-driven, the organisation would like to make its sales data accessible from one centralised location.

My first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and 
acts as a single source of truth for sales data.

I will then query the database to get up-to-date metrics for the business.

## File Structure of Projects

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
The historical data of users is currently stored in an AWS database in the cloud.
You will now create methods in your DataExtractor and DatabaseConnector class which help extract the information from an AWS RDS database.


Step 1:

Create a db_creds.yaml file containing the database credentials, they are as follows:


RDS_HOST: data-handling-project-readonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com
RDS_PASSWORD: AiCore2022
RDS_USER: aicore_admin
RDS_DATABASE: postgres
RDS_PORT: 5432


You should add your db_creds.yaml file to the .gitignore file in your repository, so that the database credentials are not uploaded to your public GitHub repository.
If you don't currently have a .gitignore file, you can create one by typing touch .gitignore in the terminal. Then just add the names of any files you don't want git to track.


Now you will need to develop methods in your DatabaseConnector class to extract the data from the database.


Step 2:

Create a method read_db_creds this will read the credentials yaml file and return a dictionary of the credentials.
You will need to pip install PyYAML and import yaml to do this.


Step 3:

Now create a method init_db_engine which will read the credentials from the return of read_db_creds and initialise and return an sqlalchemy database engine.


Step 4:

Using the engine from init_db_engine create a method list_db_tables to list all the tables in the database so you know which tables you can extract data from.
Develop a method inside your DataExtractor class to read the data from the RDS database.


Step 5:

Develop a method called read_rds_table in your DataExtractor class which will extract the database table to a pandas DataFrame.

It will take in an instance of your DatabaseConnector class and the table name as an argument and return a pandas DataFrame.
Use your list_db_tables method to get the name of the table containing user data.
Use the read_rds_table method to extract the table containing user data and return a pandas DataFrame.


Step 6:

Create a method called clean_user_data in the DataCleaning class which will perform the cleaning of the user data.

You will need clean the user data, look out for NULL values, errors with dates, incorrectly typed values and rows filled with the wrong information.


Step 7:

Now create a method in your DatabaseConnector class called upload_to_db. This method will take in a Pandas DataFrame and table name to upload to as an argument.


Step 8:

Once extracted and cleaned use the upload_to_db method to store the data in your sales_data database in a table named dim_users.

### Task 4 - Extracting Users and cleaning card details

### Task 5 - Extract and clean the details of each store


### Task 6 - Extract and clean the product details

### Task 7 - Retrieve and clean the orders table

### Task 8 - Retrieve and clean the date events data



## Milestone 3 - Create Database Schema

### Task 1 - Set up a new database to store the data


## Milestone 4 - Querying the Data

### Task 1 - Set up a new database to store the data






