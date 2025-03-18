import yfinance as yf
import numpy as np
import pandas as pd

def reverse(arr):
    i = 0
    arr2 = []
    while i < len(arr)-1:
        if (arr[i] == np.nan):
            break
        else:
            arr2.append(arr[len(arr)-(1+i)])
        i += 1
    return arr2

class indicator():
    def __init__(self):
        self.data = []
    def __getitem__(self, index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value
    def __len__(self):
        return len(self.data)
    def append(self, value):
        self.data.append(value)
    def extend(self, values):
        self.data.extend(values)
    def insert(self, index, value):
        self.data.insert(index, value)
    def remove(self, value):
        self.data.remove(value) 
    def pop(self, index=-1):
        return self.data.pop(index)
    def prepend(self, app):
        if len(self.data) == 0:
            self.data.append(app)
        else:
            self.data = [app] + self.data

priceData = yf.download("SPY", start='2000-01-01')
SPYopen = reverse(reverse(pd.Series(priceData.Open.SPY)))
SPYhigh = reverse(reverse(pd.Series(priceData.High.SPY)))
SPYlow = reverse(reverse(pd.Series(priceData.Low.SPY)))
SPYclose = reverse(reverse(pd.Series(priceData.Close.SPY)))
