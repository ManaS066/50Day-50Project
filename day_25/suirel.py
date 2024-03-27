import pandas as pd

data = pd.read_csv("day_25\sqirle_count.txt")
# grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
# red_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
# black_squirrel = data[data["Primary Fur Color"] == "Black"]
# # print the length of the diffrent color squirrel
# l_r = len(red_squirrel)
# l_b = len(black_squirrel)
# l_g = len(grey_squirrel)


# print(l_g)
# print(l_r)
# print(l_b)


# data_dict = {
#     "Fur Color": ["Grey","Cinnamon","Black"],
#     "Count" : [l_g,l_r,l_b]
# }
# df = pd.DataFrame(data_dict)
# df.to_csv("sqirle_count.txt")
print(data)
