s = int(input("height: "))
while s < 0 or s > 8:
    s = int(input("height: "))
g = 1
d = s - 1
for i in range(s):
    while(g <= s):
        print(" " * d , end = '')
        print("#" * g)
        g += 1
        d -= 1
