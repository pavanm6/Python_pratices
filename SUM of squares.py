#find the sum of squares of first n natural numbers.


N = int(input("Enter value of N natural numbers: "))
temp = 0
for i in range(1, N+1):
    temp += (i*i)
print("Sum of squares = ", temp)





#N = int(input("Enter value of N natural numbers: "))
#total=((n*(n+1)*(2*n+1)/6))
#print("sum of the squares of",n,"number is :",total)