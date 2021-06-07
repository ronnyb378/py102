#number list
numbers = [23, 234, 234, 3421]

#find largest
largest = numbers[0]
for num in numbers:
    if num > largest : 
        largest = num

print(largest)