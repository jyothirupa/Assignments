# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:38:26 2018

@author: user
"""

import pandas as pd

animals = [150, 400, 225, 175, 50]
series = pd.Series(animals, index = ["Beast Animals", "Other land animals", "Birds", "Water animals", "Reptiles"], name='series')
series.plot.pie(figsize=(6, 6), autopct = "%.2f%%") #percentage of animals