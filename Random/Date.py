#takes input as a string which has to be in format of "DD-MM-YYYY" or "D-M-YYYY" or "D-MM-YYYY" and so on
#prints the month in words and removes 0 before date if input is for example '01-2-2017'
months= ['January','February','March','April','May','June','July','August','September','October','November','December']
date= raw_input("Enter the  date in 'DD-MM-YYYY' format: ")
newdate=''
for i in range(len(date)):
    if(date[i]!='-'):
        newdate+=date[i]
flag=0
month=''
for i in range(len(date)-5):
    if(date[i]=='-'):
        if(date[i+2]!='-'):
            month=month+date[i+1]+date[i+2]
        else:
            month = month + date[i + 1]
month=int(month)
new_date=''
for i in range(2):
    if(date[i]!='-'):
        new_date+=date[i]
new_date = int(new_date)
if  month <= 0 or new_date <= 0:
    print "INCORRECT DATE!"
else:
    print "Date today is: ", new_date, " ", months[month-1], " ", newdate[-4:]
