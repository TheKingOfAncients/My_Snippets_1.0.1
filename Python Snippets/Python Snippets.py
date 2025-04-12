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


========================================================================================================


#Snippts from Youtuber 2mpythondev (Link to video https://youtube.com/shorts/xk0A_4qMtVU?si=gOo10ctwkFV568Ir)

#Mainly just ways to decrease line count.
========================================================================================================
#List Comprenhension 1

squares = []
for x in range(10):
     squares.append(x**2)

#Shorter version:

squares = [x*2 for x in range(10)]

========================================================================================================

temp = x
x = y 
y = temp



#Shorter version:

x, y = y, x 

========================================================================================================

 my_list = [1, 2, 3]

 for item in my_list:
     print(item)

#Shorter version:

[print(item) for item in my_list]

========================================================================================================

 my_list = [1, 2, 3]
 a = my_list[0]
 b = my_list[1]
 c = my_list[2]

#Shorter version:

a, b, c = [1, 2, 3]

========================================================================================================

reversed_string =''
for char in my_string:
     reversed_string = char + reversed_string

#Shorter version:

reversed_string = my_string[::-1]

========================================================================================================





