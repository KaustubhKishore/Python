#takes an array and copies all distinct numbers to a new array
array= [2,3,90,3,3,4,100,200,2]
new_array=list()
for i in array:
    if(i not in new_array):
        new_array.append(i)
print new_array