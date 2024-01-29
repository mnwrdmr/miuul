import pandas as pd
import glob

path = '/Users/macvbookpro/PycharmProjects/miuul/Interproscan/*.tsv'
out_file = '/Users/macvbookpro/PycharmProjects/miuul/output/data/ipr_concat.csv'
list_file = glob.glob(path)

#get species name from the filenames

sp_dic = {}
for element in list_file:
    i = element.split('.')[0]
    i= i.split('/')[-1]
    sp_dic[i] = element

dic_ann = {}
for key, value in sp_dic.items():
    dic_ann[key] = pd.read_csv(value, sep='\t', header=None, names=list(range(0,15)), engine='python', quoting=3)[[0,11,12]][:100]
    dic_ann[key] = dic_ann[key].dropna().drop_duplicates().rename(columns={0: 'id', 11:'ipr', 12:'ann_inter'})
    #add a columns with the species name
    dic_ann[key]['sp'] = key
    dic_ann[key].to_csv(f'/Users/macvbookpro/PycharmProjects/miuul/resource/data/{key}.csv', sep='\t', index=False)

#concat all the species
concat = pd.concat(dic_ann, axis=0).dropna().drop_duplicates()
concat.to_csv(out_file, sep='\t', index=False)