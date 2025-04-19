
import numpy as np
import pandas as pd
import ast

def missing_value_summary(df):
    """
    Returns a summary of missing values for each column in the DataFrame.

    Parameters:
    - df: pd.DataFrame

    Returns:
    - pd.DataFrame with:
        - Number of missing values per column
        - Percentage of missing values relative to total rows
    """
    miss_per_col = df.isnull().sum()
    missing_val_percent = np.round(100 * miss_per_col / len(df), 2)

    missing = pd.concat([miss_per_col, missing_val_percent], axis=1)
    missing.columns = ['Number of Missing Values', 'Percent of Total Values']
    missing = missing.sort_values('Percent of Total Values', ascending=False)

    return missing

def create_dim_and_bridge(games_df, column_name, dim_name):
    """
    Extracts a dimension and bridge table from a list-type column in the games dataframe.

    Parameters:
    - games_df: pd.DataFrame with at least 'gameid' and a column with lists (e.g., developers)
    - column_name: the name of the column in games_df containing lists
    - dim_name: the name to use for the dimension entity (e.g., 'developer', 'publisher')

    Returns:
    - dim_table: a dimension table with unique entity names and IDs
    - bridge_table: a bridge table with gameid and entity_id pairs
    """
    # Parse stringified lists if needed
    if games_df[column_name].apply(type).eq(str).any():
        games_df[column_name] = games_df[column_name].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

    # Explode to long format
    exploded = games_df[['gameid', column_name]].explode(column_name).dropna().copy()
    exploded.rename(columns={column_name: f'{dim_name}_name'}, inplace=True)

    # Create dimension table
    dim_table = exploded[[f'{dim_name}_name']].drop_duplicates().reset_index(drop=True).copy()
    dim_table[f'{dim_name}_id'] = dim_table.index + 1
    dim_table = dim_table[[f'{dim_name}_id', f'{dim_name}_name']]

    # Create bridge table
    bridge_table = exploded.merge(dim_table, on=f'{dim_name}_name', how='left')
    bridge_table = bridge_table[['gameid', f'{dim_name}_id']].drop_duplicates().reset_index(drop=True)

    return dim_table, bridge_table


def generate_date_dim(date_series, date_col_name="Date"):
    """
    Generates a standard date dimension from a given datetime series.

    Parameters:
    - date_series: a pd.Series of datetime objects (e.g. df['posted'])
    - date_col_name: name of the output column representing the date (default: 'Date')

    Returns:
    - date_dim: a DataFrame with standard date attributes
    """
    # Coerce to datetime and drop NaT
    clean_series = pd.to_datetime(date_series, errors='coerce').dropna()

    # Build date range
    full_range = pd.date_range(start=clean_series.min(), end=clean_series.max())

    # Create dimension table
    date_dim = pd.DataFrame({date_col_name: full_range})
    date_dim['date_id'] = date_dim[date_col_name].dt.strftime('%Y%m%d').astype(int)
    date_dim['Year'] = date_dim[date_col_name].dt.year
    date_dim['Month'] = date_dim[date_col_name].dt.strftime('%b')
    date_dim['MonthNumber'] = date_dim[date_col_name].dt.month
    date_dim['YearMonth'] = date_dim[date_col_name].dt.strftime('%Y-%m')

    # Final column order
    date_dim = date_dim[['date_id', date_col_name, 'Year', 'Month', 'MonthNumber', 'YearMonth']]

    return date_dim
