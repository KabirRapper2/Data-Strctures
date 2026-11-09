number = int(input("Enter a number: "))

origanail_number = number
reverse_number = 0

while number > 0:
    digit = number % 10
    reverse_number = (reverse_number * 10) + digit
    number = number // 10

if origanail_number == reverse_number:
    print(f"{origanail_number} is a palindrome number") 
else:
    print(f"{origanail_number} is not a palindrome number")