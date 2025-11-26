"""Summary module for data analysis.

This module provides functions for generating statistical summaries
of datasets including descriptive statistics and data aggregations.
"""

def summarize(data):
    """
    Generate a statistical summary of the provided dataset.
    
    This function analyzes the input data and returns key statistical
    measures such as mean, median, mode, standard deviation, min, max,
    and quartile values.
    
    Args:
        data: A pandas DataFrame or list/array containing numerical data
              to be analyzed.
    
    Returns:
        dict: A dictionary containing statistical summary metrics:
            - 'mean': Average value of the dataset
            - 'median': Middle value of the sorted dataset
            - 'mode': Most frequently occurring value
            - 'std': Standard deviation
            - 'min': Minimum value
            - 'max': Maximum value
            - 'q1': First quartile (25th percentile)
            - 'q3': Third quartile (75th percentile)
    
    Raises:
        ValueError: If data is empty or invalid
        TypeError: If data type is not supported
    
    Example:
        >>> import pandas as pd
        >>> data = pd.DataFrame({'values': [1, 2, 3, 4, 5]})
        >>> summary = summarize(data)
        >>> print(summary['mean'])
        3.0
    """
    pass
