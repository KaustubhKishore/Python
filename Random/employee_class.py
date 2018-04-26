class Emp():
    def __init__(self):
        self.name= raw_input('Enter name of employee: ')            #SELF IS IMPORTANT IT WILL TELL THE COMPILER THAT THE VARIABLE IS OF THE OBJECT
        self.addr= raw_input('Enter address of the employee: ')
        global salary
        salary= input('Enter salary')
    @staticmethod
    def newsal():
        salary=salary-(salary*0.3)


#Input number of employees and call Emp class and append to a list of objects
x=input('Enter number of employees')
emp_data=list()
for i in range(x):
    temp_obj=Emp()
    emp_data.append(temp_obj)

#search for employee if 1 is pressed
flag = input('Press 1 to search for employee: ')
if(flag==1):
    temp_name= raw_input("Enter name of employee to search: ")
    for i in emp_data:
        if(temp_name==i.name):
            print 'Name: ',i.name
            print 'Address: ',i.addr
            print 'Salary: ',i.salary


#calculate new salary by using static method
print 'New Salary has been calculated after 30% deduction.'
Emp.newsal()
for i in emp_data:
    print 'Name: ', i.name
    print 'Address: ', i.addr
    print 'Salary: ', i.salary

