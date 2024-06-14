"""
A collection of places using Place class
"""

from place import Place
from operator import attrgetter


# Create your PlaceCollection class in this file


class PlaceCollection:
    """Parent class for place collection."""

    def __init__(self):
        """Set empty list."""
        self.places = []

    def load_places(self, filename):
        """Load places from places.csv"""
        in_file = open(filename)
        for place in in_file:
            place = place.strip()
            place = place.split(",")
            status = place[3].lower()  # Convert status to lowercase
            if status == "n":
                is_visited = False
            elif status == "v":
                is_visited = True
            else:
                continue  # Skip invalid status
            new_place = Place(name=place[0], country=place[1], priority=int(place[2]), is_visited=is_visited)
            self.places.append(new_place)
        in_file.close()

    def save_places(self, filename):
        """Save places into places.csv"""
        out_file = open(filename, "w")
        for place in self.places:
            if place.is_visited is False:
                status = "n"
            else:
                status = "v"
            print(f"{place.name},{place.country},{place.priority},{status}", file=out_file)
        out_file.close()

    def add_place(self, new_place):
        """Add a new place into the place collection."""
        place = Place(new_place.name, new_place.country, new_place.priority, new_place.is_visited)
        self.places.append(place)

    def get_number_of_unvisited_places(self):
        """Count the number of unvisited places."""
        list_of_unvisited_places = [place for place in self.places if place.is_visited is False]
        return len(list_of_unvisited_places)

    def get_number_of_visited_places(self):
        """Count the number of visited places."""
        list_of_visited_places = [place for place in self.places if place.is_visited is True]
        return len(list_of_visited_places)

    def sort(self, field):
        """Sort by field"""
        if field == "is_visited":
            self.places = sorted(self.places, key=lambda x: (x.is_visited, x.name))
        else:
            self.places = sorted(self.places, key=attrgetter(field, "name"))
