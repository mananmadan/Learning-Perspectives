from filter import filter_files
from extract_kw import extract_keywords
from one_hot_encoding import encode
from write import write_score

main_file = '/home/manan/Desktop/Research/Learning-Perspectives/data/Ensemble_learning/1'
eval_file = '/home/manan/Desktop/Research/Learning-Perspectives/data/Ensemble_learning/2'


# Filter the files
filter_files(main_file + '.txt')
filter_files(eval_file + '.txt')

# generate nouns
noun_file_main = main_file + 'n' + '.txt'
noun_eval_file = eval_file + 'n' + '.txt'

## keywords extracted from the main file will normalize all the values
normalizing_val = extract_keywords(main_file+'.txt',noun_file_main)
## keywords extracted from the eval file will be stored for clustering 
count_eval = extract_keywords(eval_file+'.txt',noun_eval_file)

# one hot encoding
main_score = encode(noun_file_main,noun_eval_file,normalizing_val) 


# store the results in a file to be used by clustering
# value to be store is main_score and count_eval
results_file = '/home/manan/Desktop/Research/Learning-Perspectives/results/scores.txt'
write_score(count_eval,main_score,results_file)
