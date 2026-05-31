# Import a module to freeze the program for a specifc period of time if needed
import time

# Define a loading function to make the code cleaner
def loading(seconds):
  if not skip_loading:
    time.sleep(seconds)

# By toggling this to true the program will skip all the fake loading
skip_loading = False

# Welcome screen
print("Welcome")
loading(1)

while True:

  # Operation type selection
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

  # First number selection
  while True:
      try:
          first_number = float(input("Enter the first number for your calculation: "))
          break
      except ValueError:
          print("Invalid number. Please enter a valid number.")

  print(f"Current calculation: {first_number} {operation} _")

  # Second number selection
  while True:
      try:
          second_number = float(input("Enter the second number for your calculation: "))
          break
      except ValueError:
          print("Invalid number. Please enter a valid number.")

  print(f"Current calculation: {first_number} {operation} {second_number}")
  print("Calculating...")
  loading(0.5)

  # Do the calculation and print the result
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

  
  # Gives the option to perform another calculation without restarting the whole program
  while True:
    another_calculation = input("Do you want to perform another calculation? (yes, no): ").lower()
    if another_calculation == "yes" or another_calculation == "y":
      break
    elif another_calculation == "no" or another_calculation == "n":
      print("Bye!")
      break
    else:
      print("Please enter yes or no!")
      continue
  if not another_calculation == "yes" and not another_calculation == "y":
    break
  

# Made by Michail
