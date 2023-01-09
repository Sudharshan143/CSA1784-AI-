def add(n1,n2):
    return(n1+n2)
def sub(n1,n2):
    return(n1-n2)
def mul(n1,n2):
    return(n1*n2)
def div(n1,n2):
    return(n1%n2)
print("Please select operation -\n" 
        "1. Add\n" 
        "2. Subtract\n" 
        "3. Multiply\n" 
        "4. Divide\n")  
select = int(input("Select operations form 1,2,3,4 :")) 
number_1 = int(input("Enter number1: "))
number_2 = int(input("Enter number2: "))
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2)) 
elif select == 2:
    print(number_1, "-", number_2, "=",
                    sub(number_1, number_2)) 
elif select == 3:
    print(number_1, "*", number_2, "=",
                    mul(number_1, number_2)) 
elif select == 4:
    print(number_1, "/", number_2, "=",
                    div(number_1, number_2))
else:
    print("Invalid input")
