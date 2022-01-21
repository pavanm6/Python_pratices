#WAP to accept salary and 3 shopping bills from user and find
#1.total shoping amount 
#2.find how much % of amount he spent on shoping on his salary.


sal = int(input("Enter salary"))
b1 = int(input("Enter first shopping bill"))
b2 = int(input("Enter second shopping bill"))
b3 = int(input("Enter third shopping bills"))



total=b1+b2+b3

per=(total/sal)*100
print("percentage of amount spent :",per)

