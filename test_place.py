"""
Assignment 2 - Place Class test
Rhys Simpson
"""

from place import Place


def run_tests():
    """Test Place class"""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place("", "", 0, False)
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

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

    # Test marking multiple places visited/ unvisited and testing is_important method
    print()
    print("Test multiple places and is_important:")
    second_place = Place("Lima", "Peru", 3, False)
    places = [new_place, second_place]
    for place in places:
        place.mark_visited()
        print(place)
        place.mark_unvisited()
        print(place)
        if place.is_important():
            print(place.name)


run_tests()
