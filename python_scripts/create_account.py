import json
import base64
from tkinter.messagebox import YES
from algosdk import account, mnemonic
from algosdk.v2client import algod
import time
from kmd_wallet import KmdAlgorand
from algosdk import transaction

def send_algos_transaction(algod_client, receiver_address, sender_address, sender_private_key, amount):
    # Construct the transaction
    params = algod_client.suggested_params()

    txn = transaction.PaymentTxn(
        sender=sender_address,
        receiver=receiver_address,
        amt=amount,
        sp=params
    )

    # Sign the transaction with the sender's private key
    signed_txn = txn.sign(sender_private_key)

    # Send the transaction to the Algorand network
    try:
        tx_id = algod_client.send_transaction(signed_txn)
        print("Transaction ID:", tx_id)
    except Exception as e:
        print("Transaction failed:", e)

def create_account(fund=True):
    # Initialize the KmdAlgorand object
    kmd_algo = KmdAlgorand()

    # Create a new wallet
    user_wallet = kmd_algo.create_user_wallet(wallet_name="user", wallet_password="user")

    # Generate a new account for this wallet
    my_address = kmd_algo.get_account_address(user_wallet)
    print("My address: {}".format(my_address))

    # Check your balance. It should be 0 microAlgos
    account_info = kmd_algo.query_account_information(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

    if fund:
        # Specify the node address and token.
        algod_address = "http://localhost:4001"
        algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

        # Initialize an algod client
        algod_client = algod.AlgodClient(algod_token=algod_token, algod_address=algod_address)

        # Get the default wallet and its first account
        default_wallet = kmd_algo.create_user_wallet(wallet_name="unencrypted-default-wallet", wallet_password="")
        default_account = default_wallet.list_keys()[0]

        # Sender's private key and amount to transfer
        sender_private_key = default_wallet.export_key(default_account)
        amount = 1000000  # 1 Algo

        # Fund the account
        send_algos_transaction(
            algod_client=algod_client, 
            receiver_address=my_address, 
            sender_address=default_account, 
            sender_private_key=sender_private_key, 
            amount=amount)

        print('Fund transfer in process...')
        # Wait for the transaction to be confirmed
        time.sleep(5)
        
        print('Fund transferred!')
        # Check your balance. It should be 5000000 microAlgos
        account_info = kmd_algo.query_account_information(my_address)
        print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

        # Get the private key
        private_key = user_wallet.export_key(my_address)

        # Convert the private key to a mnemonic
        m = mnemonic.from_private_key(private_key)

    return m