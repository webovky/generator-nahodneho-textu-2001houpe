#!/usr/bin/env python3

import random

try:  
    filename = input("Zadejte jméno souboru:")
    with open(filename + ".txt","w", encoding = "utf-8" ) as soubor:
        abeceda = "qwertzuiopasdfghjklyxcvbnm"
        pslov = int(input("Zadejte počet slov:"))
        if pslov <0:
            print("Příště zadejte přirozené číslo!")
        pslov = abs(pslov)
        count = 1
        pocet_znaku = 0
        while (count <= pslov):
            delka_slova= random.randint(1,7)
            slovo = ""
            for a in range(delka_slova):
                pismeno = random.choice(abeceda)
                slovo = slovo + pismeno
                pocet_znaku = pocet_znaku + 1
            soubor.write(slovo)
            if (count < pslov):
                soubor.write(" ")
            else:
                break
            pocet_znaku = pocet_znaku + 1
            count = count + 1
            if (pocet_znaku > 80):
                soubor.write("\n")
                pocet_znaku = 0
            else:
                continue
except ValueError :
    print("Špatně jsi zadal počet slov. Zkus příště zadat přirozené číslo.") 
except type(float) :
    print("Špatně jsi zadal počet slov. Zkus příště zadat přirozené číslo.")



                 