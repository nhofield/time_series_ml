import pandas as pd

def load_and_preprocess(filename: str, missing_vals: str = None) -> pd.DataFrame:
    """
    Load the dataset and preprocess it.

    Args:
        filename (str): Path to the dataset file.
        missing_vals (str): Strategy for handling missing values ('ffill', 'mean', or None).

    Returns:
        pd.DataFrame: Preprocessed dataset.
    """
    # Load the dataset
    df = pd.read_csv(filename, parse_dates=["Time"], index_col="Time")
    
    # Handle missing values
    if missing_vals == 'ffill':
        df.fillna(method='ffill', inplace=True)
    elif missing_vals == 'mean':
        df.fillna(df.mean(), inplace=True)
    
    # Create lagged features
    df["Pressure_lag1"] = df["Pressure"].shift(1)
    
    # Create rolling statistics
    df["FlowRate_rolling3"] = df["FlowRate"].rolling(window=3).mean()
    
    # Drop rows with NaN (from lagging/rolling)
    df.dropna(inplace=True)

    return df
