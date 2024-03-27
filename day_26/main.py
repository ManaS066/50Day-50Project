## list comprihason

# new_list =[n+1 for n in list]
# print(new_list)
# [11, 31, 24]
# name = "Manas"
# new_name =[letter for letter in name]
# print(new_name)
# ['M', 'a', 'n', 'a', 's']
# tup =(10,20,39)
# Tup_list =[n*2 for n in tup]
# print(Tup_list)
# [20, 40, 78]

# list=[ n*2 for n in range(1,5)]
# print(list)
# [2, 4, 6, 8]
# list=[ n*2 for n in range(1,5)]
# print(list)
# [2, 4, 6, 8]
# name=["manas" , "Angela", "alex" , "amirut"]
# print(name)
# ['manas', 'Angela', 'Alex Star', 'amirut']
# short_name = [n for n in name if len(n)<5]
# print(short_name)
# []
# short_name = [n for n in name if len(n)<6]
# print(short_name)
# ['manas']
# long_name = [ n.upper() for n in name if len(n)>6]
# print(long_name)
# ['ALEX STAR']

# list_of_string = input().split(",")
#
# num=[int(n) for n in list_of_string]
# even= [n for n in num if n%2==0]
# print(even)

# dictionary Comprehension


# In [3]: name = ["manas","ranjan","lopamudera","ipsita"]
# In [4]: import random
# In [5]: result ={student : random.randint(1,100) for student in name}
# In [6]: passed_student ={student:mark for (student,mark) in result}
# passed_student ={student:mark for (student,mark) in result.items() if mark>60}
# In [8]: print(passed_student)
# {'manas': 77, 'lopamudera': 94}


# count  total character in word in a sentence
# sentence = input()
# # ? Don't change code above ?
# # Write your code below ?
#
#
# count ={ n :len(n) for n in sentence.split() }
# print(count)


# convert temp deg to celcious
# weather_c = eval(input())
# weather_f={ key : (value*9/5)+32 for (key,value) in weather_c.items()}
# print(weather_f)


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#     password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#     password_list += random.choice(numbers)

password_list += [random.choice(symbols) for n in range(nr_symbols)]
password_list += [random.choice(letters) for n in range(nr_letters)]
password_list += [random.choice(numbers) for n in range(nr_numbers)]
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
