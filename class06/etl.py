import pandas as pd
import os
import glob

def extract_data(folder: str) -> pd.DataFrame:
    """Extracts data from all JSON files in the specified folder into a single DataFrame.

    Args:
        folder (str): The path to the folder containing JSON files.

    Returns:
        pd.DataFrame: A DataFrame containing the combined data from all JSON files.
    """
    json_files = glob.glob(os.path.join(folder, '*.json'))
    df_list = [pd.read_json(file) for file in json_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

def calculate_total_sales_kpi(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates the total sales KPI for each row in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame with sales data, including 'Quantidade' and 'Venda' columns.

    Returns:
        pd.DataFrame: The same DataFrame with an additional 'Total' column representing the total sales (Quantidade * Sale).
    """
    df["Total"] = df['Quantidade'] * df['Venda']
    return df

def save_data(df: pd.DataFrame, output_formats: list):
    """Saves the DataFrame in the specified formats.

    Args:
        df (pd.DataFrame): The DataFrame to be saved.
        output_formats (list): A list of formats in which to save the DataFrame ('csv', 'parquet').
    """
    print(output_formats)
    for format in output_formats:
        if format == 'csv':
            df.to_csv('data.csv', index=False)
        elif format == 'parquet':
            df.to_parquet('data.parquet', index=False)

def sales_kpi_pipeline(path: str, output_formats: list):
    """The pipeline function for calculating and saving the total sales KPI.

    Args:
        path (str): The path to the folder containing the JSON files to be processed.
        output_formats (list): The formats in which to save the processed data.
    """
    data_frame = extract_data(path)
    kpi_data_frame = calculate_total_sales_kpi(data_frame)
    save_data(kpi_data_frame, output_formats)
