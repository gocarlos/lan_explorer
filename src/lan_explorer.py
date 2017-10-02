#!/usr/bin/env python3
import os
import sys
import time
from subprocess import Popen, DEVNULL
from lan_explorer_tools import Tools
import subprocess
import webview
import django
import threading
from threading import Thread
from time import sleep


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

def start_backend():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lan_explorer.settings")
    from django.core.management import call_command
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    call_command('runserver',  '127.0.0.1:8000')

# def start_frontend():

if __name__ == '__main__':
    # Clear the screen
    # subprocess.call('clear', shell=True)

    Thread(target = start_backend).start()
    sleep(1)
    webview.create_window("LAN Explorer", "http://127.0.0.1:8000")
    # Thread(target = start_frontend).start()

    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lan_explorer.settings")
    # try:
    #     from django.core.management import execute_from_command_line
    # except ImportError:
    #     # The above import may fail for some other reason. Ensure that the
    #     # issue is really that Django is missing to avoid masking other
    #     # exceptions on Python 2.
    #     try:
    #         import django
    #     except ImportError:
    #         raise ImportError(
    #     "Couldn't import Django. Are you sure it's installed and "
    #     "available on your PYTHONPATH environment variable? Did you "
    #     "forget to activate a virtual environment?"
    #     )
    #     raise
    # if (len(sys.argv)>1):
    #     execute_from_command_line(sys.argv)
    # else:
    #     execute_from_command_line("runserver")

    # tools = Tools()
    # l = LanExplorer(tools.get_my_ip())
    # l.get_ips()
