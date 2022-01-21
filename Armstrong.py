#find a given number is armstrong number or not.
n=int(input("Enter number:",))
sum=0
temp=n
while(temp>0):
    d=temp%10
    sum=sum+d**3
    temp=temp//10
if(sum==n):
    print("given number is amstrong number")
else:
    print("given number is not amstrong number")