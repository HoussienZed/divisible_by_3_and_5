# asking user to enter a number x

x = int(input("Enter an integer: "))

# checking what numbers from 1 to x divisible by 3 and 5

for i in range(1, x + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} is divisible by 3 and 5")
else:
    print(f"There are no integers between 1 and {x} divisible by 3 and 5")
