#!/usr/bin/env conda run -n default python

import subprocess  # https://docs.python.org/3/library/subprocess.html
# DEPRECATED import optparse  # https://docs.python.org/3/library/optparse.html instead
import argparse  # https://docs.python.org/3/library/argparse.html#module-argparse
import re  # https://docs.python.org/3/library/re.html?highlight=re#module-re


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest='interface', help='specify the interface to MAC modify', type=str)
    parser.add_argument("-m", "--mac", dest="new_mac", help="Specify MAC to be used", type=str)
    args = parser.parse_args()
    interface, new_mac = args.interface, args.new_mac

    if not interface:
        parser.error("no interface specified")
    elif not new_mac:
        parser.error("no new mac specified")
    
    return interface, new_mac


def change_mac(interface_mac_tuple):
    interface, new_mac = interface_mac_tuple
    print("Changing Mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


change_mac(get_args())
