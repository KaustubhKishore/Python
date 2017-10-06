def inputdict(key):
    flag=1
    while(flag==1):
        temp=[]
        x = input('Enter marks in Physics: ')
        temp.append(x)
        x = input('Enter marks in Maths: ')
        temp.append(x)
        x = input('Enter marks in Computers: ')
        temp.append(x)
        x = input('Enter marks in Communications: ')
        temp.append(x)
        x = input('Enter marks in Chemistry: ')
        temp.append(x)
        stu_data[key]=temp
        flag=input('Are you sure you entered the correct marks? Press 1 to input marks again.')


def maxmarks(sub):
    max1=stu_data[namekeys[0]][sub]
    for s in (1,len(namekeys)-1):
        if(max1<stu_data[namekeys[s]][sub]):
            max1=stu_data[namekeys[s]][sub]
    return max1


numofstus=input('Enter number of students in the class: ')
stu_data={}

for i in range(numofstus):
    name=raw_input('Enter the name of the student: ')
    inputdict(name)
print stu_data

namekeys=stu_data.keys()
print namekeys
for p in range(0,5):
    if(p==0):
        maximum1= maxmarks(0)
        print 'Section Highest for Physics: ',maximum1
    if(p==1):
        maximum1= maxmarks(1)
        print 'Section Highest for Maths: ',maximum1
    if(p==2):
        maximum1= maxmarks(2)
        print 'Section Highest for Computers: ',maximum1
    if(p==3):
        maximum1= maxmarks(3)
        print 'Section Highest for Communications: ',maximum1
    if(p==4):
        maximum1= maxmarks(4)
        print 'Section Highest for Chemistry: ',maximum1

def perc(name):
    sum=0
    for m in range(5):
        sum+=stu_data[name][m]
    percen=float(sum)/5
    return percen
percentage_all=[]
for q in stu_data:
    percentage=perc(q)
    print 'Percentage of ',q,' is: ',percentage
    percentage_all.append(percentage)
perc_flag=percentage_all[0]
for s in range(1,len(percentage_all)):
    if(perc_flag<percentage_all[s]):
        perc_flag=percentage_all[s]
print 'Highest Percentage of the section is: ',perc_flag