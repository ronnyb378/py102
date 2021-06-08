#add matrixs vertically
#creating matrix 
m1 = [[2, 4],
[3, 4]]
m2 = [[3, 5],
[2, -2]]

#adding matrix vertically
for x in range(len(m1)):
    add = m1[x] + m2[x]
    for y in range(len(add)):
        print(add[y],end = '')
