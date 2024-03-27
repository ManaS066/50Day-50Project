fruits = eval(input())


# ? Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    if index > 2:
        raise IndexError
    else:
        fruit = fruits[index]
        print(fruit + " pie")


# ? Do not change the code below
make_pie(4)
