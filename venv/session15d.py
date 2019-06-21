def dataGenerator():
    file = open("session15.txt", "r")
    lines = file.readlines()
    for line in lines:
        yield line

# A function which yields, upon execution creates a Generator Object
dg = dataGenerator()
print(dg)


print(next(dg))
print(next(dg))