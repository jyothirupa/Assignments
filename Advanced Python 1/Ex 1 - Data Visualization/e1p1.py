# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:37:14 2018

@author: user
"""
import pandas as pd

vehicles = [140, 70, 55, 5]
series = pd.Series(vehicles, index = ["Cars", "Motorbikes", "Vans", "Buses"], name='series')
series.plot.pie(figsize=(6, 6), autopct = "%.2f%%")