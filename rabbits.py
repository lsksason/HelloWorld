
total=83
legs = 240

def comput(total, legs) :
    leg2 = total * 2
    leaseLegs = legs - leg2
    rabbit = leaseLegs / 2
    chicken = total - rabbit
    return rabbit, chicken


r, b = comput(total, legs)

print("Rabbit={0}, Chicken={1}".format(r, b))
