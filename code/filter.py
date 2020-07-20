data  = ""
whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ \n')
with open('notes.txt') as f:
    for i in f:
        i = i.lower()
        data = data + ''.join(filter(whitelist.__contains__,i))

with open ('notes.txt','w') as f:
    f.write(data)