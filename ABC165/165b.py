import math

x = int(input())
task = 100
count = 0

while task < x:
    task = math.floor(task * 1.01)
    #print(task)
    count += 1

print(count)
