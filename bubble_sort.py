import random

list = [random.randint(1,20) for i in range (10)]

#list.sort(reverse = True)
print(list)

n = len(list)

for i in range(n):
    for j in range(n-i-1):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]

print (list)