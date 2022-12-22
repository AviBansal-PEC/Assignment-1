a=int(input("Enter your Gross Income (to nearest penny):"))
b=int(input("Enter the number of dependents:"))
c=a-10000-(b*3000)
t=c*0.2
print("Your Total Tax:",t)