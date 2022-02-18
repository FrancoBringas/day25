# # with open("weather_data.csv") as weather:
# #     data = weather.readlines()
# #
# #     print(data)
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temp = int(row[1])
# #             temperatures.append(temp)
# #     print(temperatures)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data["temp"].to_list()
#
# # print(temp_list)
# # list_sum = sum(temp_list)
# # list_len = len(temp_list)
# # average = list_sum / list_len
# # print(f"temperature average {average}")
# # print(max(temp_list))
# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])
# Monday = data[data.day == "Monday"]
# print((Monday.temp * 1.8) + 32)
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(Black_squirrel_count)
print(Grey_squirrel_count)
print(Cinnamon_squirrel_count)
data_dict ={
    "fur color": ["Gray","Cinnamon","Black"],
    "Count": [Grey_squirrel_count,Cinnamon_squirrel_count,Black_squirrel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
