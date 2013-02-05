__author__='liuminzhao'

f = open('equality.txt', 'r')

a = f.read()

for i in range(3, len(a) - 3):
    if a[i].islower():
        left = a[(i-3):i]
        right = a[(i+1):(i+4)]
        if all([one.istitle() for one in left]) and all([one.istitle() for one in right]):
            if a[i-4].islower() and a[i+4].islower():
                print a[(i-3):(i+4)]

f.close()

# linkedlist.php
