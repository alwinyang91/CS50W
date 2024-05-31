def square(x):
    return x * x


for i in range(10):
    print(f"{i} squared is {square(i)}")

for i in range(10):
    print("{} squared is {}".format(i, square(i)))
