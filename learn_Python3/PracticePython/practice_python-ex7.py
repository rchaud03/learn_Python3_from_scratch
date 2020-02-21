#Could not do in one line so did 6
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

for i in a:
    if i % 2 == 0:
        b.append(i)

#print(b)

#c = list(map(lambda x: x % 2,a))
d = [x % 2 for x in a]
print(d)
