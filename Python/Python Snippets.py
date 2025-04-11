#Python Snippets

#Positive or Negative Number Script

#Script

#Prompt user for a number
number = float(input("Enter a number: "))

# Check if input is a valid number

if not math.isnan(number):
	# Check if the number is positive, negative, or zero.
     if number > 0:
          print(f"{number} is a positive number.")
     elif number < 0:
          print(f"{number} is a negative number.")
     else:
          print("The entered number is zero.")
else:    
     print("Please enter a valid number.")
