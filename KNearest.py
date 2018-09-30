import cv2
import numpy
import matplotlib.pyplot as plt

// Sample KNeighbors test code

testData = numpy.random.randint(0,100,(20,2)).astype(numpy.float32)
red_blue = numpy.random.randint(0,2,20).astype(numpy.float32)

reds = testData[red_blue.ravel() == 1]
blues = testData[red_blue.ravel() == 0]
plt.scatter(reds[:,0], reds[:,1], 100 , 'red')
plt.scatter(blues[:,0], blues[:,1], 100 , 'blue')

testSubject = numpy.random.randint(0,100,(1,2)).astype(numpy.float32)
plt.scatter(testSubject[:,0], testSubject[:,1], 100, 'green')

knn = cv2.ml.KNearest_create()
knn.train(testData, cv2.ml.ROW_SAMPLE ,red_blue)
ret, results, neighbours ,dist = knn.findNearest(testSubject, k=4)
print(ret, "\n", results, '\n', neighbours, '\n', dist)

if(ret == 0):
    print("Blue")
elif(ret == 1):
    print("Red")

plt.show()
