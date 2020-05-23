import re

class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name
        self.clusters = cluster_dict



    def __str__(self):

        datacenter = {self.name : self.clusters}

        return str(datacenter)




    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        clusters_list = self.clusters.copy()

        for cluster in clusters_list:
            validity = re.match("^({}".format(self.name[:3]).upper() + "-[1-9][0-9]{0,2})$", cluster.get_name())

            if not validity:
                self.clusters.remove(cluster)
