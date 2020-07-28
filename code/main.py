from filter import filter_files
from extract_kw import extract_keywords
from one_hot_encoding import encode
main_file = '/home/manan/Desktop/Research/Learning-Perspectives/data/Ensemble_learning/1'
eval_file = '/home/manan/Desktop/Research/Learning-Perspectives/data/Ensemble_learning/2'

# Filter the files

filter_files(main_file + '.txt')
filter_files(eval_file + '.txt')

# generate nouns
noun_file_main = main_file + 'n' + '.txt'
noun_eval_file = eval_file + 'n' + '.txt'


extract_keywords(main_file+'.txt',noun_file_main)
extract_keywords(eval_file+'.txt',noun_eval_file)

# one hot encoding

encode(noun_file_main,noun_eval_file)
