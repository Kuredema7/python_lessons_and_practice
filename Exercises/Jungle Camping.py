
n = 'Grr Rawr Ssss Chirp'
a = ['Lion', 'Tiger', 'Snake', 'Bird' ]
st = input().split()
msg = ''

for i in range(len(st)):
    msg += a[n.split().index(st[i])] + ' '
print (msg)

#print (a.index(0))
