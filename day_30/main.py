# exception hendelining useing python
#
# try
# something that can cause error
# except
# Do if the code give exception
# else:
# if exceptiojn is not occure then what to do
# finally:
# exit from try

# try:
#     file = open("a_file.txt")
#
#     # adict = {"key": "value"}
#     # print((adict("sadd")))
# except FileNotFoundError:
#     # it will automatically create a file
#     file = open("a_file.txt", "w")
#     file.write("hello")
# except TypeError:
#     print("a")
# except TypeError as error_message:
#     print(error_message)
#
# else:
#     # if there is no error in the try block then the else block going to exicute
#     letter = file.read()
#     print(letter)
#
# finally:
#     raise KeyError("this message is showing error")

height = float(input("Height: "))
weight = float(input("Weight: "))


if height>3:
    raise ValueError("human height should not above 3 meter")
bmi = weight/height**2
print(bmi)

