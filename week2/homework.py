import json
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction
#
# My address: 322QW53QB4BNKE2T52XNGD2TYQ22I4I45SMKYLR7IYSG5AYSGC2DOQTMDE
# My private key: aIfgjqXRqO+C2NbKO/9exzpekWBG0aNgWjdNGqBU1jzetQt3cA8C1RNT7q7TD1PENaRxHOyYrC4/RiRugxIwtA==
# My passphrase: unfair link shuffle bottom faculty room series strategy junk woman quarter property round cattle credit spend behave hat option pill dizzy news trade ability party


def generate_algorand_keypair():
  private_key, address = account.generate_account()
  print("My address: {}".format(address))
  print("My private key: {}".format(private_key))
  print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))

passphrase="unfair link shuffle bottom faculty room series strategy junk woman quarter property round cattle credit spend behave hat option pill dizzy news trade ability party"  
address="322QW53QB4BNKE2T52XNGD2TYQ22I4I45SMKYLR7IYSG5AYSGC2DOQTMDE"

generate_algorand_keypair()

