# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))

#     print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# # print(data_dict)
# # temp_list = data["temp"].to_list()
# # print(data["temp"].max())
# # print(data[data.temp == max(data.temp)])
# # monday = data[data.day == "Monday"]
# # print(monday.temp*1.8 + 32)

# new_dict = {
#     "Students" : ["Yusuf", "Tuğba", "Kerem"],
#     "Scores" : [75, 80, 95] 
# }

# data = pandas.DataFrame(new_dict)
# data.to_csv("newFrame.csv")

# data = pandas.read_csv("weather_data.csv")
# new_data = data[data.day == "Tuesday"]
# print(new_data["day"].count())

data = pandas.read_csv("Central_park.csv")

gray_sq_count = len(data[data["Fur Color"] == "Gray"])
red_sq_count = len(data[data["Fur Color"] == "Cinnamon"])
black_sq_count = len(data[data["Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color" : ["Gray", "Red", "Black"],
    "Count" : [gray_sq_count, red_sq_count, black_sq_count]
}

result = pandas.DataFrame(squirrel_dict)
result.to_csv("squirrel_count.csv")


    