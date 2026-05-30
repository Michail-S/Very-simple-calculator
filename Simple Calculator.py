import time

print("Welcome")
time.sleep(1)


while True:
  operation = input("What operation do you want to perform? (+, -, /, *): ").lower().strip()

  if operation == "plus" or operation == "+":
      operation = "+"
      break
  elif operation == "minus" or operation == "-":
      operation = "-"
      break
  elif operation == "divide" or operation == "/":
      operation = "/"
      break
  elif operation == "multiply" or operation == "*":
      operation = "*"
      break
  else:
      print("Invalid operation. Please enter one of the following types: +, -, /, *")

print(f"Current calculation: _ {operation} _")


while True:
    try:
        first_number = float(input("Enter the first number for your calculation: "))
        break
    except ValueError:
        print("Invalid number. Please enter a valid number.")

print(f"Current calculation: {first_number} {operation} _")

while True:
    try:
        second_number = float(input("Enter the second number for your calculation: "))
        break
    except ValueError:
        print("Invalid number. Please enter a valid number.")

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

