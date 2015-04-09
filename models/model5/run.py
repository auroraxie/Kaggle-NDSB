import os
import random
import csv
import sys

cxxnet = sys.argv[1]
SOFTMAX_TEMPLATE = ""
data = []
has_one = False
OUT = "raw_output"
N = 150

fi = file("./pred.template")
for line in fi:
    SOFTMAX_TEMPLATE += line

for i in xrange(N):
    name = "temp0"
    path = "pred/0"
    seed = str(i * 2019 + 5)
    dev = "gpu:0"
    smx = SOFTMAX_TEMPLATE.replace("%PRED%", path)
    smx = smx.replace("%GPU%", dev)
    smx = smx.replace("%SEED%", seed)
    fo = open(name, "w")
    fo.write(smx)
    fo.close()
    cmd = cxxnet + " " + name
    os.system(cmd)
    #os.system("../cxxnet/bin/cxxnet %s" % name)
    fi = csv.reader(file(path), delimiter=' ')
    idx = 0
    for line in fi:
        line = line[:-1]
        val = [float(x) for x in line]
        assert(len(val) == 121)
        if has_one == False:
            data.append(val)
        else:
            for j in xrange(len(val)):
                data[idx][j] += val[j]
        idx += 1
    if has_one == False:
        has_one = True

fo = csv.writer(open(OUT, "w"))
for line in data:
    val = [x / N for x in line]
    fo.writerow(val)



