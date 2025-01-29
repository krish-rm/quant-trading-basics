# data_processing.py
# Preprocessing for equity market data). This script preprocesses equity market data, handling missing values, and normalizing the data.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(file_path):
    """
    Preprocess the equity market data: clean, handle missing values, and normalize.

    Args:
    file_path (str): Path to the data file (CSV, Excel, etc.)

    Returns:
    pd.DataFrame: Preprocessed data
    """
    # Load data
    data = pd.read_csv(file_path)

    # Handle missing values by filling with the mean of each column
    data.fillna(data.mean(), inplace=True)

    # Normalize data using MinMaxScaler (scaling between 0 and 1)
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)
    scaled_df = pd.DataFrame(scaled_data, columns=data.columns)

    return scaled_df

# Example usage:
# preprocessed_data = preprocess_data('equity_data.csv')
