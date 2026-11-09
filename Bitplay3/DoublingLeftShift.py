input("Left shift doubles. Right shift halves. Press Enter to continue...")
print(" 3 >> 1 =", 3 >> 1, " 12 << 1 =", 12 << 1)
print(" 3 >> 2 =", 3 >> 2, " 12 << 2 =", 12 << 2)

n = int(input("Enter a number to double and halve (Try 5/8): "))
guess = input(" What is " + str(n) + " >> 2? ")
input(" Left shift by 2 multiplies by 4. Right shift by 2 divides by 4. Press Enter to continue...")
print(" n >> 2 =", n >> 2, "your guess:", guess)

if n >> 2 == int(guess):
    print(" Correct!")
elif n >> 2 > int(guess):
    print(" Too low!")
else:
    print(" Too high!")