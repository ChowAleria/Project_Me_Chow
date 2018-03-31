#ALERIA, MADEL S.
#arrays and functions (1)

from array import*
chow_array = array('i',[1,2,3,4,5,6,7])

for i in chow_array:
    print (i)

print ("\n **List first three items individually** \n")
print (chow_array[0])
print (chow_array[1])
print (chow_array[2])

print("Original array: \n "+str(chow_array))

print("\n Append 11 at the end of the array:")
chow_array.append(11)
print("\nNew array: \n"+str(chow_array))