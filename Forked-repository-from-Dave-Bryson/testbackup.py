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
import sys

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






    while(True):
        command = input("type a command: ")
        if command == "QUIT":
            break 

        else:
            #assumes command is of right format.
            commandbuf = command.split()

            if(commandbuf[0] == "MINT"):
                #TODO
               banknavn = commandbuf[1]
               antall = int(commandbuf[2])
               quantity = int(commandbuf[3])
               print(banknavn)
               print(antall)
               print(quantity)

               bank = None
               for b in bankListe:
                   if(b.name == banknavn):
                       bank = b
               if(bank != None):
                   minted = bank.wallet.mint_new_coins(antall, quantity)
                   bank.wallet.receive_transfer(minted)
                   uhs.mint(minted)
                   for v in bank.wallet.spendable_inputs:
                        assert uhs.check_unspent(v)
                       
            elif commandbuf[0] == "TRANSFER":
                fraBank = commandbuf[1]
                tilBank = commandbuf[2]
                verdi = int(commandbuf[3])
                print(fraBank)
                print(tilBank)
                print(verdi)
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

                


        
def run():
    test_system()


if __name__ == "__main__":
    run()