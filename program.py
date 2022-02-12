#program.py
sum = 2 + 1;
print (sum)

#Variables
sum = 2 + 1
product = sum * 2
print (product)

#Data types
distancia_a_Toluca = 3.3639
type(distancia_a_Toluca)

#Operators with Variables
left_side = 35
right_side = 28
result_mult= left_side * right_side
result_divide = left_side / right_side
result_sum = left_side + right_side
result_substract = left_side - right_side
print ("The result for the multiplication is: ", result_mult)
print ("The result for the multiplication is: ", result_divide)
print ("The result for the multiplication is: ", result_sum)
print ("The result for the multiplication is: ", result_substract)
print ("The multiple results are: ", result_mult, ", ", result_divide, ", ", result_sum, ",", result_substract)

#Use datetime functions

#Import library
from datetime import date, datetime
#Obtain date time via function
date.today()
#Show datetime via console
print(datetime.today())
print("The datetime today is: " + str (datetime.today()))
print("The datetime today is: ", datetime.today())