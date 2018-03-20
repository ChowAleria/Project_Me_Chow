


print ("1. NAND \n2. NOR \n3. NOT \n4. AND \n5. OR \n6. XOR \n7. XNOR \n8. TTL adder-subtractor \n.9 Active High Input S-R latch (Nor Gste) \n10. Active Low Input S-R latch (nand gate) \n11. Switch Debouncer \n12. Gated S-R Latch \n13. Gate D Latch \n14. Application using switch debouncer \n15. SR FlipFlop \n16. D FlipFlop \n17. JK FlipFlop \n18. T FlipFlop \n19. Universal Shift Register \n20. BCD Ripple CounterMOD10 \n21. Up/Down Binary Counter \n22. Binary Counter with Parallel Load \n23. Ring Counter")
def madel():
    gate = {"1":"7400","2":"7402","3":"7404","4":"7408","5":"7432","6":"7486","7":"74266","8":"7483","9":"7402","10":"7400","11":"7402","12":"7400","13":"7400 and 7402","14":"7400","15":"7400","16":"7400","17":"7410 and 7400","18":"7410 and 7400","19":"74194","20":"74LS90","21":"74LS193","22":"74LS161","23":"74LS194"}
    chow = input("\nEnter LOGIC GATE: ")

    if chow == 1:
        print "IC Number" , gate["1"]
    elif chow == 2:
        print "IC Number" ,gate["2"]
    elif chow == 3:
        print "IC Number" ,gate["3"]
    elif chow == 4:
        print "IC Number" ,gate["4"]
    elif chow == 5:
        print "IC Number" ,gate["5"]
    elif chow == 6:
        print "IC Number" ,gate["6"]
    elif chow == 7:
        print "IC Number" ,gate["7"]
    elif chow == 8:
        print "Can use IC Number" ,gate["8"]
    elif chow == 9:
        print "Can use IC Number", gate["9"]
    elif chow == 10:
        print "Can use IC Number", gate["10"]
    elif chow == 11:
        print "Can use IC Number", gate["11"]
    elif chow == 12:
        print "Can use IC Number", gate["12"]
    elif chow == 13:
        print "Can use IC Number", gate["13"]
    elif chow == 14:
        print "Can use IC Number", gate["14"]
    elif chow == 15:
        print "Can use IC Number", gate["15"]
    elif chow == 16:
        print "Can use IC Number", gate["16"]
    elif chow == 17:
        print "Can use IC Number", gate["17"]
    elif chow == 18:
        print "Can use IC Number", gate["18"]
    elif chow == 19:
        print "Can use IC Number", gate["19"]
    elif chow == 20:
        print "Can use IC Number", gate["20"]
    elif chow == 21:
        print "Can use IC Number", gate["21"]
    elif chow == 22:
        print "Can use IC Number", gate["22"]
    else:
        print "Invslid INPUT. TRY AGAIN!!!"
    return madel()
madel()

