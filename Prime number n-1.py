#print list of prime number n-1

count=0
n= int(input("Enter n value :"))
for  i in range(1,n+1):
    for j in range (1,(i//2)+1):
        if i%j==0:
            count=count+1
    if count>1:
        print(i,end=" ")
    count=0    