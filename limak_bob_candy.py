# Bears love candies and games involving eating them. Limak and Bob play the following game. Limak eats 1 candy,
# then Bob eats 2 candies, then Limak eats 3 candies, then Bob eats 4 candies, and so on. Once someone cant
# eat what he is supposed to eat, he loses.
#
# Limak can eat at most A candies in total (otherwise he would become sick),
# while Bob can eat at most B candies in total. Who will win the game? Print "Limak" or "Bob" accordingly.

limak= input("")
bob= input("")
p=1
flag=1
winner=0
while(flag==1):
    if(p%2!=0):
        if(limak-p>=0):
            limak-=p
            winner=1
        elif(limak-p<0):
            winner=2
            flag=0
    else:
        if (bob-p >= 0):
            bob -= p
            winner = 2
        elif(bob-p<0):
            winner=1
            flag=0
    p+=1
if(winner==1):
    print "Limak"
elif(winner==2):
    print "Bob"
