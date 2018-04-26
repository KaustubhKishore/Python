y=1
while(y==1):
    try:
        x=input("Enter the number you want to add: ")
        y=input("Enter second number: ")
        x=x+y
        z=input("1.Add more numbers. 2.Display Sum")
        while(z==1):
            y=input("Enter the number to add: ")
            x=x+y
            z = input("1.Add more numbers. 2.Display Sum")
        if(z==2):
            print 'Sum is: ',x
    except:
        print 'Invalid Input. Do you want to retry?'
        y=input("1. To retry ")

    finally:
        print 'Final sum: ',x

x=input('Enter the number: ')
temp=x
sum=0
while(temp!=0):
    z=temp%10
    sum+=z
    temp=temp/10
print 'Sum of digits is: ',sum




 int i,j,n,k;
 n=4;
 for (i=0;i<n;i++)
        {
 	       	for(j=0;j<n-i;j++)
 	       	{
 	       		printf(" ");
 	       	}
 	       	for(k=0;k<i+1;k++)
 	       	{
 	       		printf("* ");
 	       	}
 	       	printf("\n");

l1=[10,20,30,10,40,'Abc']
l2=['abc','xyz']
l1.insert(2,l2[0])
print l1
l1.extend(['akjsdh','das','fasdadgada'])
print l1

l2=list()
l1=[10,20,31,41]
for a in l1:
    if((a%2)==0):
        a=a*2
        l2.append(a)

print l2

tup1= (10,20,30,40,50)
print 10 in tup1
l1=list(tup1)
print l1
l1.append(30)
print l1
tup1=tuple(l1)
print tup1


for i in xrange(100000):
    if(i%2==0):
        print i

x=input('Enter the number of rows you want')
for i in range(0,x+1):
    for y in range (0,i):
        print '*',
        y+=1
    for z in range(0,i+1):
        print '                ',
        z+=1
    print ''
    i+=1
print ''


try:
    x=100/0
    y=input("Enter a number: ")
except ZeroDivisionError:
    print "You are trying to divide a number by zero"
except NameError:
    print "You entered a string; expected a number"
except SyntaxError:
    print "Contact admin to correct coding problems"
for i in range(1,11):
    print i,
