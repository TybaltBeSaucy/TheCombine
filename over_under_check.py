import pandas as pd

def calculate_over_under(home_team, your_single_number, csv_path='Home_OU.csv'):
    result_home = pd.read_csv(csv_path, index_col='team_home')

    result_home.columns = pd.IntervalIndex.from_arrays(
        left=result_home.columns.str.extract(r'(\d+)', expand=False).astype(float),
        right=result_home.columns.str.extract(r',\s*(\d+)', expand=False).astype(float),
        closed='left'
    )

    over_under_range_for_single_number = result_home.columns[result_home.columns.contains(your_single_number)]

    if not over_under_range_for_single_number.empty:
        try:
            column_name = over_under_range_for_single_number[0]
            percent = result_home.loc[home_team, column_name]
            return f'Percentage for {home_team} with {your_single_number} in the range {column_name}: {percent:.2f}%'
        except KeyError:
            return f'No data found for {home_team} with {your_single_number} in the calculated range.'
    else:
        return f'No range found for {your_single_number}.'
