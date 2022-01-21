#WAP to print Fibnnoic series
num1=0
num2=1
sum=0
for i in range(10):
    sum=num1+num2
    print(sum,end=" ")
    num1=num2
    num2=sum

