from similarity.jaccard import *
#显示两个数据集和他们之间的相似度
def show_similarity(p,q):
    a=jaccard(p,q)
    print(p,'\n',q)
    print('二者相似度：',a)
