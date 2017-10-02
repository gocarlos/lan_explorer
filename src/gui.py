from gi.repository import Gtk, Gdk, WebKit
import sys
import os

class Browser(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super(Browser, self).__init__(*args, **kwargs)
        self.set_size_request(350,500)
        self.connect("destroy", Gtk.main_quit)

        self.webview = WebKit.WebView()
        self._load_url()

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)
        self.add(scrolled_window)

        scrolled_window.show_all()
        self.show()

    def _load_url(self):
        # url = "file://" + sys.path[0] + "/res/index.html"
        url = "http://localhost:8000"
        self.webview.load_uri(url)

if __name__ == "__main__":
    Gtk.init(sys.argv)

    browser = Browser()

    Gtk.main()
