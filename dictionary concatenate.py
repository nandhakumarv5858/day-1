a={1:10, 2:20}
b={3:30, 4:40}
c={5:50,6:60}
d = {}
for e in (a, b, c): d.update(e)
print(d)
