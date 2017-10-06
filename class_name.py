class Name():
    def __init__(self):
        self.first= raw_input('Enter First name: ')
        self.last= raw_input('Enter Last name: ')


    @staticmethod
    def stat(self):
        temp = self.first+ self.last
        print temp

obj1=Name()
Name.stat(obj1)
#use lambda function to concatenate all the elements from a list to a single
# l1=['a','b','c','d']
# >>> reduce(lambda x,y: x+y, l1)
# 'abcd'