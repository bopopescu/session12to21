def fun():
    file = open("session15.txt", "r")
    lines = file.readlines()
    for line in lines:
        yield line

# A function which yields, upon execution creates a Generator Object
result = fun()
print(result)


print(next(result))
print(next(result))