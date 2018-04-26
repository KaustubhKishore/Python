#wap to create a class which should take student name and name should be provided as per number of name to be
#enter. Create another class having roll numbers and details
#create another class which should ask for roll number and name should be fetched out

class Names():
    def __init__(self):
        self.name= raw_input("Enter Name: ")

class Details():
    def __init__(self):
        self.roll= input("Enter Roll Number: ")
        self.add= raw_input('Enter Address: ')

x= input("Enter number of names to enter: ")
names_data=list()
details_data=list()
for i in range(x):
    temp=Names()
    names_data.append(temp)
    temp= Details()
    details_data.append(temp)

p= input("Press 1 to search")
while(p==1):
    roll= input('Enter Roll Number to fetch details')
    for i in range(len(details_data)):
        flag=0
        if(details_data[i].roll==roll):
            print names_data[i].name, '\n', details_data[i].roll, '\n', details_data[i].add
            flag=1
    if (flag==0):
        print 'Record not found! Try Again!'
    p= input('Press 1 to continue searching: ')
