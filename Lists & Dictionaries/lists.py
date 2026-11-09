lst = ["Virat Kohli", "Yuvraj Singh", "Shane Warne", "Varun Chakravarthy", "Ravindra Jadeja", "MS Dhoni", "Rohit Sharma", "Suresh Raina", "Hardik Pandya", "Bhuvneshwar Kumar", "Jasprit Bumrah"]

print("Length of the list is: ", len(lst))
print("First element of the list is: ", lst[0])
print("Last element of the list is: ", lst[-1])

lst.append("Kapil Dev")
lst.append("Sachin Tendulkar")
print("List after appending elements: ", lst)

lst.remove("Shane Warne")
print("List after removing an element: ", lst)

lst.sort()
print("List after sorting: ", lst)

lst.pop(9)
print("List after popping an element: ", lst)

lst.reverse()
print("List after reversing: ", lst)

print("Multiplication of list: ", lst * 2)

lst = lst[:4]
print("Sliced list: ", lst)

lst.clear()
print("List after clearing: ", lst)

lst1 = ["Virat Kohli", "Yuvraj Singh", "Shane Warne", "Varun Chakravarthy", "Ravindra Jadeja", "MS Dhoni", "Rohit Sharma", "Suresh Raina", "Hardik Pandya", "Bhuvneshwar Kumar", "Jasprit Bumrah"]
lst2 = ["Kapil Dev", "Sachin Tendulkar"]
lst3 = lst1 + lst2
print("Concatenated list: ", lst3)
