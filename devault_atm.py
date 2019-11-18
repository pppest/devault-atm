import os
import coingecko_price
import coinslot
import delight
import qr
import time
import config as c
from datetime import date, datetime


# load usb device
# device = coinslot.initiate_device(c.USB_VENDOR_ID, c.USB_PRODUCT_ID)
device = coinslot.initiate_device(c.USB_VENDOR_ID, c.USB_PRODUCT_ID)

# make sure wallet is loaded
delight.start_daemon()
delight.load_wallet(c.ATM_WALLET)

# log file
log_file_name = "devaultatm-" + str(date.today()) + ".log"
log_file = open(log_file_name, "a")
log_file.write('\n# date, price with fee, atm balance, coins inserted, dvt bought, wallet, tx\n')
# main app


# print slow
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)


while True:
    price_with_fee = coinstuff.price_with_fee(c.COIN, c.COIN_PAIR, c.ATM_FEE,
                                              c.COIN_DECIMALS)
    coins_inserted = 0
    dvt_bought = 0
    atm_balance = delight.get_balance(c.ATM_WALLET)

    log_file.write(f'{str(datetime.now())[0:19]}, {price_with_fee}, {atm_balance}, ')

    os.system('clear')  # clear terminal

    # print welcome msg
    delay_print(f'''

      _____    __      __         _ _           _______ __  __
     |  __ \   \ \    / /        | | |       /\|__   __|  \/  |
     | |  | | __\ \  / __ _ _   _| | |_     /  \  | |  | \  / |
     | |  | |/ _ \ \/ / _` | | | | | __|   / /\ \ | |  | |\/| |
     | |__| |  __/\  | (_| | |_| | | |_   / ____ \| |  | |  | |
     |_____/ \___| \/ \__,_|\__,_|_|\__| /_/    \_|_|  |_|  |_|
      www.devault.cc - www.devaultchat.cc - www.devault.online\a\a

          {c.COIN.capitalize()} price is: {price_with_fee} {c.COIN_PAIR.upper()}
          Available in ATM: {atm_balance} DVT
          Equal to:         {atm_balance*price_with_fee} {c.COIN_PAIR.upper()}
          Transaction fee:  {c.TX_FEE}

          Transactions are rounded to 3 decimals


          INSERT COIN TO START
          \n''')

    # insert coins
    coins_inserted = coinslot.coinslot(device, price_with_fee, atm_balance)
    if coins_inserted is not None:
        dvt_bought = coins_inserted / price_with_fee

        print(f'''
        Total amount of coins inserted: {coins_inserted} {c.COIN_PAIR.upper()}
        DVT bought: {dvt_bought}''')

        log_file.write(f'{coins_inserted}, {dvt_bought}, ')

        client_wallet = qr.read_qr_code()  # scan wallet qr

        print(f'\nYour wallet address is: {client_wallet}')
        print(f'\nSending {round(dvt_bought - c.TX_FEE, 3)} to {client_wallet}')
        log_file.write(f'{client_wallet}, ')

        # deposit dvt to client
        tx_id = delight.deposit(client_wallet, dvt_bought, c.ATM_WALLET)
        print(f'''\n
        Transaction ID: {tx_id})\n
        View on blockexplorer: https://exploredvt.com/#/DVT/mainnet/tx/{tx_id}
        ''')
        log_file.write(f'{tx_id}\n')
        delay_print("Thank you for buying DeVault!!!")
        time.sleep(5)
