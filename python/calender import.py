'''import calendar
yy=int(input("enter a year"))
mm=int(input("enter a month"))
print(calendar.month(yy,mm))'''

import pandas as pd
date= pd.date_range('2023-02-01',period=1)
data= pd.series(date)
print(data.dt.daysinmonth)
