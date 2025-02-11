class calculator:
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divided(self,x,y):
        return x/y
calc = Calculator()
print("selcet the operation:")
print("\n1.add")
print("\n2.subtract")
print("\n3.multiply")
print("\n4.divided")

operations=int(input("choose theoperation:"))
num1=float(input("enter the first number:"))
num2=float(input("enter the second number"))
if operations==1:
    print(f"{num1}+{num2}={calc.add(num1,num2)}")
elif operations==2:
    print(f"{num1}-{num2}={calc.subtract(num1,num2)}")
elif operations==3:
    print(f"{num1}*{num2}={calc.multiply(num1,num2)}")
elif operations==4:
    print(f"{num1}/{num2}={calc.divided(num1,num2)}")
else:
    print("invalid operations")
calculator()
    

    




