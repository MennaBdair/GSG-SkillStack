
# Q1: Write a code to check if a year is a leap year.
x = int(input("Enter the number:"))
if ((x % 4 == 0 and x % 100 != 0) or x % 400 == 0):
    print("is Leap Year")
else:
    print("is not Leap Year")


# Q2: Write a loop that prints the multiplication of a given number (Up to 10).
m = int(input("Enter the number :"))
for n in range(11):
    print(n, "*", m, "=", n*m)
