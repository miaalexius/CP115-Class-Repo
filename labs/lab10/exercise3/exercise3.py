monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

max_loan_amount = 5 * monthly_income

if credit_score >= 700:
    interest_rate = 3.5
elif credit_score >= 600:
    interest_rate = 5.5
else:
    interest_rate = 0 

approval_status = "Rejected"

if monthly_income >= 4000 and credit_score >= 600 and loan_amount <= max_loan_amount:
    approval_status = "Approved"

print(interest_rate)
print(max_loan_amount)
print(approval_status)