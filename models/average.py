import csv
import sys
import copy

fa = csv.reader(file(sys.argv[1]))
fb = csv.reader(file(sys.argv[2]))
fc = csv.reader(file(sys.argv[3]))
fd = csv.reader(file(sys.argv[4]))
fe = csv.reader(file(sys.argv[5]))
ff = csv.reader(file(sys.argv[6]))
fo = csv.writer(open(sys.argv[7], "w"), lineterminator='\n')

head = fa.next()
fb.next()
fc.next()
fd.next()
fe.next()
ff.next()
fo.writerow(head)


da = {}
db = {}
dc = {}
dd = {}
de = {}
df = {}

for line in fa:
    key = line[0]
    line = line[1:]
    value = [float(x) for x in line]
    da[key] = value

for line in fb:
    key = line[0]
    line = line[1:]
    value = [float(x) for x in line]
    db[key] = value

for line in fc:
    key = line[0]
    line = line[1:]
    value = [float(x) for x in line]
    dc[key] = value

for line in fd:
    key = line[0]
    line = line[1:]
    value = [float(x) for x in line]
    dd[key] = value

for line in fe:
    key = line[0]
    line = line[1:]
    value = [float(x) for x in line]
    de[key] = value

for line in ff:
    key = line[0]
    line = line[1:]
    value = [float(x) for x in line]
    df[key] = value




keys = da.keys()
keys = sorted(keys)
for key in keys:
    line = [key]
    a = da[key]
    b = db[key]
    c = dc[key]
    d = dd[key]
    e = de[key]
    f = df[key]
    h = []
    s = 1.0 / 6
    for i in xrange(len(a)):
        h.append((a[i] + b[i] + c[i] + d[i] + e[i] + f[i]) * s)
    line.extend(h)
    fo.writerow(line)



