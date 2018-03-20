# MIDTERM EXAMINATION
# Aleria Madel S


def match_a():
    print ("Function match_a() \n")

    chow1 = input("Enter m1st input:")
    chow2 = input("Enter m2nd input:")
    chow3 = input("Enter m3rd input:")

    chow22 = []
    chow33 = []
    chow11 = []

    for i in chow1:
        if len(i) != 1:  # exclude character
            if i == i[::-1]:  # Palindrome checker
                chow11.append(i)

    for i in chow2:
        if len(i) != 1:  # exclude character
            if i == i[::-1]:  # Palindrome checker
                chow22.append(i)

    for i in chow3:
        if len(i) != 1:  # exclude character
            if i == i[::-1]:  # Palindrome checker
                chow33.append(i)

    print "1st output: ", len(chow11)
    print "2nd output: ", len(chow22)
    print "3rd output: ", len(chow33)


match_a()
print ("\n\n")


def front_x():
    print ("Function front_x()\n")

    chow1 = input("Enter 1st input:")
    chow2 = input("Enter 2nd input:")
    chow3 = input("Enter 3rd input:")

    chow11 = []
    chow111 = []
    chow22 = []
    chow222 = []
    chow33 = []
    chow333 = []

    for i in chow1:
        if i.startswith('x'):  # new list of strings that starts with 'x' from others
            chow11.append(i)
        else:
            chow111.append(i)  # new list of other strings

    print "1st output: ", sorted(chow11) + sorted(chow111)  # to alphabetically arranged

    for i in chow2:
        if i.startswith('x'):  # new list of strings that starts with 'x' from others
            chow22.append(i)
        else:
            chow222.append(i)  # new list of other strings

    print "2nd output: ", sorted(chow22) + sorted(chow222)  # to alphabetically arranged

    for i in chow3:
        if i.startswith('x'):  # new list of strings that starts with 'x' from others
            chow33.append(i)
        else:
            chow333.append(i)  # new list of other strings

    print "3rd output: ", sorted(chow33) + sorted(chow333)  # to alphabetically arranged


front_x()





