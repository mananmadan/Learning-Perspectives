def write_score(param_a,param_b,param_c,file_r):
 openfile = open(file_r,'a')
 openfile.write(str(param_a) + ' ' + str(param_b)+' '+str(param_c))
 openfile.write('\n')
