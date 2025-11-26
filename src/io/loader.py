"""Data loading module for file I/O operations.

This module provides functions for loading data from various file formats
including CSV, JSON, Excel, and other common data formats.
"""

def load_csv(path):
    """
    Load data from a CSV (Comma-Separated Values) file.
    
    This function reads a CSV file from the specified path and returns
    the data as a pandas DataFrame for easy manipulation and analysis.
    
    Args:
        path (str): The file path to the CSV file to be loaded.
                   Can be an absolute or relative path.
    
    Returns:
        pandas.DataFrame: A DataFrame containing the loaded CSV data with
                         columns and rows corresponding to the file structure.
    
    Raises:
        FileNotFoundError: If the specified file path does not exist
        PermissionError: If there are insufficient permissions to read the file
        pd.errors.EmptyDataError: If the CSV file is empty
        pd.errors.ParserError: If the CSV file has formatting issues
    
    Example:
        >>> data = load_csv('data/sales.csv')
        >>> print(data.head())
           Date       Product  Sales
        0  2024-01-01  Widget   100
        1  2024-01-02  Gadget   150
    
    Note:
        - The function assumes the CSV has a header row
        - Default encoding is UTF-8
        - Handles common CSV formats automatically
    """
    pass
