#create a list and add a new list made up of positive
#list 
list = [2, -234, -2 ,0 , 234, 31, 33]
#postive list
postive = []
#check for postive 
for pos in list:
    if pos >= 0: 
        postive.append(pos)

print(postive)