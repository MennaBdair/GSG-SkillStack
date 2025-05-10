# the function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Let the user input a range of numbers
begin = int(input("Enter the starting number of range: "))
end = int(input("Enter the ending number of range: "))

with open("prime.txt", "w") as file:
    for num in range(begin, end + 1):
        # Use a function to check if a number is prime.
        if is_prime(num):
            file.write(str(num) + "\n")

print("Prime numbers written to 'prime.txt'.")
