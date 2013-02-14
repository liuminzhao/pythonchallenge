# level 4
num = "8022"
p = re.compile('the next nothing is [0-9]+')
p2 = re.compile('[0-9]+')
for i in range(1000):
    url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    req = urllib2.Request(url+num)
    response = urllib2.urlopen(req)
    newnum = response.read()
    tmp = p.search(newnum).group()
    num = p2.search(tmp).group()
    print newnum
