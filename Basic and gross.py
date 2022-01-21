#Wap to accept basic salary and find gross salary.
#gross_salary=basic+HRA+DA

#if basic salary <10000
#DA is 70% on basic 
#HRA is 65% on basic

# basic salary betwen 10000to 20000
#DA is 75% on basic 
#HRA is 73% on basic

# basic salary above 20000
#DA is 80% on basic 
#HRA is 76% on basic


basic=int(input("Enter Salary"))

if (basic<10000 and basic>0):
    da=(70/100)*basic
    hra=(65/100)*basic
    gross=basic+hra+da
    print("Gross salary is:",gross)
elif(basic>=10000 and basic<=20000):
    da=(75/100)*basic
    hra=(73/100)*basic
    gross=basic+hra+da
    print("Gross salary is:",gross)
else:
    da=(80/100)*basic
    hra=(76/100)*basic
    gross=basic+da+hra
    print("Gross salary is:",gross)