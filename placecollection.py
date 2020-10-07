"""
Assignment 2 - Place Collection Class
Rhys Simpson
"""


class PlaceCollection:
    """Represent a list of place objects"""

    def __init__(self, places=None):
        """Initialise a collection of places"""
        if places is None:
            places = []
            self.places = places

    def load_places(self, filename):
        """Load places from csv and store into places list"""
        in_file = open(filename, "r")
        for line in in_file:
            parts = line.strip().split(",")
            parts[2] = int(parts[2])
            self.places.append(parts)
        in_file.close()
        return self.places

    def save_places(self):
        """Save places from the places list to the csv file"""

    def add_place(self):
        """Add a place object to places attribute"""

    def get_unvisited_places(self):
        """Retrieve number of unvisited places in list"""

    def sort_places(self):
        """Sorted by..., then priority"""
        # might have to do __lt__

    pass
