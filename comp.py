# -*- coding: cp936 -*-
import numpy as np
X=[]
f = open('centroids.txt','r')
for line in f.readlines():
    linelist = [float(i) for i in line.split()]
    X.append(linelist)

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

np.savetxt('labels.txt',label_pred,fmt='%d') #保存标签
