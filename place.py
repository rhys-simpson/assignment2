"""
Assignment 2 - Place Class
Rhys Simpson
"""


class Place:
    """Represent a Place object"""

    def __init__(self, name, country, priority, visited_status):
        """Initialise a Place instance.

        name: string, name of place
        country: string, country of place
        priority: integer, value for visiting priority
        visited_status: True/False, marked visited or unvisited
        """
        self.name = name
        self.country = country
        self.priority = priority
        self.visited_status = visited_status

    def __str__(self):
        """Return a string of Place object"""
        return "{} - {} in {} priority {}".format(self.visited_status, self.name, self.country, self.priority)

    def mark_visited(self):
        """Mark a place as visited"""
        self.visited_status = " "

    def mark_unvisited(self):
        """Mark a place as unvisited"""
        self.visited_status = "*"

    def is_important(self):
        """Determine if a place is important (important if - priority <= 2)"""
        if self.priority <= 2:
            return "Place is important"

    pass
