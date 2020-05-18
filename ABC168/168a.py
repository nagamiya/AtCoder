n = int(input())
mod = n % 10
caseA = [3]
caseB = [0, 1, 6, 8]
if mod in caseA:
    print("bon")
elif mod in caseB:
    print("pon")
else:
    print("hon")
