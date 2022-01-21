#Wap to check a given number prime or not

num=int(input("Enter n values:"))
count=0
for i in range(1,(num//2)+1):
  if num%i ==0:
    count=count+1
if count>1:
  print("Prime")
else:
  print("Not prime")
