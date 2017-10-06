# Alexey is trying to develop a program for a very simple microcontroller. It makes readings from
# various sensors over time, and these readings must happen at specific regular times.
# Unfortunately, if two of these readings occur at the same time, the microcontroller freezes and must be reset.
#
# There are N different sensors that read data on a regular basis. For each i from 1 to N, the reading from
# sensor i will occur every Ai milliseconds with the first reading occurring exactly Ai milliseconds
# after the microcontroller is powered up. Each reading takes precisely one millisecond on Alexey's microcontroller.
#
# Alexey wants to know when the microcontroller will freeze after he turns it on.

num= input("Enter the number of sensors: ")
nums=list()
lcm=list()
for i in range(num):
    temp= input("Enter the time taken by sensor: ")
    nums.append(temp)
lowest=nums[0]
for i in nums:
        if(i<lowest):
            lowest=i
index=0
flag=0
for i in range(num):
    if(lowest==nums[i]):
        index=i
print index

for i in range(num):
    if(i!=index):
        p=1
        lcm1=lowest
        while(p==1):
            if(lcm1%nums[index]==0 and lcm1%nums[i]==0):
                lcm.append(lcm1)
                p=0
            else:
                lcm1+=1
print lcm
lowest_lcm=lcm[0]
for i in lcm:
        if(i<lowest_lcm):
            lowest_lcm=i
# print lcm
print 'The Circuit will first break at ',lowest_lcm