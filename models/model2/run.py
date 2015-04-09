import os
import sys
cxxnet = sys.argv[1]
# softmax
TEMPLATE_SOFTMAX = ""
TEMPLATE_TEST = ""
TEMPLATE_TRAIN = ""

fi = file("./pred.template")
for line in fi:
    TEMPLATE_SOFTMAX += line

SZ = [65, 70, 75]
xx = 0
yy = 0
FLIP = [0, 1]


for sz in SZ:
    while xx <= 30:
        yy = 0
        while yy <= 30:
            for flp in FLIP:
                if xx + sz > 80:
                    continue
                if yy + sz > 80:
                    continue
                raw_path = "pred/%d-%d-%d-%d" % (xx, yy, flp, sz)
                sub_path = "sub/sm_%d-%d-%d-%d.csv" % (xx, yy, flp, sz)
                if os.path.exists(sub_path) == True:
                    print "Skip: %s" % sub_path
                    continue
                smx = TEMPLATE_SOFTMAX.replace("%PRED_PATH%", raw_path)
                smx = smx.replace("%CROP_X%", str(xx))
                smx = smx.replace("%CROP_Y%", str(yy))
                smx = smx.replace("%FLIP%", str(flp))
                smx = smx.replace("%SZ%", str(sz))
                fo = open("temp", "w")
                fo.write(smx)
                fo.close()
                cmd = cxxnet + " " + "temp"
                os.system(cmd)
                cmd = "pypy ../etc/make_softmax_submission.py ../data/sampleSubmission.csv ../data/test.lst %s %s" % (raw_path, sub_path)
                os.system(cmd)
                os.remove(raw_path)
            yy += 2
            if sz == 65:
                yy += 2
        xx += 2
        if sz == 65:
            xx += 2
    xx = 0


