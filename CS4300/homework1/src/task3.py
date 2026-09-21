number = -7

if number > 0:
    num_result = "Pos"
elif number < 0:
    num_result = "Neg"
else:
    num_result = "Zero"

print(number, "is", num_result)

prime_numbers = []

for num in range(2, 30):
    is_prime = True

    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    
    if is_prime:
        prime_numbers.append(num)

    if len(prime_numbers) == 10:
        break

print("First 10 prime num: ", prime_numbers)

total = 0
current_num = 1

while current_num <= 100:
    total += current_num
    current_num += 1

print("Sum of number 1 through 100: ", total)
    