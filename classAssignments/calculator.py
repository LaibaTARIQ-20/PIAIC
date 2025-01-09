#Assignment 3 calculator
num1 = float(input("enter first number "))#taking inputs from user first step
num2 = float(input("enter second number here "))
#now we will perform operations 

addition = num1+num2
#results using .format method
print("the sum of {} and {} is {}." .format(num1, num2, addition))
subtraction = num1-num2

#using string concatenation
print("The difference of " + str(num1) + " and " + str(num2) + " is " + str(subtraction) + ".")

#simple print 
multiplication = num1*num2
print("The product of", num1, "and", num2, "is", multiplication, ".")

division = num1/num2
print("The quotient of", num1, "and", num2, "is", division, ".")
#fstring method
modulus = num1 % num2
print(f"The modulus of {num1} and {num2} is {modulus}.")

exponentiation = num1 ** num2
print(f"the exponentiation of {num1} and {num2} is {exponentiation}.")

floor_division = num1 // num2
print (f"the answer of floor division of {num1} and {num2} is {floor_division}")