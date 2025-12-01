employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()
overtime_pay = overtime_hours * 35
epf = 0.11
sosco = 0.005


# TODO your code here
if tax_status == "Single" and base_salary >= 5000 :
    tax_rate = "22%"
    rate = 0.22
elif tax_status == "Single" and base_salary < 5000 :
    tax_rate = "18%"
    rate = 0.18
elif tax_status == "Married" and base_salary >= 6000 :
    tax_rate = "20%"
    rate = 0.2
elif tax_status == "Married" and base_salary < 6000 :
    tax_rate = "15%"
    rate = 0.15
elif tax_status == "Head" and base_salary >= 5500 :
    tax_rate = "25%"
    rate = 0.25
else :
    tax_rate = "19%"
    rate = 0.19

total_income = base_salary + overtime_pay
net_salary = total_income * (1 - rate) * (1- epf - sosco)
print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")