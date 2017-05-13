"""
This script is used to analyze unemployment data from 1948 to 2017
data from Federal Reserve bank of St. Louis website. https://fred.stlouisfed.org/series/UNRATE
Usage:
python simple_viz_un_rate.py
"""

__author__ = 'Tamby Kaghdo'

import pandas as pd
import sys
import matplotlib.pyplot as plt


def main():
    try:
        unrate_df = pd.read_csv("data/UNRATE.csv")

        # convert column 'DATE' from string to date
        unrate_df["DATE"] = pd.to_datetime(unrate_df["DATE"])
        print(unrate_df.head())

        # simple plot by year

        plt.xlabel("Year")
        plt.ylabel("Unemployment Rate")
        plt.title("Yearly Unemployment 1948-2017")
        plt.plot(unrate_df["DATE"], unrate_df["UNRATE"])
        plt.show()


        monthly_df = unrate_df[unrate_df["DATE"] >= "2016-01-01"]
        # simple plot by month from Jan 2016 to Apr 2017
        plt.plot(monthly_df["DATE"], monthly_df["UNRATE"])
        plt.xticks(rotation=90)
        plt.title("Monthly Unemployment Rate From Jan 2016 to Apr 2017")
        plt.xlabel("Month")
        plt.ylabel("Unemployment Rate")
        plt.show()

    except IOError as e:
        print(e)
        sys.exit(e.errno)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
