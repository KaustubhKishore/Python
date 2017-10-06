# b=[9,1,8,2,7,3,6,4,5,0,5345,6456,234,76,56,47,234,1,23,54,6]
# for i in range(len(b)):
# 	for j in range(len(b)):
# 		if(b[i]<b[j]):
# 			t= b[j]
# 			b[j]= b[i]
# 			b[i]= t
# print b
# import numpy
# print numpy.std([2,8,5,3,9,12])

# for p in range(len(b)):
#     for i in range(len(b)-1):
#         if (b[i]>b[i+1]):
#             t=b[i+1]
#             b[i+1]=b[i]
#             b[i]=t
# print b

# a=[10,45,23,65,87,12,43,54]
#
# pivotval=len(a)/2
# for i in range(len(a)/2):
#     if(a[i]>a[pivotval]):
#         t=a[pivotval+i+1]
#         a[pivotval+i+1]=a[i]
#         a[i]=a[pivotval+i+1]
#
# print a
# print pivotval

# str='Hello World!'
x=['ab','cd']
for i in x:
    x.append(i.upper())
print x