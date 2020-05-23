class Cluster:
    def __init__(self, name, network_dict, security_level):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """

        self.name = name
        self.security_level = security_level
        self.networks = network_dict


    def __str__(self):

        cluster = {self.name :
                          {"security_level" : self.security_level,
                           "networks" : self.networks}}

        return str(cluster)    



    def get_name(self):

        return self.name
