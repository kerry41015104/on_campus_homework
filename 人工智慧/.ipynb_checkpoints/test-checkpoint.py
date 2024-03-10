# 下載台積電歷年股票價格
import requests
import pandas as pd
import io
import datetime
import time
import os
import sys
import json
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math


def get_stock_price(stock_no, start_date, end_date):
    url = (
        "https://query1.finance.yahoo.com/v7/finance/download/"
        + stock_no
        + ".TW?period1="
        + str(start_date)
        + "&period2="
        + str(end_date)
        + "&interval=1d&events=history&crumb=OQQi%5Cu002FQXu%5Cu002FQXq"
    )
    r = requests.get(url)
    df = pd.read_csv(io.StringIO(r.text))
    return df
