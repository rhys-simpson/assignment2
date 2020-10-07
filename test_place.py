"""
Assignment 2 - Place Class test
Rhys Simpson
"""

from place import Place


def run_tests():
    """Test Place class"""

    # Test empty place (defaults)
    # print("Test empty place:")
    # default_place = Place()
    # print(default_place)
    # assert default_place.name == ""
    # assert default_place.country == ""
    # assert default_place.priority == 0
    # assert not default_place.visited_status

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    # Test __str__ method
    print(new_place)
    # Test mark visited method
    new_place.mark_visited()
    print(new_place)
    # Test mark unvisited method
    new_place.mark_unvisited()
    print(new_place)


run_tests()
