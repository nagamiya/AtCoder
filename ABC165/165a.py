import sys
# input
k = int(input())
a, b = map(int, input().split())
#print(f"k >>{k}, a >>{a}, b >>{b}")


for i in range(a, b+1):
    if (i % k == 0):
        print("OK")
        sys.exit(0)

print("NG")
