# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
print("select option:")
print("1.add")
print("2.sub")
print("3.multiply")
while True:
     choice=input("enter the choice(1/2/3):")
     if choice in('1','2','3'):
         num1=float(input("enter the first number: "))
         num2=float(input("enter the second number: "))
         if choice=='1':
             print(num1,"+",num2,"=",add(num1,num2))
         elif choice=='2':
             print(num1,"-",num2,"=",sub(num1,num2))
         elif choice=='3':
             print(num1,"*",num2,"=",multiply(num1,num2))
         next_calculation=input("lets do next calculation?(yes/no):")
         if next_calculation=="no":
             break
         else:
             print("invalid input")






