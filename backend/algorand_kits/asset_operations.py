import json
import hashlib
from algosdk.v2client import algod
from algosdk import account, mnemonic
from algosdk.transaction import AssetConfigTxn, AssetTransferTxn, wait_for_confirmation
import algosdk
import os
import sys
from algorand_kits.create_account import create_account

# Initialize Algorand client
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_address = "http://192.168.137.236:4001"
algod_client = algod.AlgodClient(algod_token, algod_address)

def print_created_asset(algodclient, account, assetid):
    account_info = algodclient.account_info(account)
    idx = 0
    for my_account_info in account_info['created-assets']:
        scrutinized_asset = account_info['created-assets'][idx]
        idx = idx + 1       
        if scrutinized_asset['index'] == assetid:
            print("Asset ID: {}".format(scrutinized_asset['index']))
            print(json.dumps(my_account_info['params'], indent=4))
            break

def print_asset_holding(algodclient, account, assetid):
    account_info = algodclient.account_info(account)
    idx = 0
    for my_account_info in account_info['assets']:
        scrutinized_asset = account_info['assets'][idx]
        idx = idx + 1        
        if scrutinized_asset['asset-id'] == assetid:
            print("Asset ID: {}".format(scrutinized_asset['asset-id']))
            print(json.dumps(scrutinized_asset, indent=4))
            break

def create_asset(m, receiver_pk, asset_name,ipfs):
    private_key = algosdk.mnemonic.to_private_key(m)
    public_key = algosdk.account.address_from_private_key(private_key)
    accounts = {1: {'pk': public_key, 'sk': private_key}}

    params = algod_client.suggested_params()

    f = open('algorand_kits/NFT/metadata.json', "r")
    metadataJSON = json.loads(f.read())
    metadataStr = json.dumps(metadataJSON)

    hash = hashlib.new("sha512_256")
    hash.update(b"arc0003/amj")
    hash.update(metadataStr.encode("utf-8"))
    json_metadata_hash = hash.digest()

    txn = AssetConfigTxn(
        sender=accounts[1]['pk'],
        sp=params,
        total=1,
        default_frozen=False,
        unit_name="10-Cert",
        asset_name=asset_name,
        manager=accounts[1]['pk'],
        reserve=receiver_pk,
        freeze=None,
        clawback=None,
        strict_empty_address_check=False,
        url="https://aqua-advanced-eel-969.mypinata.cloud/ipfs/"+ipfs,
        metadata_hash=json_metadata_hash,
        decimals=0
    )

    stxn = txn.sign(accounts[1]['sk'])
    txid = algod_client.send_transaction(stxn)

    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))

    try:
        ptx = algod_client.pending_transaction_info(txid)
        asset_id = ptx["asset-index"]
        print_created_asset(algod_client, accounts[1]['pk'], asset_id)
        print_asset_holding(algod_client, accounts[1]['pk'], asset_id)
    except Exception as e:
        print(e)

def opt_in(trainee_m, asset_id):
    trainee_sk = algosdk.mnemonic.to_private_key(trainee_m)
    trainee_pk = algosdk.account.address_from_private_key(trainee_sk)

    params = algod_client.suggested_params()
    params.fee = 1000
    params.flat_fee = True

    txn = AssetTransferTxn(
        sender=trainee_pk,
        sp=params,
        receiver=trainee_pk,
        amt=0,
        index=asset_id
    )
    stxn = txn.sign(trainee_sk)
    txid = algod_client.send_transaction(stxn)

    wait_for_confirmation(algod_client, txid)
    print_asset_holding(algod_client, trainee_pk, asset_id)

def transfer_asset(sender_m, receiver_pk, asset_id):
    sender_sk = algosdk.mnemonic.to_private_key(sender_m)
    sender_pk = algosdk.account.address_from_private_key(sender_sk)

    params = algod_client.suggested_params()
    params.fee = 1000
    params.flat_fee = True

    txn = AssetTransferTxn(
        sender=sender_pk,
        sp=params,
        receiver=receiver_pk,
        amt=1,
        index=asset_id
    )
    stxn = txn.sign(sender_sk)
    txid = algod_client.send_transaction(stxn)

    wait_for_confirmation(algod_client, txid)
    print_asset_holding(algod_client, receiver_pk, asset_id)

if __name__ == "__main__":
    action = sys.argv[1]

    if action == "create_asset":
        m = sys.argv[2]
        receiver_pk = sys.argv[3]
        asset_name = sys.argv[4]
        ipfs = sys.argv[5]
        create_asset(m, receiver_pk,asset_name,ipfs)

    elif action == "opt_in":
        trainee_m = sys.argv[2]
        asset_id = sys.argv[3]
        opt_in(trainee_m, asset_id)

    elif action == "transfer_asset":
        sender_m = sys.argv[2]
        receiver_pk = sys.argv[3]
        asset_id = sys.argv[4]
        transfer_asset(sender_m, receiver_pk, asset_id)
