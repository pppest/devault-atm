# this module is for communicating with the DeLight wallet
# to read atm devault wallet and send bought amount to client
# for readability and consistency I define commands for os as a string
# before calling

import os
import json
import config as c


def start_daemon():
    print('Starting daemon.')
    cmd = 'delight daemon start'
    os.system(cmd)


def stop_daemon():
    print('Stopping daemon')
    cmd = 'delight daemon stop'
    os.system(cmd)


def load_wallet(path_to_wallet):
    print('Loading wallet...')
    cmd = f'delight daemon load_wallet -w {path_to_wallet}'
    os.system(cmd)


def get_balance(path_to_wallet):
    print('getting balance')
    cmd = f'delight getbalance -w {path_to_wallet}'
    balance_data = os.popen(cmd).read()
    # use json to convert str to dict and get balance
    # and make sure atm balance is updated
    confirmed_balance = float(json.loads(balance_data)['confirmed'])
    if len(json.loads(balance_data)) > 1:
        unconfirmed_balance = float(json.loads(balance_data)['unconfirmed'])
        if unconfirmed_balance < 0:
            return confirmed_balance + unconfirmed_balance
    return confirmed_balance


def deposit(address, amount, path_to_wallet):
    print('Beginning deposit')
    # the wallet can only handle 3 decimals or it breaks
    amount_rounded = round(amount - c.TX_FEE, 3)

    txcmd = f'delight payto {address} {amount_rounded} -f {c.TX_FEE}\
            -w {path_to_wallet}'

    # set true to avoid error when converting data to dict, can be anything
    true = True
    tx_data = os.popen(txcmd).read()

    # use json to convert str to dict
    hex = json.loads(tx_data)['hex']
    broadcast_cmd = f'delight broadcast {hex}'
    tx = os.popen(broadcast_cmd).read()
    tx_id = json.loads(tx)[1]
    return tx_id


def payout_to_client(address, amount, path_to_wallet):
    start_daemon()  # make sure daemon is running
    load_wallet(path_to_wallet)
    deposit(address, amount, path_to_wallet)
    
    
