import csv
infile =open('sitka_weather_07-2018_simple.csv','r')
csvfile =csv .reader(infile,delimiter=',')  # breaks into a list

next(csvfile)

for record in csvfile:
    print(record)
    print(record[0])
    print(record[1])
    input()
