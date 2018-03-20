#Aleria, Madel S

chow = "A man a plan a caddy Ore Lee tsuba Thaine a lair Uball EHFA Jaela Gant Masai Liana DVS USES Ojai Ruyter Geraint Irbid Naman a milliard Nahant Epps Argall Emil Lepus a tort a loon Samia HCM a deme Lenaea glebae Keon a cart seraphs a suitor otius a shp a restr a canoe Kea Belgae an elem Edam Chaim a snool a trot a sup Elli Mell a grasp PETN a handrail Liman a mandi Britni a regret Yuria Joses USV Danai Lias a mtn a galea Jaf Hell a burial Aeniah Tabu Steele Roydd a canal Panama"

chow = chow.replace(" ", "")
chow = chow.lower()
list_chow = list(chow)
reverse_chow = list_chow[::-1]

if reverse_chow == list_chow:
    print ("It's a Palindrome")
else:
    print ("It's not a Palindrome")