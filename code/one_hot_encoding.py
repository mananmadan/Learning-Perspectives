nouns = {}
eval_list = []
def load_dict(mainfile):
    #get the nouns from the main file and store in dict
    openfile = open(mainfile,'r')
    readtext = openfile.read()
    a = ""
    for i in readtext:
        if i!=',':
         a = a+i
        else:
         nouns[a] = 1
         a = ""
    #for i in nouns:
    #    print(i,":",nouns[i])


def load_list(evalfile):
    # get the file to be evaluated and loads them into a list
    openfile = open(evalfile,'r')
    readtext = openfile.read()
    a = ""
    for i in readtext:
        if i!=',':
         a = a+i
        else:
         eval_list.append(a)
         a = ""
    #for i in eval_list:
    #    print(i)

def encode(mainfile,evalfile):
    # encoding in binary strings
    bstring = "" 
    load_list(evalfile)
    load_dict(mainfile)
    for i in nouns:
        if i in eval_list:
            bstring = bstring + '1'
        else:
            bstring = bstring + '0'
    print(bstring)

