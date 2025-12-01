age = int(input())
accident_count = int(input())
discount_amount = 0

if age < 25 :
    base_premium = 2400
elif age <= 50 :
    base_premium = 1800
elif age > 50 :
    base_premium = 2000

if accident_count == 0 :
    discount_amount = 10/100 * base_premium
    final_premium = base_premium - discount_amount
elif accident_count <= 2 :
    final_premium = base_premium + 300
elif accident_count >= 3 :
    final_premium = base_premium + 600


print (int(base_premium))
print (int(final_premium))
print (int(discount_amount))