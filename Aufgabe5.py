for i in range(0, 3):
    answer = input ("Was ist die Hauptstadt der Schweiz")
    if answer == "Bern":
        print("Gratulation, sie haben die Prüfung bestanden")
        break
    elif i == 2:
        print("Sie haben die Prüfung leider nicht bestanden")
    else: 
        print("Leider falsch, sie haben noch " + str(2 - i) + (" Versuche"))
