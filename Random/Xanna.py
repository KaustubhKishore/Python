test_case= input("") #Enter the number of test cases
p=0
while(p<test_case):
    x= input('') #Enter the number of tasks: 
    xen=list()
    yan=list()
    for i in range(x):
        temp= input("") #Enter time for xenny
        xen.append(temp)
        temp= input("") #Enter time for yan
        yan.append(temp)
    time_sum=0
    time_sum2=0
    for i in range(x):
        if(i%2==0):
            time_sum+=xen[i]
            time_sum2+=yan[i]
        else:
            time_sum+=yan[i]
            time_sum2+=xen[i]

    if(time_sum>time_sum2):
        print "",time_sum2 #Minimum time taken by Xenny and Yanna is
    else:
        print "", time_sum #Minimum time taken by Xenny and Yanna is
    p+=1
