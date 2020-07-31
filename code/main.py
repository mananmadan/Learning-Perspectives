from filter import filter_files
from extract_kw import extract_keywords
from one_hot_encoding import encode
from write import write_score
from count import count_keywords
main_file = '/home/manan/Desktop/Research/Learning-Perspectives/data/data_notes/79'
eval_file = '/home/manan/Desktop/Research/Learning-Perspectives/data/data_notes/'


val =0
temp =0

for i in range(0,93):

# Filter the files

#filter_files(main_file + str(i) + '.txt')
#filter_files(eval_file + '.txt')

# generate nouns

#noun_file_main = main_file + str(i) + 'n' + '.txt'
#noun_eval_file = eval_file + 'n' + '.txt'

## keywords extracted from the main file will normalize all the values
#normalizing_val = extract_keywords(main_file+str(i)+'.txt',noun_file_main)
#print(normalizing_val)
#if normalizing_val>val:
#           val = normalizing_val
#           temp = i
#           print(normalizing_val)

#print(val,temp)

## keywords extracted from the eval file will be stored for clustering 
#count_eval = extract_keywords(eval_file+'.txt',noun_eval_file)

# one hot encoding
 encode(main_file+'n'+'.txt' ,eval_file+str(i)+'.txt',0)
 #print(x,main_score)
# store the results in a file to be used by clustering
# value to be store is main_score and count_eval
 #results_file = '/home/manan/Desktop/Research/Learning-Perspectives/results/scores.txt'
 #found = count_keywords(eval_file + str(i)+'n'+'.txt')
 #write_score(x,main_score,found,results_file)
