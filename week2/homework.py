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

txn = AssetConfigTxn(
  sender=asset_creator_address,
  sp=algod_client.suggested_params(),
  total=1000,
  default_frozen=False,
  unit_name="LATINUM",
  asset_name="VelaruLatinum" ,
  manager=asset_creator_address,
  reserve=asset_creator_address,
  freeze=asset_creator_address,
  clawback=asset_creator_address,
  url="https://gateway.pinata.cloud/ipfs/QmRCVewpjF9DCDih2rMcdZ8HaC8WDp3e7pUhyivi8RzqzD",
  decimals=0) 
  

signed_txn = txn.sign(private_key)
try:
  txid = algod_client.send_transaction(signed_txn)
  print("Signed transaction with txID: {}".format(txid))  
  confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
  print("TXID: ", txid)
  print("Result confimation in round: {}".format(confirmed_txn['confirmed-round']))
except Exception as err:
  print(err)
  
  
print("Transaction Info: {}".format(
  json.dumps(confirmed_txn, indent=4)))