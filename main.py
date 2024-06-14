"""
Name: Kantapong Wongsanguan
Date: 6/9/2023
Brief Project Description: Travel Tracker 2.0
GitHub URL: https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-KantapongWongJC14405427
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from placecollection import PlaceCollection
from place import Place
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

OPTIONS = {"Visited": "is_visited", "Priority": "priority", "Country": "country", "Name": "name"}


class PlaceToVisitApp(App):
    """Program to create a travel tracker app using the PlaceCollection class."""
    current_place = StringProperty()
    sort_places = ListProperty()

    def __init__(self, **kwargs):
        """Initialise the object attributes of the PlaceToLearnApp class."""
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.sort_places = OPTIONS.keys()

    def build(self):
        """Build TravelTracker 2.0 by loading the kivy and csv files."""
        self.title = "TravelTracker"
        self.root = Builder.load_file("app.kv")
        self.current_place = self.sort_places[0]
        self.place_collection.load_places("places.csv")
        self.create_widgets()
        self.root.ids.top_message.text = f"Places to visit: {self.place_collection.get_number_of_unvisited_places()}"
        self.root.ids.bottom_message.text = "Welcome to Travel Tracker 2.0"
        return self.root

    def switch_sort_option(self, current_place):
        """Switch sort option."""
        self.current_place = current_place
        self.sort_places_by_option(current_place)

    def create_widgets(self):
        """Create widgets for each place in the app."""
        self.root.ids.main_places.clear_widgets()  # Clear widgets, so they do not multiply when switching between tabs.
        for place in self.place_collection.places:
            text = str(place)  # Convert place object to a string.
            temporary_button = Button()
            temporary_button.text = text
            temporary_button.place = place  # Assign attribute place to object.
            temporary_button.bind(on_press=self.mark_place_status)
            if place.is_visited:
                temporary_button.background_color = "gray"
            else:
                temporary_button.background_color = (0, 0.8, 0.9, 1)
            self.root.ids.main_places.add_widget(temporary_button)

    def mark_place_status(self, button):
        """Mark the selected place as visited or unvisited."""
        place = button.place
        if place.is_visited:
            place.mark_unvisited()
            button.text = str(place)
            button.background_color = (0, 0.8, 0.9, 1)  # Change background color to unvisited color
            if place.is_important():
                self.root.ids.bottom_message.text = f"You visited {place.name}. Great travelling!"
            else:
                self.root.ids.bottom_message.text = f"You visited {place.name}."
        else:
            place.mark_visited()
            button.text = str(place)
            button.background_color = "gray"  # Change background color to visited color
            if place.is_important():
                self.root.ids.bottom_message.text = f"You need to visit {place.name}. Get going!"
            else:
                self.root.ids.bottom_message.text = f"You need to visit {place.name}."
        self.root.ids.top_message.text = f"Places to visit: {self.place_collection.get_number_of_unvisited_places()}"

        self.sort_places_by_option(self.current_place)


    def sort_places_by_option(self, option):
        """Sort the places based on the selected sort option."""
        if option == "Visited":
            self.place_collection.sort("is_visited")
        else:
            self.place_collection.sort(OPTIONS[option])
        self.create_widgets()

    def add_new_place(self):
        """Add a new place from user's input with error checking."""
        add_name = self.root.ids.name_input.text.title()
        add_country = self.root.ids.country_input.text.title()
        add_priority = self.root.ids.priority_input.text
        if len(add_name) == 0 or len(add_country) == 0 or len(
                add_priority) == 0:  # Check the length of user's input and return error if it is zero.
            self.root.ids.bottom_message.text = "All fields must be completed"
            return
        else:
            try:
                add_priority = int(add_priority)
                if add_priority < 0:
                    self.root.ids.bottom_message.text = "Priority must be > 0"
                    return
            except ValueError:
                self.root.ids.bottom_message.text = "Please enter a valid number"
                return
        new_place = Place(add_name, add_country, add_priority)
        self.place_collection.add_place(new_place)
        self.create_widgets()
        self.root.ids.bottom_message.text = f"{add_name} in {add_country}, priority {add_priority} added"
        self.clear_place_inputs()

    def on_stop(self):
        """Save the new places into the csv file."""
        self.place_collection.save_places("places.csv")

    def clear_place_inputs(self):
        """Clear all user inputs."""
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""
    

PlaceToVisitApp().run