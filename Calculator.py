def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q

print("Which operation would you like to do today?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice =  int(input("Please pick the operation that you want with the option's number:"))

num1 = int(input("Please enter the first number:"))
num2 = int(input("Please enter the second number"))

if choice == 1:
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == 2:
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice == 3:
    print(num1,"x",num2,"=",multiply(num1,num2))
elif choice == 4:
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid Input. Please try again")