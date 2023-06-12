import csv
import pandas

with open("weather_data.csv") as file:
    data = csv.reader(file)

    temperature = []
    for item in data:
        if item[1].isdigit():
            temperature.append(int(item[1]))

    print(temperature)

data1 = pandas.read_csv("weather_data.csv")
print(data1['temp'])
data_in_dict = data1.to_dict()
print(data_in_dict)
data_in_list = data1['temp'].to_list()
print(data_in_list)
average = sum(data_in_list) / len(data_in_list)
print(average)
use_lib = data1['temp'].mean()
print(use_lib)

max_val = data1['temp'].max()
print(max_val)

# Gey data in a row
print(data1[data1.day == "Monday"])

print(data1[data1.temp == data1.temp.max()])

monday = data1[data1.day == "Monday"]
print(monday.condition)
print(monday.temp * 9 / 5 + 32)

data_dict = {"students": ["anna", "oleg", "stephan"],
             "scores": [74, 89, 88]}
another_data = pandas.DataFrame(data_dict)
print(another_data)
another_data.to_csv("another_csv.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_black = len(data[data["Primary Fur Color"] == "Black"])
fur_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
fur_grey = len(data[data["Primary Fur Color"] == "Grey"])

new_data = {"Fur color": ["Black", "Cinnamon", "Grey"],
           "count": [fur_black, fur_cinnamon, fur_grey]}
new_csv = pandas.DataFrame(new_data)
new_csv.to_csv("for_lesson.csv")
print(fur_black)




