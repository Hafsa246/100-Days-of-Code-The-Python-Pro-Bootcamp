# # Angela's Solution
# data1 = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels_count = len(data1[data1["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data1[data1["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data1[data1["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count1.csv")


grey_count = 0
red_count = 0
black_count = 0

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_list = data["Primary Fur Color"].to_list()

for color in color_list:
    if color == "Gray":
        grey_count += 1
    elif color == "Black":
        black_count += 1
    elif color == "Cinnamon":
        red_count += 1

color_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}

color_data = pandas.DataFrame(color_dict)
print(color_data)
color_data.to_csv("squirrel_count.csv")