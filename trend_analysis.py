import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
import pymannkendall as mk
from typing import List, Dict, Union

# Constants
MINIMUM_DATA_POINTS = 6

# Correct Sampling Intervals
def correct_sampling_intervals(file_path: str, sampling_period: str = "6M", t_number: Union[str, List[str]] = "All", gas: Union[str, List[str]] = "All", download: bool = False) -> pd.DataFrame:
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")

    data['Date'] = pd.to_datetime(data['Date'], format="%d/%m/%Y")
    data['ref'] = pd.to_numeric(data['ref'], errors='coerce')

    if t_number == "All":
        tx_list = data['T.Number'].unique()
    else:
        tx_list = [t_number] if isinstance(t_number, str) else t_number

    if gas == "All":
        gases = ['Hydrogen', 'Methane', 'Ethane', 'Ethylene', 'Acetylene', 'Carbon.dioxide', 'Carbon.monoxide']
    else:
        gases = [gas] if isinstance(gas, str) else gas

    for g in gases:
        data[g] = pd.to_numeric(data[g], errors='coerce')

    output = []

    for tx in tx_list:
        tx_data = data[data['T.Number'] == tx].sort_values(by='Date')
        tx_data.set_index('Date', inplace=True)

        resampled_data = tx_data.resample(sampling_period).median()
        resampled_data['T.Number'] = tx

        output.append(resampled_data.reset_index())

    result = pd.concat(output, ignore_index=True)

    if download:
        result.to_csv(f"{sampling_period}_ProcessedData.csv", index=False)

    return result

# Advanced Trend Analysis (not shared with recruiters)
def advanced_trend_analysis(data: pd.DataFrame, gas: str, ref_col: str = 'ref') -> List[Dict]:
    """
    Custom algorithm incorporating domain-specific knowledge and physics for trend analysis.

    Parameters:
    - data (pd.DataFrame): The input data.
    - gas (str): The name of the gas column to analyze.
    - ref_col (str): The name of the reference column.

    Returns:
    - List[Dict]: A list of dictionaries containing analysis results.
    """
    results = []

    for idx, row in data.iterrows():
        # Example placeholder for custom trend logic
        result = {
            'Index': idx,
            'Gas': gas,
            'Ref': row[ref_col],
            'AnalysisResult': None  # Replace with actual logic
        }
        results.append(result)

    return results

# Find Trends
def find_trends(data: pd.DataFrame, t_number: Union[str, List[str]] = "All", gas: Union[str, List[str]] = "All", historic: bool = True, latest_only: bool = False) -> pd.DataFrame:
    if t_number == "All":
        tx_list = data['T.Number'].unique()
    else:
        tx_list = [t_number] if isinstance(t_number, str) else t_number

    if gas == "All":
        gases = ['Hydrogen', 'Methane', 'Ethane', 'Ethylene', 'Acetylene', 'Carbon.dioxide', 'Carbon.monoxide']
    else:
        gases = [gas] if isinstance(gas, str) else gas

    trends = []

    for tx in tx_list:
        tx_data = data[data['T.Number'] == tx]

        for g in gases:
            gas_data = tx_data[['Date', 'ref', g]].dropna()
            if len(gas_data) > MINIMUM_DATA_POINTS:
                trend_result = advanced_trend_analysis(gas_data, gas=g)
                trend = {
                    'T.Number': tx,
                    'Gas': g,
                    'Trend': trend_result,  # Placeholder for detailed trend result
                    'Confidence': None  # Define based on your logic
                }
                trends.append(trend)

    trends_df = pd.DataFrame(trends)
    trends_df.to_csv("Trends.csv", index=False)
    return trends_df

# Find Outliers
def find_outliers(data: pd.DataFrame, gas_thresholds: Dict[str, float], t_number: Union[str, List[str]] = "All", gas: Union[str, List[str]] = "All") -> pd.DataFrame:
    if t_number == "All":
        tx_list = data['T.Number'].unique()
    else:
        tx_list = [t_number] if isinstance(t_number, str) else t_number

    if gas == "All":
        gases = ['Hydrogen', 'Methane', 'Ethane', 'Ethylene', 'Acetylene', 'Carbon.dioxide', 'Carbon.monoxide']
    else:
        gases = [gas] if isinstance(gas, str) else gas

    outliers = []

    for tx in tx_list:
        tx_data = data[data['T.Number'] == tx]

        for g in gases:
            gas_data = tx_data[['Date', 'ref', g]].dropna()
            if g in gas_thresholds:
                threshold = gas_thresholds[g]
                outliers_data = gas_data[gas_data[g] > threshold]
                outliers_data['Gas'] = g
                outliers.append(outliers_data)

    outliers_df = pd.concat(outliers, ignore_index=True)
    outliers_df.to_csv("Outliers.csv", index=False)
    return outliers_df

# Plot Trends
def plot_trends(data: pd.DataFrame, gas: Union[str, List[str]] = "All", t_number: Union[str, List[str]] = "All", gas_thresholds: Dict[str, float] = None, figsize: tuple = (10, 6)) -> None:
    if t_number == "All":
        tx_list = data['T.Number'].unique()
    else:
        tx_list = [t_number] if isinstance(t_number, str) else t_number

    if gas == "All":
        gases = ['Hydrogen', 'Methane', 'Ethane', 'Ethylene', 'Acetylene', 'Carbon.dioxide', 'Carbon.monoxide']
    else:
        gases = [gas] if isinstance(gas, str) else gas

    for tx in tx_list:
        tx_data = data[data['T.Number'] == tx]

        for g in gases:
            gas_data = tx_data[['Date', 'ref', g]].dropna()
            if len(gas_data) > MINIMUM_DATA_POINTS:
                plt.figure(figsize=figsize)
                plt.plot(gas_data['Date'], gas_data[g], marker='o', label=f"{g} Levels")
                plt.xlabel("Date")
                plt.ylabel(f"{g} [ppm]")
                plt.title(f"{tx} - {g} Trend")

                if gas_thresholds and g in gas_thresholds:
                    plt.axhline(y=gas_thresholds[g], color='red', linestyle='--', label="Threshold")

                plt.legend()
                plt.show()