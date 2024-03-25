def reg(x):
    return x.isupper()

i = int(input())
j = int(input())

st = 'CJInjGjOjVEWxxgc'
new_st = st[i-1: j+1]

print(st)
print(len(list(filter(reg, [x for x in new_st])))) #JInjG
