# file=open("myfile.txt")
# c =file.read()
# print(c)
# file.close()


with open("myfile.txt" ,mode="w") as file :# this will open the file in write mode
     file.write("hello")

with open("myfile.txt", mode="a") as file: # this will open the file in append mode .
    file.write("\n hello")

with open("file.txt",mode="w") as file:
    file.write("This file was directly created useing the write mode")