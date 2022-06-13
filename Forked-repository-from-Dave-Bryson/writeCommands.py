import random



"""
file.write("MINT NorgesBank 1 1000000000")
file.write("MINT DNB 1 1000000")
file.write("MINT Nordea 1 1000000")
file.write("MINT Sparebank1 1 1000000")
file.write("MINT DanskeBank 1 1000000")
"""

def allCommands(iterations):
    file = open("commands.txt", "w")

    tall = 0
    bankIndeks = 0
    antall = 0
    kvantitet = 0
    navn = ""
    navn2 = ""

    commandListe = ["MINT", "TRANSFER", "BALANCE"]
    bankListe = ["NorgesBank", "DNB", "Sparebank1", "Nordea", "DanskeBank"]

    counter = 0
    while(counter < iterations):
        tall = random.randrange(0, 3)
        line = ""

        if tall == 0:
            bankIndeks = random.randrange(0, 4)
            navn = bankListe[bankIndeks]
            antall = random.randrange(1, 20)
            kvantitet = random.randrange(1, 10000)
            line = "MINT " + navn + " " + str(antall) + " " + str(kvantitet) + "\n"
            file.write(line)
        elif tall == 1:
            navn = "foo"
            navn2 = "foo"
            while(navn == navn2): #hopper over etter en gang hvis ikke likt. Ellers repeterer til ulikt.
                bankIndeks = random.randrange(0,4)
                fraIndeks = bankIndeks
                navn = bankListe[bankIndeks]
                bankIndeks = random.randrange(0,4)
                tilIndeks = bankIndeks
                navn2 = bankListe[bankIndeks]

            kvantitet = random.randrange(1, 10000)
            line = "TRANSFER " + navn + " " + navn2 + " " + str(kvantitet) + "\n"
            file.write(line)
        elif tall == 2:
            bankIndeks = random.randrange(0,4)
            navn = bankListe[bankIndeks]
            line = "BALANCE " + navn + "\n"
            file.write(line)
        counter += 1

    file.close()

def doTransactions(iterations):
    #TODO 
    file = open("commands.txt", "w")
    bankIndeks = 0
    kvantitet = 0
    navn = ""
    navn2 = ""

    bankListe = ["NorgesBank", "DNB", "Sparebank1", "Nordea", "DanskeBank"]
    counter = 0

    while(counter < iterations):

        navn = "foo"
        navn2 = "foo"
        while(navn == navn2): #hopper over etter en gang hvis ikke likt. Ellers repeterer til ulikt.
            bankIndeks = random.randrange(0,4)
            fraIndeks = bankIndeks
            navn = bankListe[bankIndeks]
            bankIndeks = random.randrange(0,4)
            tilIndeks = bankIndeks
            navn2 = bankListe[bankIndeks]

            kvantitet = random.randrange(1, 10000)
            line = "TRANSFER " + navn + " " + navn2 + " " + str(kvantitet) + "\n"
            file.write(line)
        counter += 1
    file.close()


def doMinting(iterations):
    #TODO
    file = open("commands.txt", "w")
    bankIndeks = 0
    antall = 0
    kvantitet = 0
    navn = ""
    bankListe = ["NorgesBank", "DNB", "Sparebank1", "Nordea", "DanskeBank"]

    counter = 0
    while(counter < iterations):
        file = open("commands.txt", "w")
        tall = random.randrange(0, 3)
        line = ""


        bankIndeks = random.randrange(0, 4)
        navn = bankListe[bankIndeks]
        antall = random.randrange(1, 20)
        kvantitet = random.randrange(1, 10000)
        line = "MINT " + navn + " " + str(antall) + " " + str(kvantitet) + "\n"
        file.write(line)
        counter += 1

    file.close()





