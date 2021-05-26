import numpy as np
import pandas as pd


def setup_dfs():
    frut_data = pd.read_csv("./Data/frut_raw.csv")
    iff_data = pd.read_csv("./Data/iff_raw.csv")
    frut_data.columns = iff_data.columns.copy()
    col_to_choose = ['Date', 'Price', 'Vol.']
    frut_data = frut_data[col_to_choose]
    iff_data = iff_data[col_to_choose]
    iff_data['Date'] = pd.to_datetime(iff_data['Date'])
    frut_data['Date'] = pd.to_datetime(frut_data['Date'],format='%d.%m.%Y')

    frut_data = frut_data.set_index('Date')
    iff_data = iff_data.set_index('Date')

    frut_data = frut_data.sort_index(ascending=False)
    iff_data = iff_data.sort_index(ascending=False)

    iff_data['Price'] = pd.to_numeric(iff_data['Price'].astype(str).str.replace(",", ""))
    frut_data['Price'] = pd.to_numeric(frut_data['Price'].astype(str).str.replace(",", ""))

    frut_data["LOG Return"] = np.log(frut_data[['Price']].resample('D').ffill().pct_change() + 1)
    iff_data["LOG Return"] = np.log(iff_data[['Price']].resample('D').ffill().pct_change() + 1)
    frut_data["Return"] = frut_data[['Price']].resample('D').ffill().pct_change()
    iff_data["Return"] = iff_data[['Price']].resample('D').ffill().pct_change()
    return iff_data, frut_data


def main():
    iff_data, frut_data = setup_dfs()
    iff_data.to_csv("./Data/iff_processed_data.csv")
    frut_data.to_csv("./Data/frut_processed_data.csv")


if __name__ == '__main__':
    main()
