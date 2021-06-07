#multiply lists
#lists
l1= [2, 5, 10]
l2= [1, 15, -2]
combined = []
#multiply lists
for x in range(len(l1)):
    combined.append(l1[x] * l2[x])
#print
print(combined)