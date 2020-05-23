class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = ipv4_network
        self.entries = raw_entry_list


    def __str__(self):

        network_collection = {self.ipv4_network : self.entries}

        return str(network_collection)



    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        import ipaddress

        entries_list = self.entries.copy()

        for entry in entries_list:
            try:
                ip_address = ipaddress.IPv4Address(entry.get_address())
                if ip_address not in self.ipv4_network:
                    self.entries.remove(entry)
            except:
                # ip address invalid
                self.entries.remove(entry)




    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
