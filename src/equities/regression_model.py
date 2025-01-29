# regression_model.py
# Regression models for stock price prediction). This script implements a simple linear regression model to predict stock prices.

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def predict_stock_price(data, target_column='price'):
    """
    Predict stock prices using a linear regression model.

    Args:
    data (pd.DataFrame): DataFrame containing stock prices and features.
    target_column (str): The column name to predict (usually 'price').

    Returns:
    tuple: Model and predictions
    """
    # Prepare features (X) and target (y)
    X = data.drop(target_column, axis=1)  # Features (all columns except target)
    y = data[target_column]  # Target (stock price)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model's performance (MSE)
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

    return model, predictions

# Example usage:
# model, predictions = predict_stock_price(stock_data)
