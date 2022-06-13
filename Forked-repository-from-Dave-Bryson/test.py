from cbdc.wallet import Wallet
from cbdc.uhs import UhsController
from re import T
from cbdc.transaction import (
    Outpoint,
    TxIn,
    TxOut,
    Transaction,
    hash_tx_input,
    uhs_id_from_output,
)
from cbdc.utils.keys import PUBLIC_KEY_SIZE, SIGNATURE_SIZE
import pytest
from nacl.exceptions import BadSignatureError
from cbdc.utils.hash import hash256
from cbdc.utils.address import encode_address, decode_address
from cbdc.utils.keys import generate_keypair, sign_message, verify_signature
#from writeCommands import allCommands
#from writeCommands import doTransactions
#from writeCommands import doMinting
import sys
import random
import time


"""
def test_processing():
    bob = Wallet()
    dave = Wallet()
    uhs = UhsController()

    assert dave.balance == 0
    assert bob.balance == 0

    minted = dave.mint_new_coins(10, 100)
    dave.receive_transfer(minted)
    assert dave.balance == 1000

    uhs.mint(minted)
    for v in dave.spendable_inputs:
        assert uhs.check_unspent(v)
"""

class Bank:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet 

def test_system():
    """
    NorgesBank = Wallet()
    uhs = UhsController()
    DNB = Wallet()
    Nordea = Wallet()
    Sparebank1 = Wallet()
    DanskeBank = Wallet()
    """
    iterations = 100000
    doTransactions(iterations)
    print("ferdig med printing")

    NorgesBank = Bank("NorgesBank", Wallet())
    DNB = Bank("DNB", Wallet())
    Nordea = Bank("Nordea", Wallet())
    Sparebank1 = Bank("Sparebank1", Wallet())
    DanskeBank = Bank("DanskeBank", Wallet())
    bankListe = []
    bankListe.append(NorgesBank)
    bankListe.append(DNB)
    bankListe.append(Nordea)
    bankListe.append(Sparebank1)
    bankListe.append(DanskeBank)
    uhs = UhsController()
    
    
    
    for bank in bankListe:
        minted = bank.wallet.mint_new_coins(1, 1000000)
        bank.wallet.receive_transfer(minted)
        uhs.mint(minted)
        for v in bank.wallet.spendable_inputs:
                assert uhs.check_unspent(v)

    file = open("commands.txt", "r")

    counter = 0
    #while(True):
    start = time.time()
    end = start + 60
    while(counter < iterations and time.time() < end):
    
        #command = input("type a command: ")
        command = file.readline()
        #print(command)
        
     
        if command == "QUIT":
            break 

        else:

            #assumes command is of right format.
            commandbuf = command.split()

            if(commandbuf[0] == "MINT"): #if bør være good.
               banknavn = commandbuf[1]
               antall = int(commandbuf[2])
               quantity = int(commandbuf[3])

               bank = None
               for b in bankListe:
                   if(b.name == banknavn):
                       bank = b
               if(bank != None):
                   minted = bank.wallet.mint_new_coins(antall, quantity)
                   bank.wallet.receive_transfer(minted)
                   uhs.mint(minted)
                       
            elif commandbuf[0] == "TRANSFER":
                fraBank = commandbuf[1]
                tilBank = commandbuf[2]
                verdi = int(commandbuf[3])
                fbank = None 
                tbank = None 
                for b in bankListe:
                    if(b.name == fraBank):
                        fbank = b
                    elif(b.name == tilBank):
                            tbank = b
             
                if(tbank != None and fbank != None):
                    tx = fbank.wallet.transfer(verdi, tbank.wallet.address)
                    tbank.wallet.receive_transfer(tx)
            
            elif commandbuf[0] == "BALANCE":
                #TODO
                banknavn = commandbuf[1]
                bank = None

                for b in bankListe:
                    if(b.name == banknavn):
                        bank = b
                
                if(bank != None):
                    print(f"{bank.name}: ", bank.wallet.balance)
            
        counter += 1
    print("ITERASJON NR: " + str(counter))

    file.close()




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
    file = open("commands.txt", "w")
    bankIndeks = 0
    antall = 0
    kvantitet = 0
    navn = ""
    bankListe = ["NorgesBank", "DNB", "Sparebank1", "Nordea", "DanskeBank"]

    counter = 0
    while(counter < iterations):
        print("teller " + str(counter))
        line = ""

        bankIndeks = random.randrange(0, 4)
        navn = bankListe[bankIndeks]
        antall = random.randrange(1, 20)
        kvantitet = random.randrange(1, 10000)
        line = "MINT " + navn + " " + str(antall) + " " + str(kvantitet) + "\n"
        file.write(line)
        counter += 1

    file.close()
        
def run():
    test_system()


if __name__ == "__main__":
    run()




