def check_num(number):
    #return if num is pos neg or 0
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

def first_ten_primes():
    #returns the first 10 primes
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

    return prime_numbers

def sum_one_to_one_hundred():
    #returns the sum of all numbers 1 to 100
    total = 0
    current_num = 1

    while current_num <= 100:
        total += current_num
        current_num += 1

    return total

number = int(input("Enter a Number: "))
print(number, "is", check_num(number))
print("First 10 prime numbers: ", first_ten_primes())
print("Sum of 1 to  100: ", sum_one_to_one_hundred())    