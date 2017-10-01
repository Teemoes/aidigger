# -*- coding: cp936 -*-
import numpy as np
from sklearn.cluster import KMeans

data = np.random.rand(100,3) #100个3维连续型变量
penalty = 1 #惩罚系数
k = 0
p = 0

for i in range(2,5):
    #选取类别数i，最多迭代(max(i)-min(i)+1)*n_init*max_iter次    
    estimators = KMeans(n_clusters=i,init='k-means++',
                   n_init=10, max_iter=300,tol=1e-4)
    estimators.fit(data)
    label_pred = estimator.labels_
    centroids = estimator.cluster_centers_
    
    inertia = estimators.inertia_ + penalty * i
    if(i == 2):
        min_inertia = inertia
    if(inertia < min_inertia):
        k = i


estimator = KMeans(n_clusters=k,init='k-means++',
                   n_init=10, max_iter=300,tol=1e-4)
estimator.fit(data)
label_pred = estimator.labels_
centroids = estimator.cluster_centers_

np.savetxt('label.txt',label_pred,fmt='%d') #保存标签

#连续保存质心
f = open('centroids.txt','a')
for j in centroids:
    for l in j:
        f.write(str(l)+' ')
        p = p + 1
        if(p == 3):
            f.write('\n')
            p = 0
f.close()
