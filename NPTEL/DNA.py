num = int(input())
i=1
s=0
while i<num:
    if num%i==0:
        s=s+i
    i+=1
print(s)
if s==num:

  print("perfect")