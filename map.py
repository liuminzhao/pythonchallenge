text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

text = "map"

newtext = [ord(one) + 2 for one in text]

new = ''
for i in newtext:
    if i == 123:
        i = 97
    elif i == 124:
        i = 98
    new += chr(i)

print new


