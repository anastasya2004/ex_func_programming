a = int(input())
b = int(input())

c = int(input())
d = int(input())


lst = [x for x in range(a, b+1)]

p = list(filter(lambda x: x%c != 0 and x%10 == d, lst))

#print(lst)
#print(p)
ct = 0
for i in p:
    ct += 1
print(ct)
