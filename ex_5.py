from functools import reduce
a = int(input())
b = int(input())
c = int(input())



lst = [x for x in range(a, b+1)]

p = list(filter(lambda x: x%c == 0 and (x**0.5).is_integer(), lst))

print(lst)
print(p)

pr = reduce(lambda x, y: x*y, p)
print(pr)
