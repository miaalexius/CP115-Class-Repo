for number in range(1,101) : 
    print(f'Checking: {number}')
    if number % 7 == 0 and number % 13 == 0:
        break  # Stop searching

found_number = number
print(found_number)
