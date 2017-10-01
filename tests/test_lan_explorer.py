from src import lan_explorer, vendor_resolver
import unittest

response = 'Cisco Systems, Inc'
# url = 'http://api.macvendors.com/'
mac_address = 'FC:FB:FB:01:FA:21'


class MyTest(unittest.TestCase):

    def test(self):
        print ('\n\n\n\n\n\nInside the test\n\n\n\n')
        self.assertEqual(my_great_app.fun(3), 4)

    def test2(self):
        self.assertEqual(MacAdressResolver(mac_address), response)

if __name__ == '__main__':
    unittest.main()
