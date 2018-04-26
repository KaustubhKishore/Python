row= input("Enter number of rows")
cols= input("Enter number of cols")
for i in range(row*2+1):
    if(i%2 == 0):
        for p in range(cols * 4 + 1):
            if(p%4==0):
                print ' ',
            else:
                print '-',
        print ''
    else:
        for p in range(cols*4+1):
            if(p%4==0):
                print '|',
            else:
                print ' ',
        print ''
# Find special characters in string
