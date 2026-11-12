input(" Power of Two Scanner. Left shift doubles: 1 << 1 is 2, 1 << 2 is 4, 1 << 3 is 8. Press Enter to continue...")
print(" 1 << 1 =", 1 << 1, " 1 << 2 =", 1 << 2, " 1 << 3 =", 1 << 3)
print(" 2 << 1 =", 2 << 1, " 4 << 1 =", 4 << 1, " 8 << 1 =", 8 << 1)

n = int(input("Enter a number to scan (Try 16/12): "))

input(" Right shift halves. Keep halving n until it is 1 or 0. Press Enter to continue...")
copy, shifts = n, 0
while copy > 1:
    copy >>= 1
    shifts += 1
print(" n >> 1 done", shifts, "times reaches", copy)

input(" If halving reaches 1, n is a power of 2. Press Enter to continue...")
print(" n is power of 2:", copy == 1)

input(" If the shift count is even, the power is a power of 4. Press Enter to continue...")
print(" n is power of 4:", copy == 1 and shifts % 2 == 0)

input(" If the shift count divides by 3, the power is a power of 8. Press Enter to continue...")
print(" n is power of 8:", copy == 1 and shifts % 3 == 0)

guess = input(" Guess how many shifts it took to reach 1 (0 if not a power of 2): ")
if shifts == int(guess):
    print(" Correct!")
elif shifts > int(guess):
    print(" Too low!")
else:
    print(" Too high!")

input(" Binary exponentiation. Halve the exponent with >> and double the base with *. Press Enter to continue...")
print(" 2^10 = 1024 because 10 in binary is", bin(10))

base = int(input("Enter a base (Try 3): "))
exp = int(input("Enter an exponent (Try 5): "))
result = 1
while exp > 0:
    if exp & 1:
        result *= base
    base *= base
    exp >>= 1
guess = input(" Guess the answer: ")
if result == int(guess):
    print(" Correct!")
elif result > int(guess):
    print(" Too low!")
else:
    print(" Too high!")

print(" The answer is", result)    