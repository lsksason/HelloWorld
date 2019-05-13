# _*_ coding:UTF-8 _*_

import keyword
import random

print("BMI計算")
# h = 1.65
# w = 65
h, w = 1.65, 65

# del w
print(w / pow(h, 2))

num2 = 5 + True  # 6

string1 = "1.65"
# val1 = int(string1)
val2 = float(string1)

print(w, h, sep="\t", end="")

print("random " + str(random.randint(40, 80)))
# print("random " + str(random.random(40, 80, 2)))

print("h={0}, w={1:03d}, BMI={2:.4f}".format(h, w, w / pow(h, 2)))

print(keyword.kwlist)
