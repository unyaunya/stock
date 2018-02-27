# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Option(object):
    def __init__(self, strikingPrice):
        self.strikingPrice = strikingPrice

    def strikingPrice(self):
        """行使価格"""
        return 100

s = pd.Series([1,3,5,np.nan,6,8])
print(s)

dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

data = np.loadtxt("../data/n225-2014.csv", delimiter=",", dtype=int)
print(data)