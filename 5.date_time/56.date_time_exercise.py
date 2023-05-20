import datetime
from time import *


class Event:
    def __init__(self, startTime, endTime) -> None:
        self.startTime = startTime
        self.endTime = endTime
        self.venue = None

    def getVenue(self):
        print(self.venue.getAddress())

    def setVenue(self, venue):
        self.venue = venue

    def getEventDetails(self):
        print("Start time: ", self.startTime)
        print("End time: ", self.endTime)
        print("Venue name: ", self.venue.name)
        print("Address: ",)
        self.venue.getAddress()


class Venue:
    def __init__(self, name) -> None:
        self.name = name
        self.address = []

    def getAddress(self):
        for i in self.address:
            print("Address is {} {} {} {}".format(
                i.street, i.city, i.state, i.city))

    def setNewAddress(self, address):
        self.address.append(address)


class Address:
    def __init__(self, street, city, state, country) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.country = country


adress = Address(
    "Example street",
    "Example city",
    "Example State",
    "Example Country"
)

venue = Venue("Example Venue")
venue.setNewAddress(adress)

event = Event(datetime.time(15,00), datetime.time(18,000))
event.setVenue(venue)
event.getEventDetails()
