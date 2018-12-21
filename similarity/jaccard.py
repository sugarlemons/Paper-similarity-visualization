#-*-coding:utf-8 -*-

#计算jaccard系数
def jaccard(p,q):                 #计算字典格式数据的相似度
    c = [v for v in p.values() if v in q.values()]
    return float(len(c) / (len(p) + len(q) - len(c)))
'''
    def jaccard(p,q):                      #计算元组或集合格式数据的相似度
    c = [v for v in p if v in q]
    return float(len(c) / (len(p) + len(q) - len(c)))
'''
