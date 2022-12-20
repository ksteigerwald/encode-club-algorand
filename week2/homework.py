import json
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn, wait_for_confirmation
from algosdk.mnemonic import to_private_key


algod_address = "https://testnet-api.algonode.cloud"
algod_client = algod.AlgodClient("", algod_address)

passphrase="unfair link shuffle bottom faculty room series strategy junk woman quarter property round cattle credit spend behave hat option pill dizzy news trade ability party"  
asset_creator_address="322QW53QB4BNKE2T52XNGD2TYQ22I4I45SMKYLR7IYSG5AYSGC2DOQTMDE"

private_key = to_private_key(passphrase)

