#!/usr/bin/env python3
import os
import time
from subprocess import Popen, DEVNULL
from lan_explorer_tools import Tools
import subprocess

class LanExplorer():

    # Amount of time for ping
    timeout = '20'

    def __init__(self, address):
        self._ip = address
        self._addr =  address.rsplit('.', 1)[0]

    def get_ips(self):

        p = {} # ip -> process
        for n in range(1, 255): # start ping processes
            ip = self._addr + ".%d" % n
            # https://linux.die.net/man/8/ping
            p[ip] = Popen(['ping', '-n', '-w' + self.timeout, '-c3', ip], stdout=DEVNULL)

        while p:
            for ip, proc in p.items():
                if proc.poll() is not None: # ping finished
                    del p[ip] # remove from the process list
                    if proc.returncode == 0:
                        print('%s active' % ip)
                    elif proc.returncode != 1:
                        print('%s error' % ip)
                    break


if __name__ == '__main__':
    # Clear the screen
    subprocess.call('clear', shell=True)

    tools = Tools()
    l = LanExplorer(tools.get_my_ip())
    l.get_ips()
