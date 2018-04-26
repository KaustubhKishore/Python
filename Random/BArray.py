 a=list()
 t= input("Enter the number of elements in list a: ")

 for i in range(t):
     temp= input("Enter element of list: ")
     a.append(temp)


 flag=0
 for i in range(t):
     for p in range(t):
         if(i!=p):
             if(a[i]*a[p]==i):
                 flag+=1
 if(flag==t):
     print 'Beautiful Array'
 else:
     print 'ugly array'
