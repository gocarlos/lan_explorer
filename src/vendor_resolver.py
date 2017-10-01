#!/usr/bin/env python3
import requests

"""
    Using the API of this website:
    https://macvendors.com/
"""

url = 'http://api.macvendors.com/'

class MacAdressResolver():


    def __init__(self, mac_address):
        self._address = mac_address
        r = requests.get(url + self._address)
        if r:
            print('Vendor is: "' + r.content + '"')
            self.vendor = r.content
        else:
            print('Vendor not found')

            self.vendor = None


if __name__ == '__main__':
    MacAdressResolver('FC:FB:FB:01:FA:21')
