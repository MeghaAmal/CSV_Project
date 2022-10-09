import csv
from datetime import datetime

infile =open('sitka_weather_07-2018_simple.csv','r')
csvfile =csv .reader(infile,delimiter=',')  # breaks into a list

header_row = next(csvfile)

#print(header_row)

#to know the index location of the specific element we are lookiing for
for index,column_header in enumerate(header_row):
    print(index,column_header)
highs =[]
dates = []


for record in csvfile:
    highs.append(int(record[5]))
    thedate =datetime.strptime(record[2],'%Y-%m-%d')
    dates.append(thedate)
print(highs)
print(dates)



import matplotlib.pyplot as plt
fig = plt.figure()  

#1st - xaxis 

plt.plot(dates,highs,c="red")
plt.title("Daily high temperature,July 2018",fontsize=16)
plt.xlabel("July 2018",fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",which ="major",labelsize=16)

# for dates to format it
fig.autofmt_xdate()


plt.show()