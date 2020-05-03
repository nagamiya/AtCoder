# input
n = int(input())
sum = 0

# judge
for i in range(n+1):
    if ((i % 3 != 0) and (i % 5 != 0)):
        sum += i

# output
print(sum)
