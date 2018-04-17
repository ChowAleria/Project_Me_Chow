#ALERIA, MADEL S.
#RemoveDuplicates

def remdupli():
    chowdupli = input("Enter numbers: ")
    chowdupli = list(chowdupli)
    chow = []
    chow2 = []

    for i in chowdupli:
        chowdupli.count(i)
        if chowdupli.count(i) != 1:
                chow.append(i)
        elif chowdupli.count(i) == 1:
                chow2.append(i)

    set(chow2)
    print chow2
    return(remdupli())

remdupli()