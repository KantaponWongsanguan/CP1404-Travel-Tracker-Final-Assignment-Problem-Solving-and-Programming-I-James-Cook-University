"""
Modified Assignment A1 to that of each place is stored as an object of the new Place Class
"""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place


import csv
import random
from operator import itemgetter
from place import Place
from placecollection import PlaceCollection

filename = 'places.csv'


def main():
    """Travel Tracker Programme  with data from an external file"""
    print("Travel Tracker 1.0 - by Kantapong Wongsanguan")
    count_places_loaded()

    place_collection = PlaceCollection()
    place_collection.load_places(filename)

    display_menu()

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            list_places(place_collection)
        elif choice == "R":
            random_choice(place_collection)
        elif choice == "A":
            add_new_place(place_collection)
        elif choice == "M":
            if place_collection.get_number_of_unvisited_places() > 0:
                mark_visited(place_collection)
            else:
                print("No unvisited places")
        else:
            print("Invalid menu choice")
        display_menu()
        choice = input(">>> ").upper()

    place_collection.save_places(filename)
    print("Have a nice day :)")  # exited


def count_places_loaded():
    """Introduction to programme: Count places loaded from external csv file"""
    with open('places.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = sum(1 for _ in reader)

    return print(f"{rows} places loaded from places.csv")


def load_places():
    """Load saved data from external csv file"""
    places = []
    with open(filename, 'r') as csvfile:
        read_file = csv.reader(csvfile)
        for row in read_file:
            places.append(row)
    return places


def display_menu():
    """Display menu option"""
    print(
        "Menu:\nL - List places\nR - Recommend random place\nA - Add new place\nM - Mark a place as visited\nQ - Quit")


def list_places(place_collection):
    """Display list of all places neatly with their details"""
    place_collection.sort("is_visited")
    places = place_collection.places
    for i, place in enumerate(places, 1):
        visited = "*" if place.is_visited else " "
        print(f"{visited}{i}. {place}")
    print(f"{len(places)} places. You still want to visit {place_collection.get_number_of_unvisited_places()} places.")


def random_choice(place_collection):
    """Random choice recommending to visit from any available unvisited places"""
    unvisited = [place for place in place_collection.places if not place.is_visited]
    if unvisited:
        recommendation = random.choice(unvisited)
        print(f"Not sure where to visit next?\nHow about... {recommendation.name} in {recommendation.country}?")
    else:
        print("No places left to visit!")


def add_new_place(place_collection):
    """Add places to the list (unvisited as default)"""
    name = input("Name: ").strip()
    while name == "":
        print("Input cannot be blank")
        name = input("Name: ").strip()
    country = input("Country: ").strip()
    while country == "":
        print("Input cannot be blank")
        country = input("Country: ").strip()
    priority = input("Priority: ").strip()
    new_place = Place(name, country, priority)
    place_collection.add_place(new_place)
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


def mark_visited(place_collection):
    """Display list of all places as choice to mark as visited"""
    list_places(place_collection)
    print("Enter the number of a place to mark as visited")
    while True:
        try:
            place_num = int(input(">>> "))
            while place_num <= 0 or place_num > len(place_collection) or place_num == "":
                if place_num <= 0:
                    print("Number must be > 0")
                else:
                    print("Invalid place number")
                place_num = int(input(">>> "))
            place = place_collection[place_num - 1]
            if not place.is_visited:
                place.mark_visited()
                print(f"{place.name} in {place.country} visited!")
                break
            else:
                print("You have already visited", place.name)
                break
        except ValueError:
            print("Invalid input; enter a valid number")


def save_places(places):
    """Save data to an external file"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for place in places:
            writer.writerow(place)


main()
