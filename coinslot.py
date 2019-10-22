# methods to initialize and read coinslot via joystick usb encoder
import usb.core
import time
import config as c


def initiate_device(vendor_id, product_id):
    device = usb.core.find(idVendor=vendor_id, idProduct=product_id)

    # check if device connected
    if device is None:
        raise ValueError('Device not found!')

    # make sure kernel is dettached
    if device.is_kernel_driver_active(0):
        print("Kernel driver active, detaching.")
        device.detach_kernel_driver(0)

    else:
        print("Kernel driver not active.")

    # set to first config

    device.set_configuration()
    return device


def read_usb(device):
    data = device.read(0x81, 8, timeout=0)
    return data


# for finding interval between pulses
def pulse_test(device):
    lastpulse = 0
    intervals = []
    while len(intervals) < 19:
        d = read_usb(device)[6]
        if d == 128 and (time.time() - lastpulse > 0.13):
            pulse = time.time()
            intervals += [pulse - lastpulse]
            print(intervals[-1])
            lastpulse = pulse
    return intervals


def coinslot(device, price_with_fee, atm_balance):
    max_buy = float(atm_balance) - c.TX_FEE
    coins_inserted = 0
    coin_switch = False
    pulses = 0
    lastpulse = 0
    lastcoin = time.time()

    while True:
        dvt_bought = coins_inserted / price_with_fee
        d = read_usb(device)[6]    # input K12 on encoder is [6]==128
        # d2 is an extra button I use to stop the loop when testing
        # d2 = read_usb(device)[5]  # input K1 on encoder is [5]==31

        # TODO: test max buy
        if max_buy <= dvt_bought:
            return coins_inserted

        if d == 128 and (time.time() - lastpulse > 0.13):
            pulses += 1
            lastpulse = time.time()

        elif d != 128 and (time.time() - lastpulse > 0.3):
            if pulses == 1:
                coins_inserted += 0.5
                lastcoin = time.time()
                coin_switch = True
                dvt_bought = coins_inserted / price_with_fee
                print('You bought ' + str(0.5 / price_with_fee) + ' DVT' +
                      ' with 0.5 MXN')
                print('In total ' + str(dvt_bought) + ' DVT' + ' with ' +
                      str(coins_inserted) + ' ' + c.COIN_PAIR.upper() + '\n')
            if pulses == 2:
                coins_inserted += 1
                lastcoin = time.time()
                coin_switch = True
                dvt_bought = coins_inserted / price_with_fee
                print('You bought ' + str(1 / price_with_fee) + ' DVT' +
                      ' with 1 MXN')
                print('In total ' + str(dvt_bought) + ' DVT' + ' with ' +
                      str(coins_inserted) + ' ' + c.COIN_PAIR.upper() + '\n')
            if pulses == 3:
                coins_inserted += 2
                lastcoin = time.time()
                coin_switch = True
                dvt_bought = coins_inserted / price_with_fee
                print('You bought ' + str(2 / price_with_fee) + ' DVT' +
                      ' with 2 MXN')
                print('In total ' + str(dvt_bought) + ' DVT' + ' with ' +
                      str(coins_inserted) + ' ' + c.COIN_PAIR.upper() + '\n')
            if pulses == 4:
                coins_inserted += 5
                lastcoin = time.time()
                coin_switch = True
                dvt_bought = coins_inserted / price_with_fee
                print('You bought ' + str(5 / price_with_fee) + ' DVT' +
                      ' with 5 MXN')
                print('In total ' + str(dvt_bought) + 'DVT' + ' with ' +
                      str(coins_inserted) + ' ' + c.COIN_PAIR.upper() + '\n')
            if pulses == 5:
                coins_inserted += 10
                lastcoin = time.time()
                coin_switch = True
                dvt_bought = coins_inserted / price_with_fee
                print('You bought ' + str(10 / price_with_fee) + ' with 10 MXN')
                print('In total ' + str(dvt_bought) + ' DVT' + ' with ' +
                      str(coins_inserted) + ' ' + c.COIN_PAIR.upper() + '\n')
            if (time.time() - lastcoin) > 15 and coin_switch is True:
                return coins_inserted
            if (time.time() - lastcoin) > 15 and coin_switch is False:
                return None

            pulses = 0
            lastpulse = 0
