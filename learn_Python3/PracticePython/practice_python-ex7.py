""""
Exercise 7
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""

#Could not do in one line so did 6
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

for i in a:
    if i % 2 == 0:
        b.append(i)

print(b)
""""
Below is the list comprehension method as seen at the following url
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

I just get the modulo operation results which will be just 0s and 1s
"""

#fist example. Tho the lambda part is wrong
c = list(map(lambda x: x % 2,a))
print(c)

#second example
d = [x % 2 for x in a]
print(d)
