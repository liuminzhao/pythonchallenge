__author__ = 'liuminzhao'

f = open('ocr.txt', 'r')

for one in  f.read():
    tmp = ord(one)

    if tmp >= 97 and tmp <= 122 :
        print one
    if tmp >= 65 and tmp <= 90:
        print one

f.close()
