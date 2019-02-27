# set operation
a={1,2,3,4,5}
b={4,5,6,7,8,9}
# union
c=a-b
d=b-a
print(c)
print(d)
e=a|b
print(e)
# intersection
f = a & b
print(f)
g = set.symmetric_difference(a,b)
print(g)

#frozen set
frozen_set = frozenset(['w','e'])
print(frozen_set)