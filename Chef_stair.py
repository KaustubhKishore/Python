# Chef has been working in a restaurant which has N floors.
# He wants to minimize the time it takes him to go from the N-th floor to ground floor.
# He can either take the elevator or the stairs.
#
# The stairs are at an angle of 45 degrees and Chefs velocity is V1 m/s when taking the stairs down.
# The elevator on the other hand moves with a velocity V2 m/s. Whenever an elevator is called, it always starts
# from ground floor and goes to N-th floor where it collects Chef (collecting takes no time),
# it then makes its way down to the ground floor with Chef in it.
# The elevator cross a total distance equal to N meters when going from N-th floor to ground floor or vice versa,
# while the length of the stairs is sqrt(2) * N because the stairs is at angle 45 degrees.
#
# Chef has enlisted your help to decide whether he should use stairs or the
# elevator to minimize his travel time. Can you help him out?

floors= input("Enter number of floors: ")
stairs= input('Enter the velocity of chef: ')
lift=   input("Enter velocity of lift: ")

total_stair=float((floors*(2**(0.5)))/stairs)
total_lift=float(float((2*floors))/lift)

if(total_stair<total_lift):
    print "Take the Stairs!"
else:
    print "Take the elevator!"