from similarity.jaccard import *
def store_similarity(p):
    length=len(p)
    dict={}               #最终要得到的字典
    for key in p.keys():
        dict1={}                          #每个点对应的相似度字典
        for i in range(key+1,length):
            dict1.setdefault(i,jaccard(p.get(key),p.get(i)))
        dict.setdefault(key,dict1)
    return dict
