
seznam = {"Slovenija": "Ljubljana", "Italija": "Rim", "Avstrija": "Dunaj", "Francija": "Pariz", "Srbija": "Beograd","Spanija": "Madrid", "ZDA": "Washibngton", "Libija": "Tripoli", "Mauritius": "Port Louis", "Senegal": "Dakar", "Irak": "Bagdad", "Maldivi": "Male", "Vietnam": "Hanoj"}

navodilo = str("Poizkusi uganiti imena glavnih mest nastetih drzav!")

stevec = 0

print (navodilo)

for key, value in seznam.iteritems():
    print (key), "- ime glavnega mesta je: "
    odgovor = raw_input()

    if odgovor == value:
        print ("Cestitamo, dobili ste eno tocko")
        stevec += 1

    else:
        print ("Ne, ne bo prav")
        stevec -= 1

print ("Imate naslednje stevilo tock:"), (stevec)

if stevec > 0:
    print ("Se kar dobro poznate geografijo.")
else:
    print ("Ste koncali osnovno solo?Imate pa res sreco")