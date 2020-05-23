# -*- coding: utf-8 -*-
"""

@author: robert.duchi
"""



import unittest
import os



os.chdir('..')

from data_structures.datacenter import Datacenter
from data_structures.cluster import Cluster





class TestDatacenter(unittest.TestCase):
    def test_remove_invalid_clusters(self): 
        
        datacenter_name = "Berlin"
       
        datacenter = Datacenter(datacenter_name, [Cluster('BER-1', 0, []), 
                                                  Cluster('BER-203', 0, []),
                                                  Cluster('BER-4000', 0, []),
                                                  Cluster('TEST-1', 0, [])])
        
        valid_datacenter = Datacenter(datacenter_name, [Cluster('BER-1', 0, []),
                                                        Cluster('BER-203', 0, [])])
    
        datacenter.remove_invalid_clusters()  
        
        self.assertEqual([d.name for d in datacenter.clusters],
                         [d.name for d in valid_datacenter.clusters])
        

        
if __name__ == '__main__':
    unittest.main()



