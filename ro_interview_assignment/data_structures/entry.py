import ipaddress

class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = last_used
        
    def __str__(self):
        
        entry = {"address": self.address,
                 "available": self.available,
                 "last_used": self.last_used}
        
        return str(entry)
    

    def __lt__(self, other):

        return (int(ipaddress.ip_address(self.address)) < int(ipaddress.ip_address(other.address)))



    def get_address(self):

        return self.address
