#print Alternate prime number

count=0
n= int(input("Enter n value :"))
for  i in range(1,n+1):
    for j in range (1,(i//2)+1):
        if i%j==0:
            count=count+1
    if count==1:
        a=a+1
        if a%2!=0:
            print(i,end=" ")
    count=0    
print("Number of prime no :",a)    