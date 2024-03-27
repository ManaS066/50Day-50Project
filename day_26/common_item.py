with open("file1.txt", "w") as num1:
    n1 = [int(n) for n in num1]
with open("file2.txt", "w") as num2:
    n2 = [int(n) for n in num2]
common = [n for n in n1 if n == n in n2]
print(common)
