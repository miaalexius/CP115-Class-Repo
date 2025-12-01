""" 
NAME : AZZA DAMIA BINTI KHAIRUL ZAMAN
PROBLEM DESC : Python program that asks the user to enter the
monthly usage and then calculates and displays the amount of the bill to be paid
after receiving the discount 
"""

monthly_usage = float(input( "Enter Usage : " ))
discount = 0

if monthly_usage < 50 : 
    discount = 0
elif monthly_usage <= 100 :
    discount = 0.05 * monthly_usage
elif monthly_usage > 100 : 
    discount = 0.2 * monthly_usage

total_bill = monthly_usage - discount 

print (total_bill)


