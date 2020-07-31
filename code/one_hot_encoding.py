nouns = set()
def load_dict(mainfile):
    #get the nouns from the main file and store in dict
    openfile = open(mainfile,'r')
    readtext = openfile.read()
    a = ""
    for i in readtext:
        if i!=',':
         a = a+i
        else:
         nouns.add(a)
         a = ""
    #for i in nouns:
    #    print(i,":",nouns[i])



def calc_score(bstring,normalizing_val):
    # calculate the score from the binary string and give out the normalized score
    count =0
    ans = 0
    flag = 0
    for i in bstring:
     if i == '0' :
         count = count+1
     elif i == '1':
         ans = ans + pow(2,count)
         count = count +1
    ans = ans +0.01
    val = ans/pow(10,normalizing_val)
    print(val)
    return val

def encode(mainfile,evalfile,normalizing_val):
    # encoding in binary strings
    bstring = "" 
    count = 0
    load_dict(mainfile)
    for i in nouns:
          print(i)
          if i in open(evalfile).read():
             bstring = bstring + '1'
             count = count + 1
             print(i)
          else:
             bstring = bstring + '0'
    
    print(bstring)
    print(count)
    nouns.clear()
    val = calc_score(bstring,normalizing_val)
    return count,val
