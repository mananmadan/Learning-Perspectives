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

def calc_score(bstring,normalizing_val):
    # calculate the score from the binary string and give out the normalized score
    count =0;
    ans = 0;
    for i in bstring:
     if i == '0':
         count = count+1
     elif i == '1':
         ans = ans + pow(2,count)
         count = count +1
    ans = ans + 0.01
    val = ans/pow(2,normalizing_val)
    print(val)
    return val

def encode(mainfile,evalfile,normalizing_val):
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
    val = calc_score(bstring,normalizing_val)
    return val
