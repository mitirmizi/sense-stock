
# import nasdaqdatalink
import pandas as pd
import yfinance as yf
from datetime import datetime
from os import mkdir
from os.path import exists, join

MAIN_DIR = "/home/teemo/MEGA/bdma-semesters/2-semester/sense-stock"

todays_date_str = datetime.now().strftime("%Y-%m-%d")

# Check if "stock" folder exists
if not exists( join(MAIN_DIR, "stock") ):
    mkdir( join(MAIN_DIR, "stock") )

if not exists( join(MAIN_DIR, "stock", "ohlc") ):
    mkdir(join(MAIN_DIR, "stock", "ohlc"))

if not exists( join(MAIN_DIR, "stock", "ohlc", todays_date_str)):
    mkdir(join(MAIN_DIR, "stock", "ohlc", todays_date_str))

# Where all the files will be saved
file_dir = join(MAIN_DIR, "stock", "ohlc", todays_date_str)

start = datetime(2022, 3, 26, 14)
end = datetime(2022, 3, 28, 15, 30)


list_companies = [
    "ATVI",
    "ADBE",
    "GOOGL",
]

print(f'\nDatetime: {datetime.now()}' )
for company in list_companies:
    print(f" -- For {company} -- ")

    if exists( join(file_dir, f"{todays_date_str}_{company}_stocks.csv")):
        df_old_data = pd.read_csv(join(file_dir, f"{todays_date_str}_{company}_stocks.csv"))
    else:
        df_old_data = pd.DataFrame()

    print(f"Length of df_old_data: {len(df_old_data)}")

    # Fetch the actual data
    df_data = yf.download(tickers=company, period="1h", interval="1m")

    print(f"Start Datetime: {df_data.index[0]}")
    print(f"Start Datetime: {df_data.index[-1]}")

    df_data = pd.concat( (df_old_data, df_data) )

    df_data.to_csv(join(file_dir, f"{todays_date_str}_{company}_stocks.csv"))

    print(f"Rows: {len(df_data)}")
    print(f" === Done  === \n")


# ---------  code library
# command get data for "ADBE"
# data = yf.download(tickers="ADBE", period="1d", interval="1m")

########################################
# for testing
########################################

# Test case where data overlaps in the dfs
# start = datetime(2022, 3, 29, 14)
# end = datetime(2022, 3, 29, 15)
#
# df1 = yf.download(tickers="ADBE", period='2h', interval="1m")
# df2 = yf.download(tickers="ADBE", period='1h', interval="1m")


# date_str = datetime.now().strftime("%Y-%m-%d")

# print(data)

# data.to_csv(f"/home/teemo/MEGA/bdma-semesters/2-semester/sense-stock/{date_str}_ATVI_stocks.csv")
