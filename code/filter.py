def filter_files(filename):
 data  = ""
 whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ \n')
 with open(filename) as f:
     for i in f:
         i = i.lower()
         data = data + ''.join(filter(whitelist.__contains__,i))

 with open (filename,'w') as f:
     f.write(data)
