import random


iValue = 0
print("While")
iValue = random.randint(1, 9)
print(iValue)
while iValue % 2 == 0:
    iValue = random.randint(1, 9)
    print(iValue)
    if iValue % 2 == 0:
        break
else:  # 只有在loop條件不滿足時才會進來，如果中途被break是不會進來的
    print("while else")

print("Do While")
while True:
    iValue = random.randint(1, 9)
    if iValue % 2 == 0:
        print(iValue)
    else:
        break;

if None:
    print("None")

for i in range(0, 5):
    print(i)
    # if i > 2:
    #     break
else:  # 只有在loop條件不滿足時才會進來，如果中途被break是不會進來的
    print("loop else")


