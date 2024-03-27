# with open ("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)



# import csv
# with open("weather_data.csv")as data:
#     all_data=csv.reader(data)
#     temp=[]
#
#     for row in all_data:
#         if row[1]!="temp":
#              temp.append(int(row[1]))
#     print(temp)
#


import pandas as pd
data= pd.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
#
#
# data_dict = data.to_dict()
# print(data_dict)
#
# t_list=data["temp"].to_list()
# avg = sum(int(data_dict))/len(data_dict)
# print(avg)

# data in serial
# print(data["temp"].mean())
# print(data["temp"].max())


#acces data in colomn  // column

#print(data['condition'])

# another aproch
#print(data.condition)


#get data from the row

# print(data[data.day == 'Monday'])
#
# print(data[data.temp==data.temp.max()])

#
# monday=data[data.day =="Monday"]
# monday_temp = monday.temp[0]
# tf=monday_temp*9/5+32
# print(tf)