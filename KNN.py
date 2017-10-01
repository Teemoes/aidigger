import numpy
import operator

def createDataSet():
    group =array([[1.2,0.9],
             [1.1,1.0],
             [1.0,1.1],
             [0.1,0.2],
             [0.0,0.1],
             [0.2,0.3]])
    labels = [1,1,1,2,2,2]
    return group,labels

def kNNClassify(newInput, dataSet, labels, k):
    numSamples = dataSet.shape[0]
    diff = tile(newInput, (numSamples, 1)) - dataSet
    squaredDiff = diff ** 2
    squaredDist = sum(squaredDiff, axis = 1)
    distance = squaredDist ** 0.5
    sortedDistIndices = argsort(distance)
    classCount = {}
    for i in xrange(k):
        voteLabel = labels[sortedDistIndices[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
        maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key
    return maxIndex

dataSet, labels = createDataSet()

testX = [1.2, 1.0]
k = 3
outputLabel = kNNClassify(testX, dataSet, labels, 3)
print testX, "is in", outputLabel

testX = [0.1, 0.3]
outputLabel = kNNClassify(testX, dataSet, labels, 3)
print  testX, "is in", outputLabel
