import time


print("""
 __          __  _                            _          _   _                      _            _       _             
 \ \        / / | |                          | |        | | | |                    | |          | |     | |            
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___    ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/ | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
      
""")
time.sleep(1)



is_operation_correct = False
while is_operation_correct == False:
  operation = input("What operation do you want to perform? (+, -, /, *): ").lower()

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



first_number = float(input("Enter the first number for your calculation: "))
print(f"Current calculation: {first_number} {operation} _")

second_number = float(input("Enter the second number for your calculation: "))
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

