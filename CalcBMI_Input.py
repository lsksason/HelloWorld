

def calc(bmi):
    if 18<=bmi<23:
        return "good"
    elif bmi < 18:
        return "thin"
    else:
        return "fat"

def getBmi(h, w):
    hvalue = float(h)
    wvalue = float(w)
    result = wvalue / hvalue ** 2
    return result, calc(result)


h = input("請輸入身高(m) ")
w = input("請輸入體重(kg) ")

bmi, result = getBmi(h, w)

print("BMI={0:.2f}, msg={1}".format(bmi, result))
msg = "good" if 18 <= bmi < 23 else "bad"

calc(bmi)

print(msg)




