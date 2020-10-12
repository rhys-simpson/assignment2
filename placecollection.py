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
            # assign boolean value (True/False) based on whether place is visited ("v") or unvisited ("n")
            if parts[3] == "v":
                visited_status = True
            else:
                visited_status = False
            new_place = Place(name=parts[0], country=parts[1], priority=int(parts[2]), is_visited=visited_status)
            self.add_place(new_place)
        in_file.close()
        return self.places

    def add_place(self, add_place):
        """Add a place object to places attribute"""
        self.places.append(add_place)

    def sort(self, sort_method=""):
        """Sort places based on key passed in, then by priority"""
        # sort by name then priority
        if sort_method == "name":
            return self.places.sort(key=attrgetter(sort_method, "priority"))
        # sort by country then priority
        elif sort_method == "country":
            return self.places.sort(key=attrgetter(sort_method, "priority"))
        # sort by visited status then priority
        elif sort_method == "is_visited":
            return self.places.sort(key=attrgetter(sort_method, "priority"))
        # sort by priority
        else:
            return self.places.sort(key=attrgetter("priority"))

    def save_places(self, filename):
        """Save and update places from the places list to the csv file"""
        out_file = open(filename, "w")
        for place_data in self.places:
            parts = str(place_data).split(",")
            print("{},{},{},{}".format(parts[0], parts[1], parts[2], parts[3]), file=out_file)
            self.places.sort(key=attrgetter("is_visited"))
        out_file.close()

    #TODO - fix
    # def get_unvisited_places(self):
        # """Retrieve number of unvisited places in list"""
        # unvisited_places_number = 0
        # for places_data in self.places:
            # if places_data[3] is False:
                # unvisited_places_number += 1
        # return unvisited_places_number
