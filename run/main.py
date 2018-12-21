from similarity.store_similarity import *
from graph.graph import *
if __name__=='__main__':
    file=open('D://学习/大三/可视化/大作业/data.txt', 'r')
    done=0
    num=0              #论文对应的序号
    dict1={}           #dict1  key:论文序号  value:论文名称
    dict2={}
    while not done:
        if file.readline().strip('\n')=='论文':
            dict1.setdefault(num,file.readline().strip('\n'))
        length=int(file.readline().strip('\n'))
        p={}
        for i in range(0,length):
            p.setdefault(i,file.readline().strip('\n'))
        dict2.setdefault(num,p)
        num=num+1
        if file.readline()!='':
            pass
        else:
            done=1
    dict3=store_similarity(dict2)                 #dict2 key:论文序号  value:引用的论文
    print(dict1)
    print(dict2)
    print(dict3)                                 #dict3 key:论文序号  value:当前论文和其他论文的相似度
    for key,value in dict3.items():
        print(key,':',value)
    data = dict3
    data = data_verify(data)
    data = format_transform(data)
    total_points, loss = tf_get_points(data)
    for tmp in total_points:
        print(tmp)
    print(loss)
