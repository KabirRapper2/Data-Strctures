input(" XOR Swap. Exchange two values without a third variable. Press Enter to continue...")
print(" Before: a = 5, b = 9")

a, b = 5, 9
a ^= b; b ^= a; a ^= b
print(" After: a =", a, "b =", b)