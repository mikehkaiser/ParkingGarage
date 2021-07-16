# Your Code will go here
# need a class ParkingGarage()
# def __init__(self, tickets = 50, parkingSpaces = 50, currentTicket = True)
#self.tickets = tickets #define a number of tickets for the garage, default 50
#self.parkingSpaces = parkingSpaces #define number of parking spaces, should equal tickets, default 50
#self.currentTicket = currentTicket #status of current ticket payment, either true or false, when taken, changes to false and then to true when paid

#have ticket 'name' same as parking space 'name'
# it will have def takeTicket(), def payForParking(), and def leaveGarage()
# the attributes for the class are tickets = [], parkingSpaces = [], currentTicket = {}
#currentTicket has key of 'paid' and value of 'True' or 'False'
#currentTicket 

#self.tickets.remove()
#self.parkingSpaces.remove()
#add that ticket as key to currentTicket dictionary with value of false

#payForParking


#leaveGarage()
#ticket = input('Please enter your parking space:')
#if currentTicket.value = 'Awaiting Payment', payment = input('Please enter payment before leaving:')
    #then payment triggers change in currentTicket.value to 'Paid'
#if currentTicket.value = True, print('Thanks! Enjoy your day!')
# parkingSpaces self.parkingSpaces.append()
# tickets self.ticekts.append()

class ParkingGarage():
    def __init__(self, tickets = list(range(1,11)), parkingSpaces = list(range(1,11)), currentTicket = {}):
        self.tickets = tickets #define a number of tickets for the garage, default 10
        self.parkingSpaces = parkingSpaces #define number of parking spaces, should equal tickets, default 10
        self.currentTicket = currentTicket #status of current ticket payment, either true or false, when taken, changes to false and then to true when paid


    def takeTicket(self):
        print(f'Available spaces: {self.parkingSpaces}')
        spot = int(input('What spot are you going to park in?'))
#         response = input('What do you want to do?')
#         if response == 'park':
        self.parkingSpaces.remove(spot)
        self.tickets.remove(spot)
        
    def availableSpaces(self):
        print(f'There are {len(self.parkingSpaces)} spaces available: {self.parkingSpaces}') # return integer number of count of number of parking spaces available

lot = ParkingGarage()
lot.takeTicket()
lot.availableSpaces()