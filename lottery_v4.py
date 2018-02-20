#Oleg Puchkov
import math
numbers_in_lottery =eval(input("Please enter the amount of numbers in the lottery "))
number_chosen=eval(input("Please enter the number chosen "))

while numbers_in_lottery <= 0 or number_chosen <= 0:
    print("Number must be positive")
    numbers_in_lottery =eval(input("Please enter the amount of numbers in the lottery "))
    number_chosen=eval(input("Please enter the number chosen "))

odds = math.factorial(numbers_in_lottery)/(math.factorial(number_chosen)*math.factorial(numbers_in_lottery - number_chosen))
print("Odds are",odds)

