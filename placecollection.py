"""
Assignment 2 - Place Collection Class
Rhys Simpson
"""

from operator import attrgetter


class PlaceCollection:
    """Represent a list of place objects"""

    def __init__(self):
        """Initialise a collection of places"""
        self.places = []

    def __str__(self):
        """Return a string of PlaceCollection with Place objects"""
        place = [place_data for place_data in self.places]
        return "{}".format(place)

    def load_places(self, filename):
        """Load places from csv and store into places list"""
        in_file = open(filename, "r")
        for line in in_file:
            parts = line.strip().split(",")
            if parts[3] == "n":
                parts[3] = False
            else:
                parts[3] = True
            parts[2] = int(parts[2])
            self.places.append(parts)
        in_file.close()
        return self.places

    # TODO
    def save_places(self):
        """Save places from the places list to the csv file"""

    def add_place(self, add_place):
        """Add a place object to places attribute"""
        new_place = str(add_place).split(',')
        new_place[2] = int(new_place[2])
        self.places.append(new_place)

    def get_unvisited_places(self):
        """Retrieve number of unvisited places in list"""
        unvisited_places_number = 0
        for place_data in self.places:
            if place_data[3] == "n":
                unvisited_places_number += 1
        return unvisited_places_number

    # TODO
    def sort(self):
        """ """
        name_priority = {}
        for place in self.places:
            name_priority[place[0]] = place[2]
