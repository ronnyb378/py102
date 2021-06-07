#number list
numbers = [23, 234, 234, 3421]

#find smallest 
smallest = numbers[0]
for num in numbers:
    if num < smallest : 
        smallest = num

print(smallest)