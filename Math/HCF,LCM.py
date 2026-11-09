numberLargest = (int(input("Enter the largest number: ")))
numberSmallest = (int(input("Enter the smallest number: ")))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print(f"The HCF of the given numbers is: {numberLargest}")