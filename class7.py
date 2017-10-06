# import os
# #print os.getcwd()
# #os.mkdir('c:\\') #make directory
# #os.chdir('c:\\abc') #change directory
# #os.rmdir('') #remove directory
# #print os.getcwd() #get working directory
# #print os.getpid()
# #os.rename('text.txt','tex2.txt')
# #print os.urandom(1000) #print random shit
# i=0
# while(i<10001):
#     print os.urandom(1)
#     i+=1

l1=[2,3,16,8]
# # for i in range(len(l1)):
# #     l1[i]*=2
# # print l1
# mult=lambda x: x*2
# for i in l1:
#     l2.append(mult(i))
# print l2

#print map(lambda x:x*2,l1)         #map takes each every value of list and passes to a function
#print filter(lambda x:x%2==0, l1)
print reduce(lambda x,y :x+y,l1)
