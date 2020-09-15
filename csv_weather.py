import csv
from matplotlib import pyplot as plt
from datetime import datetime
import numpy as np


filename='./sitka_weather_2018_full.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            # strptime(),接收各种实参数，根据它们来决定如何解读日期
            current_data = datetime.strptime(row[2], "%Y-%m-%d")
            high=int(row[8])
            low=int(row[9])
        except ValueError:
            print(current_data,'missing data')
        else:
            dates.append(current_data)
            highs.append(int(row[8]))
            lows.append(int(row[9]))



fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.title('daily high temperture,July 2018',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()          #绘制倾斜的日期标签，防止彼此重叠
plt.ylabel('temperture(F)',fontsize=16)
y=np.arange(0,80,5)
plt.yticks(y)
# plt.tick_params(axis='both',which='major',labelsize=5)
plt.show()