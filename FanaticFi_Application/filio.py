import csv
from pathlib import Path
import pandas as pd

def load_csv(csvpath): #defining function load_csv 
    
    with open(csvpath, "r") as csvfile: #use with open function to open the csv file from the Path as a reader csvfile
        data = [] #create a new list for data to append data to later on
        csvreader = csv.reader(csvfile, delimiter=",") #names file inputted as the csvreader and opens by passing csvfile

        # next(csvreader) # Skip the CSV Header

        for row in csvreader: #iterates through the rows od data in the csv file given
            data.append(row) #appends the empty list data with the new rows of data
    data_df = pd.DataFrame(data)
    return data_df #Returns data frame from the csv file inputted
