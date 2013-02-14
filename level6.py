num = '90052'
import re
import zipfile
p = re.compile('[0-9]+')
file = zipfile.ZipFile("channel.zip", "r")
comments = []
for i in range(1000):
    filename = "channel/" + num + ".txt"
    f = open(filename, 'r')
    comments.append(file.getinfo(num+'.txt').comment)
    tmp =  f.readline()
    f.close()
    num = p.search(tmp).group()
    print tmp
print ''.join(comments)

    
