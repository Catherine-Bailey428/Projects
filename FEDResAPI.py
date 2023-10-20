import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fredapi import Fred
import plotly.express as px
import os
from dotenv import load_dotenv
load_dotenv('.env')
fred = Fred(api_key= os.getenv('fred_key'))
print(fred.get_series(series_id='UNRATE',observation_start='2020-08-01',observation_end='2023-08-01'))
unemploy = fred.get_series(series_id='UNRATE',observation_start='2022-08-01',observation_end='2023-08-01')
unemploy.plot()
plt.title('unemployment')
plt.show()
inflation = fred.get_series(series_id='CPILFESL',observation_start='2022-08-01',observation_end='2023-08-01')
print(inflation)