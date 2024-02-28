# Unlimited argument
# --------------------#

# def add(*args):
#     for n in args:
#         print(n)
#
# add(12,3,6,2,4,6,7,8)

# unlimited positional argument
# -----------------------------#
#
# def prin(*args):
#     print(args[0])
#     print(args[1])
# prin(3,4,3,2,5,5)


def calculate(n, **kwargs):
    print(kwargs)
    # for (key,value) in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=12, multiply=3)