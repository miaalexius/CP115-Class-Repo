monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

<<<<<<< HEAD
max_loan_amount = 5 * monthly_income

=======
# Determine max loan amount (5x income)
max_loan_amount = monthly_income * 5

# Determine interest rate based on credit score
>>>>>>> 52b7dc842d8af1f3331bbf40309986588d6f1f08
if credit_score >= 700:
    interest_rate = 3.5
elif credit_score >= 600:
    interest_rate = 5.5
else:
<<<<<<< HEAD
    interest_rate = 0 

approval_status = "Rejected"

if monthly_income >= 4000 and credit_score >= 600 and loan_amount <= max_loan_amount:
    approval_status = "Approved"
=======
    interest_rate = 0.0

# Check approval criteria
if monthly_income >= 4000 and credit_score >= 600 and loan_amount <= max_loan_amount:
    approval_status = "Approved"
else:
    approval_status = "Rejected"
    interest_rate = 0.0  # No interest for rejected loans
>>>>>>> 52b7dc842d8af1f3331bbf40309986588d6f1f08

print(interest_rate)
print(max_loan_amount)
print(approval_status)