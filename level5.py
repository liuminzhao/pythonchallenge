# peak.html
import pickle
f = open('banner.p', 'r')
test = pickle.load(f)
f.close()

for line in test:
    print "".join(map(lambda x: x[0]*x[1], line))
