def write_score(param_a,param_b,file_r):
 openfile = open(file_r,'w')
 openfile.write(str(param_a) + ' ' + str(param_b))
 openfile.write('\n')
