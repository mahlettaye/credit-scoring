import pandas as pd
import numpy as np


def load_data(filepath):
    """Loads the dataset from the given file path."""
    try:
       # check if file is csv  use read_csv
        if filepath.endswith('.csv'):
            data = pd.read_csv(filepath)
            return data
        # Load the data using the openpyxl engine
        data = pd.read_excel(filepath, engine='openpyxl', header=None)

        # Split the single-column data into multiple columns
        data = data[0].str.split(',', expand=True)

        # Remove any lingering duplicate header rows
        data.columns = data.iloc[0]  # Assign the first row as headers
        data = data[1:]  # Drop the header row from data

        # Reset the index
        data.reset_index(drop=True, inplace=True)

        return data
    except Exception as e:
        raise FileNotFoundError(f"Error loading file: {e}")


def clean_data(data):
    """Cleans the dataset by handling missing values and formatting."""

    # Convert numeric columns to proper types if necessary
    numeric_columns = [
        "age", "savings_balance", "monthly_contribution",
        "payment_history_score", "loan_history", "mobile_money_volume",
        "years_in_sacco", "dependents"
    ]
    data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')
    # Replace common missing value placeholders with np.nan
    data.replace(["", "NA", "null", "NULL", "missing"], np.nan, inplace=True)

    return data
def handle_missing_values(df):
    """
    Handles missing values in the dataset with credit-scoring-specific justifications.
    """
    # Numeric columns: Fill with median or specific values
    numeric_columns = ["savings_balance", "monthly_contribution", "loan_history", 
                       "payment_history_score", "mobile_money_volume", "age", "dependents"]
    for column in numeric_columns:
        if column == "dependents":
            # Assume missing dependents mean 0
            df[column].fillna(0, inplace=True)
        else:
            df[column].fillna(df[column].median(), inplace=True)
    
    # Categorical columns: Fill with 'Unknown'
    categorical_columns = ["business_type", "location", "group_membership", "utility_payments"]
    for column in categorical_columns:
        df[column].fillna("Unknown", inplace=True)
    
    # Verify handling
    print("Remaining Missing Values:\n", df.isnull().sum())
    return df

def detect_outliers(df, columns):
    """
    Detects outliers using the IQR method for the given numeric columns.
    Returns a DataFrame with the count of outliers for each column.
    """
    outliers_info = {}
    for column in columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        outliers_info[column] = {
            "Lower Bound Outliers": (df[column] < (Q1 - 1.5 * IQR)).sum(),
            "Upper Bound Outliers": (df[column] > (Q3 + 1.5 * IQR)).sum()
        }
    return pd.DataFrame(outliers_info).T

def numeric_summary(df, numeric_columns):
    """
    Provides summary statistics for numeric columns.
    """
    return df[numeric_columns].describe()

def save_cleaned_data(data, output_path):
    """Saves the cleaned data to the specified output path."""
    data.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
