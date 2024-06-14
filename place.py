"""
Place class for the initialisation of the travel tracker.
"""


# Create your Place class in this file


class Place:
    """Parent class for travel tracker, places to visit"""

    def __init__(self, name="", country="", priority=0, is_visited=False):
        """Assign values to the object attributes."""
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def mark_visited(self):
        """Mark place as visited."""
        self.is_visited = True

    def mark_unvisited(self):
        """Mark place as unvisited"""
        self.is_visited = False

    def __str__(self):
        """Format the objects and neatly display them."""
        if self.is_visited is True:
            status = "(visited)"
        else:
            status = ""
        return f" {self.name} in {self.country}, priority {self.priority} {status}"

    def is_important(self):
        return self.priority <= 2
