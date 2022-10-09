import csv
from datetime import datetime

infile =open('death_valley_2018_simple.csv','r')
csvfile =csv.reader(infile,delimiter=',')  # breaks into a list


header_row = next(csvfile)

#print(header_row)

#to know the index location of the specific element we are lookiing for
for index,column_header in enumerate(header_row):
    print(index,column_header)
highs =[]
dates = []
lows = []


for record in csvfile:
    #
    try:
         thedate =datetime.strptime(record[2],'%Y-%m-%d')
         high =int(record[4])
         low = int(record[5])

    except ValueError:
        print(f"Missing data for {thedate}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)

# print(highs)
# print(lows)
# print(dates)



import matplotlib.pyplot as plt
fig = plt.figure()  

#1st - xaxis which is dates

plt.plot(dates,highs,c="red")
plt.plot(dates,lows,c="blue")

#fill between with shade  alpha - transparency 10%
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.title("Daily High temperature- 2018\nDeath Valley",fontsize=16)
plt.xlabel("July 2018",fontsize=16)
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis="both",which ="major",labelsize=16)

#just for dates to format it into readable format or else its will be collapsed
fig.autofmt_xdate()


plt.show()



#value error , value may be missing




