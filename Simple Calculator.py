import time


print("Welcome")
time.sleep(1)



is_operation_correct = False
while is_operation_correct == False:
  operation = input("What operation do you want to perform? (+, -, /, *): ").lower().strip()

  if operation == "plus" or operation == "+":
      operation = "+"
      is_operation_correct = True
  elif operation == "minus" or operation == "-":
      operation = "-"
      is_operation_correct = True
  elif operation == "divide" or operation == "/":
      operation = "/"
      is_operation_correct = True
  elif operation == "multiply" or operation == "*":
      operation = "*"
      is_operation_correct = True
  else:
      print("Invalid operation. Please enter one of the following types: +, -, /, *")
      continue

  print(f"Current calculation: _ {operation} _")



first_number = float(input("Enter the first number for your calculation: ")).strip()
print(f"Current calculation: {first_number} {operation} _")

second_number = float(input("Enter the second number for your calculation: ")).strip()
print(f"Current calculation: {first_number} {operation} {second_number}")

print("Calculating...")
time.sleep(0.5)


if operation == "+":
    print(f"Here is the result: {first_number + second_number}")
elif operation == "-":
    print(f"Here is the result: {first_number - second_number}")
elif operation == "/":
    print(f"Here is the result: {first_number / second_number}")
elif operation == "*":
    print(f"Here is the result: {first_number * second_number}")
else:
    print("A critical error accured, exiting...")


# Made by Michail

