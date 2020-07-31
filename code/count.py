def count_keywords(filename):
    openfile = open(filename)
    readfile = openfile.read()
    ans = 0 
    for i in readfile:
        if i == ',':
            ans = ans+1

    return ans
