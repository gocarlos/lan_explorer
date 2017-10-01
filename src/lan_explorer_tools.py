#!/usr/bin/env python3

import socket
import os
import sys

class Tools():

    def __init__(self):
        self._hostname = socket.gethostname()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        self._myip = s.getsockname()[0]

    def get_hostname(self):
        return self._hostname

    def get_my_ip(self):
        return self._myip

    def __str__(self):
        return 'Hostname: "' + self._hostname + '"' + '\n' + \
        'IP: "' + self._myip + '"'

    def getmac(interface):

      try:
        mac = open('/sys/class/net/'+interface+'/address').readline()
      except:
        mac = "00:00:00:00:00:00"

      return mac[0:17]


  
if __name__ == '__main__':
    tools = Tools()
    print(tools)
