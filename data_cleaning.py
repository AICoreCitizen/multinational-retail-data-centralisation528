import pandas as pd

class DataCleaning:
    """A utility class for cleaning data from different sources."""

    def __init__(self):
        # Initialize any attributes or parameters here
        pass

    def clean_csv_data(self, df):
        """Clean data from a CSV file and return a pandas DataFrame."""
        # Perform any cleaning steps here, such as removing null values, duplicates, outliers, etc.
        df = df.dropna()
        df = df.drop_duplicates()
        # Return the cleaned DataFrame
        return df

    def clean_api_data(self, data):
        """Clean data from an API endpoint and return a JSON object."""
        # Perform any cleaning steps here, such as filtering, transforming, validating, etc.
        data = data['results'] # Extract the relevant data from the JSON object
        data = [d for d in data if d['status'] == 'success'] # Filter out any failed requests
        # Return the cleaned JSON object
        return data

    def clean_s3_data(self, data):
        """Clean data from an S3 bucket and return a bytes object."""
        # Perform any cleaning steps here, such as decoding, parsing, sanitizing, etc.
        data = data.decode('utf-8') # Decode the bytes object to a string
        data = data.split('\n') # Split the string by newline characters
        data = [d.strip() for d in data if d] # Remove any whitespace and empty lines
        # Return the cleaned bytes object
        return data