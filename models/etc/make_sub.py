import csv
import sys
import copy

fa = csv.reader(file(sys.argv[1]))
fo = csv.writer(open(sys.argv[4], "w"), lineterminator='\n')

fk = csv.reader(file(sys.argv[2])) #sampleSubmission.csv
head = fk.next()
fl = csv.reader(file(sys.argv[3]), delimiter='\t') #list
imgs = []
fo.writerow(head)
for line in fl:
    name = line[2].split('/')[-1]
    imgs.append(name)

for i in xrange(len(imgs)):
    a = fa.next()
    line = [imgs[i]]
    line.extend(a)
    fo.writerow(line)



