"""
Assignment 2 - Place Collection Class
Rhys Simpson
"""

from place import Place
from operator import attrgetter


class PlaceCollection:
    """Represent a list of place objects"""

    def __init__(self):
        """Initialise a collection of places"""
        self.places = []

    def __str__(self):
        """Return a string of PlaceCollection with Place objects"""
        return str([str(place) for place in self.places])

    def load_places(self, filename):
        """Load places from csv and store into places list"""
        in_file = open(filename, "r")
        for line in in_file:
            parts = line.strip().split(",")
            new_place = Place(name=parts[0], country=parts[1], priority=int(parts[2]), is_visited=parts[3])
            self.add_place(new_place)
        in_file.close()
        return self.places

    def add_place(self, add_place):
        """Add a place object to places attribute"""
        self.places.append(add_place)

    def sort(self, sort_method=""):
        """Sort places based on key passed in, then by priority"""
        if sort_method == "name":
            return self.places.sort(key=attrgetter(sort_method, "priority"))
        elif sort_method == "country":
            return self.places.sort(key=attrgetter(sort_method, "priority"))
        elif sort_method == "is_visited":
            return self.places.sort(key=attrgetter("is_visited", "priority"))
        else:
            return self.places.sort(key=attrgetter("priority"))

    # TODO
    def save_places(self):
        """Save places from the places list to the csv file"""

    #TODO - fix
    def get_unvisited_places(self):
        """Retrieve number of unvisited places in list"""
        unvisited_places_number = 0
        for places_data in self.places:
            if places_data[3] is False:
                unvisited_places_number += 1
        return unvisited_places_number
