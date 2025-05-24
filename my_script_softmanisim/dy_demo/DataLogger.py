# https://gemini.google.com/app/0c13af4b6739b793
# save the data at the end of file
# update： 2025-04-23 created the DataLogger class

import numpy as np
import time
from pathlib import Path
import pandas as pd

class DataLogger:
    
    def __init__(self, output_dir_base = ".", filename_prefix="sim_data", 
                 fieldnames=None):
        """
        Initialize the DataLogger class.

        Args:
            output_dir_base (str or Path): The base directory to save data in.
            filename_prefix (str): prefix for the output CSV filename.
            fieldnames (list): List of column headers for the CSV file.
        """
        self.output_dir = Path(output_dir_base)
        self.filename_prefix = filename_prefix
        if fieldnames is None:
            raise ValueError("Fieldnames must be provided.")
        self.fieldnames = fieldnames
        self._data_rows =[]
        # Ensure the output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
        print(f"[DataLogger] Initialized. Data will be saved in: {self.output_dir.resolve()}")
        
    def log(self, data_dict):
        """
        logs a single row of data.
        
        Args:
            data_dict (dict): A dictionary where keys match the fieldnames. 
        """
        self._data_rows.append(data_dict)
        
    def get_data_frame(self):
        """ Converts the logged data into a Pandas DataFrame. """
        if not self._data_rows:
            raise ValueError("No data logged yet.")
            return pd.DataFrame(columns=self.fieldnames)    
        # if success, 
        return pd.DataFrame(self._data_rows, columns=self.fieldnames)
    
    def save(self, timestamp_format="%Y%m%d_%H%M%S"):
        """
        Saves all logged data to a timestamped CSV file. 

        Args:
            timestamp_format (str, optional): _description_. Defaults to "%Y%m%d_%H%M%S".
            
        Returns:
            Path or None: the Path object of the saved file or None if no data was logged.
        """
        if not self._data_rows:
            print("[DataLogger] No data to save.")
            return None
        
        timestamp = time.strftime(timestamp_format)
        filename = self.output_dir / f"{self.filename_prefix}_{timestamp}.csv"
        
        output_df = self.get_data_frame() # Get data as DataFrame
        
        output_df.to_csv(filename, index=False, encoding='utf-8')
        print(f"[DataLogger] {len(output_df)} data rows saved successfully to: {filename.resolve()}")
        
    def __len__(self):
        """ Returns the number of logged data rows. """
        return len(self._data_rows)
        
                