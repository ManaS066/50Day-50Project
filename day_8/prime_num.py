def prime(num):
    if (num==0):
        print('Neither prime or composite')
    else:
        flag=0
        p=int(num/4)
        for i in range(2,p):
            if(num%i==0):
               flag=0
            else:
                flag=1
    if(flag==1):
        print("prime num")
    else:
         print(f'The number {num} is not a prime number')           

num=int(input("enter num"))
prime(num)