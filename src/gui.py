from gi.repository import Gtk, Gdk, WebKit
# gi.require_version('Gtk', '3.0')
import sys
import os
import django
import threading
from threading import Thread
from time import sleep
import webview
import threading
import time


# t = webview
#
# class Browser(Gtk.Window):
#     def __init__(self, *args, **kwargs):
#         super(Browser, self).__init__(*args, **kwargs)
#         self.set_size_request(350,500)
#         self.connect("destroy", Gtk.main_quit)
#
#         self.webview = WebKit.WebView()
#         self._load_url()
#
#         scrolled_window = Gtk.ScrolledWindow()
#         scrolled_window.add(self.webview)
#         self.add(scrolled_window)
#
#         scrolled_window.show_all()
#         self.show()
#
#     def _load_url(self):
#         # url = "file://" + sys.path[0] + "/res/index.html"
#         url = "http://localhost:8000"
#         self.webview.load_uri(url)
#
# def start_backend():
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lan_explorer.settings")
#     from django.core.management import call_command
#     from django.core.wsgi import get_wsgi_application
#     application = get_wsgi_application()
#     call_command('runserver',  '127.0.0.1:8000')
#
#
# def start_frontend():
#     webview.create_window("LAN Explorer", "http://127.0.0.1:8000/")
#     # t.create_window("LAN Explorer")

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        # thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

        thread2 = threading.Thread(target=self.run2, args=())
        # thread.daemon = True                            # Daemonize thread
        thread2.start()


    def run(self):
        """ Method that runs forever """
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lan_explorer.settings")
        from django.core.management import call_command
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        call_command('runserver',  '127.0.0.1:8000')

    def run2(self):
        """ Method that runs forever """
        webview.create_window("LAN Explorer", "http://127.0.0.1:8000/")

if __name__ == "__main__":
    example = ThreadingExample()


    # backend_thread = Thread(target = start_backend)
    # # backend_thread.start()
    # backend_thread.run()
    # start_frontend()

    # webview.load_url("http://localhost:8000")
    # webview.create_window("LAN Explorer", "http://127.0.0.1:8000")

    # Gtk.init(sys.argv)
    #
    # browser = Browser()
    #
    # Gtk.main()
