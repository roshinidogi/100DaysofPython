# with open("weather_data.csv") as file:
#     content = file.readlines()
# print(content)
from itertools import count

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
from pandas import DataFrame

# data = pandas.read_csv("weather_data.csv")

# average_temp = sum(data.temp) / len(data.temp)
# print(round(average_temp, 2))
#
# print(round(data.temp.mean(), 2))
# print(data.temp.max())
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 1.8 + 32
# print(monday_temp_f)

# data_dict = {
#     "students": ["Rosh", "Jaan", "Sravs"],
#     "scores": [90, 85, 70],
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
count_dict = {
   "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}
count_df = pandas.DataFrame(count_dict)
print(count_df)
count_df.to_csv("count_color.csv")