a = int(input())
b = int(input())

c = int(input())
d = int(input())


lst = [x for x in range(a, b+1)]

p = list(filter(lambda x: x%c == 0 and x%d == 0, lst))

sm = 0
for i in p:
    sm += i
print(sm)
