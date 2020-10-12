"""
Assignment 2 - Console program
Rhys Simpson
GitHub URL: https://github.com/rhys-simpson/assignment2
"""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class


# to change whether is visited or not just say if True place.mark_visited; if False place.mark_unvisited

from place import Place
from operator import attrgetter
FILENAME = "places.csv"
MENU = "Menu:\nL - List Places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\n>>> "


def main():
    """Program to get and list users visited and unvisited places"""
    print("Travel Tracker 1.0 - by Rhys Simpson")
    places = get_places()
    print("{} places loaded from {}".format(len(list(places)), FILENAME))
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            print_places(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            mark_visited(places)
        else:
            print("Invalid menu choice")
        choice = input(MENU).upper()
    save_places(places)


def get_places():
    """Convert input file to list"""
    places = []
    in_file = open(FILENAME, "r")
    for line in in_file:
        parts = line.strip().split(",")
        if parts[3] == "v":
            visited_status = True
        else:
            visited_status = False
        new_place = Place(name=parts[0], country=parts[1], priority=int(parts[2]), is_visited=visited_status)
        places.append(new_place)
    in_file.close()
    return places


def print_places(places):
    """Print places from place list"""
    # Get longest elements in place list from another function
    longest_country_name_length, longest_number_length, longest_town_name_length = longest_elem_length(places)
    unvisited_number = unvisited_places_value(places)

    places.sort(key=attrgetter("is_visited", "priority"))
    for number, places_data in enumerate(places):
        # Check if place is unvisited and assign "*" in print statement
        parts = str(places_data).strip().split(",")
        if parts[3] == "True":
            unvisited_marker = ""
        else:
            unvisited_marker = "*"
        print("{:1}{}. {:<{}} in {:<{}} priority {:>{}}".format(unvisited_marker, number+1, parts[0],
                                                                longest_town_name_length, parts[1],
                                                                longest_country_name_length, parts[2],
                                                                longest_number_length))

    if unvisited_number <= 0:
        print("{} places. No places left to visit. Why not add a new place?".format(len(list(places))))
    else:
        print("{} places. You still want to visit {} places.".format(len(list(places)), unvisited_number))

    # print important places (for loop to ensure only important places are listed and doesn't return 'None')
    print("\nImportant Places (if priority is less than 2) -")
    for place in places:
        if place.is_important():
            print(place.is_important())


# TODO FIX to work with class
def longest_elem_length(places):
    """Get longest elements in places list for formatting"""
    parts = str(places).split(",")
    longest_town_name_length = max(len(places_data[0]) for places_data in parts)
    longest_country_name_length = max(len(places_data[1]) for places_data in parts)
    longest_number_length = max(len(str(places_data[2])) for places_data in parts)
    return longest_country_name_length, longest_number_length, longest_town_name_length


def unvisited_places_value(places):
    """Retrieve number of unvisited places in list"""
    unvisited_places_number = 0
    for places_data in places:
        parts = str(places_data).split(",")
        if parts[3] == "False":
            unvisited_places_number += 1
    return unvisited_places_number


def add_place(places):
    """Add new place to places list"""
    name, country, priority = get_valid_input()
    new_place = Place(name, country, priority, False)
    # if statement so print statement doesn't return 'None' if new place isn't important
    if new_place.is_important():
        print(new_place.is_important())
    places.append(new_place)


def get_valid_input():
    """Error checking for add new place function"""
    finished = False
    name = input("Name: ")
    while name == "":
        print("Input can not be blank")
        name = input("Name: ")
    country = input("Country: ")
    while country == "":
        print("Input can not be blank")
        country = input("Country: ")
    while not finished:
        try:
            priority = int(input("Priority: "))
            while priority < 0:
                print("Number must be > 0")
                priority = int(input("Priority: "))
            else:
                finished = True
                print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))
                return name, country, priority
        except ValueError:
            print("Invalid input; enter a valid number")


# TODO - fix
def mark_visited(places):
    """Code to mark an unvisited place as visited with error checking"""
    finished = False

    # Check if all places are visited
    visit = unvisited_places_value(places)
    if visit == 0:
        print("No unvisited places")
        return

    print_places(places)
    print("Enter the number of a place to mark as visited")
    while not finished:
        try:
            item_to_change = int(input(">>> "))
            if item_to_change < 0:
                print("Number must be > 0")
            elif item_to_change > len(list(places)):
                print("Invalid place number")
            elif places[item_to_change - 1][3] == "True":
                print("That place is already visited")
                break
            else:
                finished = True
                places[item_to_change - 1][3].mark_visited()
                print("{} in {} visited!".format(places[item_to_change - 1][0], places[item_to_change - 1][1]))
        except ValueError:
            print("Invalid input; enter a valid number")


def save_places(places):
    """Save and update new places to csv"""
    out_file = open(FILENAME, "w")
    for places_data in places:
        parts = str(places_data).split(",")
        print("{},{},{},{}".format(*parts), file=out_file)
        places.sort(key=attrgetter("is_visited"))
    out_file.close()
    print("{} places saved to {}".format(len(list(places)), FILENAME))
    print("Have a nice day :)")


if __name__ == '__main__':
    main()
