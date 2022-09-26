import csv
from datetime import datetime

infile =open('sitka_weather_2018_simple.csv','r')
csvfile =csv .reader(infile,delimiter=',')  # breaks into a list

header_row = next(csvfile)

#print(header_row)

#to know the index location of the specific element we are lookiing for
for index,column_header in enumerate(header_row):
    print(index,column_header)
highs =[]
dates = []
lows = []


for record in csvfile:

    highs.append(int(record[5]))
    lows.append(int(record[6]))
    thedate =datetime.strptime(record[2],'%Y-%m-%d')
    dates.append(thedate)
print(highs)
print(lows)
print(dates)



import matplotlib.pyplot as plt
fig = plt.figure()  

#1st - xaxis which is dates

plt.plot(dates,highs,c="red")
plt.plot(dates,lows,c="blue")

#fill between with shade  alpha - transparency 10%
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.title("Daily High temperature- 2018",fontsize=16)
plt.xlabel("July 2018",fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",which ="major",labelsize=16)

#just for dates to format it into readable format or else its will be collapsed
fig.autofmt_xdate()


#plt.show()

#2 rows , 1 column , which column are u wrking on - index value on chart we are working on
plt.subplot(2,1,1)
plt.plot(dates,highs,c="red")
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows,c="blue")
plt.title("Lows")

plt.suptitle("Highs and lows of Sitka,Alaska")
plt.show()




