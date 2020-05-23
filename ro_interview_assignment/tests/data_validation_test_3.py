# -*- coding: utf-8 -*-
"""

@author: robert.duchi
"""



import unittest
import os
import ipaddress



os.chdir('..')

from data_structures.network_collection import NetworkCollection
from data_structures.entry import Entry





class TestEntry(unittest.TestCase):
    def test_sort_records(self): 
        
        network_address = ipaddress.IPv4Network('192.168.0.0/24')
        
        network = NetworkCollection(network_address, [Entry("255.255.255.0", True, "30/01/20 17:00:00"),
                                                      Entry("192.168.0.3", True, "30/01/20 17:00:00"),
                                                      Entry("10.0.12.1", True, "30/01/20 17:00:00"),
                                                      Entry("10.0.8.1", True, "30/01/20 17:00:00"),
                                                      Entry("192.168.10.6", True, "30/01/20 17:00:00")])
        
        
        valid_network = NetworkCollection(network_address, [Entry("10.0.8.1", True, "30/01/20 17:00:00"),
                                                            Entry("10.0.12.1", True, "30/01/20 17:00:00"),
                                                            Entry("192.168.0.3", True, "30/01/20 17:00:00"),
                                                            Entry("192.168.10.6", True, "30/01/20 17:00:00"),
                                                            Entry("255.255.255.0", True, "30/01/20 17:00:00")])
        
        
        network.sort_records()        
               
        self.assertEqual([e.address for e in network.entries], 
                         [e.address for e in valid_network.entries])
        

        
if __name__ == '__main__':
    unittest.main()



