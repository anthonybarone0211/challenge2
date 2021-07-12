# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


#Saves qualifying loans to a csv file if required.
def save_csv(save_csv_path, qualifying_loans, header):

    with open(save_csv_path, 'w', newline = "") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ",")
        if header:
            csvwriter.writerow(header)
        for items in qualifying_loans:
            csvwriter.writerow(items)