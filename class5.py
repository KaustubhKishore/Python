# opt=1
#
# def add(a,b):
#     print a+b
# def sub(a,b):
#     print a-b
# def multiply(a,b):
#     print a*b
# def div(a,b):
#     print a/b
#
# while(opt==1):
#     y=input('Enter number: ')
#     z=input('Enter Number')
#     x=input('1.Add \n2.Subtract \n3.Multiply \n4.Divide\n')
#     if(x==1):
#         add(y,z)
#     elif(x==2):
#         sub(y,z)
#     elif(x==3):
#         multiply(y,z)
#     elif(x==4):
#         if(y>=z):
#             div(y,z)
#         else:
#             div(z,y)
#     else:
#         print 'Invalid input'
#     opt=input('1.Continue/Retry 2.Exit')


# def fun(l):
#     print '2. ',l
#     l.extend([1,2,3,4])
#     print '3. ', l
# l=[100,200]
# print '1. ',l
# fun(l)
# print '4. ',l


# def fun(a,b=10,c=20):
#     print a
#     print b
#     print c
# fun(*[20,30,40])

# a= [1, 2, 3, 4, 5]
# for i in range(1, 6):
#     a[i-1] = a[i]
# for i in range(0, 5):
#     print a[i]

# a=[10,23,56,[78]]
# b=list(a)
# a[3][0]=95
# a[1]=34
# print(b)

# values = [[3, 4, 5, 1], [33, 6, 1, 2]]
#
# v = values[0][0]
# for row in range(0, len(values)):
#     for column in range(0, len(values[row])):
#         if v < values[row][column]:
#             v = values[row][column]
#
# print(v)
# data = [     [[1, 2], [3, 4]],            [[5, 6], [7, 8]]                  ]
#
# print(data[1][0][0])


# def addItem(listParam):
#     listParam += [1]
#
#
# mylist = [1, 2, 3, 4]
# addItem(mylist)
# print mylist

# d = {"john":40, "peter":40}
# print d[40]

# a={1:"A",2:"B",3:"C"}
# for i,j in a.items():
#     print i
#     print j


# a = {}
# a[1] = 1
# a['gfh'] = 2
# a[2] =56
# print a

# a = {}
# a[1] = 1
# a['1'] = 2
# a[1]=a[1]+1
# count = 0
# for i in a:
#     count += a[i]
# print(count)

# test = {1:'A', 2:'B', 3:'C'}
# test = {}
# print(len(test))

# D={}
# D[1]=2
# D[2]=3
# D[4]=5
# D[5]=1
# D[1]=5
# print len(D)
# a=[]
# for j in range(0,3):
#     x=input('Enter Item for list')
#     a.append(x)
# for i in range(0,3):
#     for k in range(0,4):
#         print a[i][k],
#     print ''
#
#
# for l in range(0,4):
#     a[1][l]=a[1][l]+5
#
# for z in range(0,3):
#     for k in range(0,4):
#         print a[z][k],
#     print ''

# dict1={}
# key=input('Enter the key for dict1: ')
# value=input('Enter the value for dict1: ')
# dict1[key]=value
# key=input('Enter the key for dict1: ')
# value=input('Enter the value for dict1: ')
# dict1[key]=valuekey=input('Enter the key for dict1: ')
# value=input('Enter the value for dict1: ')
# dict1[key]=value
# print dict1
# l1=[]
# l1=dict1.keys()
# x=len(l1)

# dict={1:1,2:3,3:7}
# for i in dict:
#     dict[i]+=1
# print dict

# a=34
# del (a)
# print a

# myList = [1, 5, 5, 5, 5, 1]
# max = myList[0]
# indexOfMax = 0
# for i in range(1, len(myList)):
#     if myList[i] > max:
#         max = myList[i]
#         indexOfMax = i
#
# print(indexOfMax)

# list1 = [1, 3]
# list2 = list1
# list1[0] = 4
# print(list2)

# def f(values):
#     values[0] = 44
# v = [1, 2, 3]
# f(v)
# print(v)

# def m(list):
#     v = list[0]
#     for e in list:
#         if v < e: v = e
#     return v
#
# values = [[3, 4, 5, 1], [33, 6, 1, 2]]
# for row in values:
#     print(m(row)

# list1 = list([1, 2, 3])
# print list1
#
# list1=list("class",)
# print list1

# names = ['one', 'two', 'three', 'four']
# print(names[-1][-1])

# names1 = ['apple', 'boy', 'cat', 'dog']
# names2 = names1[:]
# names3 = names1
# names2[0] = 'yes'
# names3[1] = 'no'
# print names1,' ',names2,' ',names3


# names1 = ['apple', 'boy', 'cat', 'dog']
# names2 = names1
# names3 = names1[:]
# names2[0] = 'yes'
# names3[1] = 'no'
# sum = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'yes':
#         sum += 1
#     if ls[1] == 'no':
#         sum += 10
# print sum

# list1 = [0.5 * x for x in range(0, 4)]
# print list1

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# a[::2]=10,20,30,40
# print a


# abcd = ['Apple', 'Ball', 'Cat']
# if 'apple' in abcd:
#     print(1)
# else:
#     print(2)
#
# animals = ['cat', 'dog', 'pig', 'horse']
# animals.insert(animals.index('dog'), 'rat')
# print(animals)

# a=[1,2,3,4]
# b=(sum(a[0:x+1]) for x in range(0,len(a)))
# print(b)

# my_tuple = (1, 2, 3, 4)\
# my_tuple.append( (5, 6, 7) )
# print len(my_tuple)
#
# print type({1:2})

# a=("Check",)*3
# print a

# a = [(1, 1), (2, 4), (3, 9)]
# print type(a)

# a={1:"A",2:"B",3:"C"}
# for i in a:
#     print i

a={1:"A",2:"B",3:"C"}
print len(a)

