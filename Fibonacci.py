def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index - 2) + fibonacci(index - 1)


count = int(input("Please enter the index of Fibonacci "))
print("Index {0} of Fibonacci is {1}".format(count, fibonacci(count)))
