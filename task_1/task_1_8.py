x_n = -9
x_k = 7
dx = 0.5


print("+------+------+")
print("|  x   |   y  |")
print("+------+------+")

x = x_n

while x <= x_k:
    if x < -7:
        y = 0
    elif x < -3:
        y = x + 7
    elif x < -2:
        y = 4
    elif x <= 2:
        y = x ** 2
    elif x <= 4:
        y = -2 * x + 8
    else:
        y = 0

    print(f"|{x:5.2f} |{y:5.2f} |")
    x += dx

print("+------+------+")
