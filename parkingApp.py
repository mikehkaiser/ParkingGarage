# Your Code will go here
# need a class ParkingGarage()
# def __init__(self, tickets = 50, parkingSpaces = 50, currentTicket = True)
# self.tickets = tickets #define a number of tickets for the garage, default 50
# self.parkingSpaces = parkingSpaces #define number of parking spaces, should equal tickets, default 50
# self.currentTicket = currentTicket #status of current ticket payment, either true or false, when taken, changes to false and then to true when paid

# have ticket 'name' same as parking space 'name'
# it will have def takeTicket(), def payForParking(), and def leaveGarage()
# the attributes for the class are tickets = [], parkingSpaces = [], currentTicket = {}
# currentTicket has key of 'paid' and value of 'True' or 'False'
# currentTicket

# self.tickets.remove()
# self.parkingSpaces.remove()
# add that ticket as key to currentTicket dictionary with value of false

# payForParking


# leaveGarage()
# ticket = input('Please enter your parking space:')
# if currentTicket.value = 'Awaiting Payment', payment = input('Please enter payment before leaving:')
# then payment triggers change in currentTicket.value to 'Paid'
# if currentTicket.value = True, print('Thanks! Enjoy your day!')
# parkingSpaces self.parkingSpaces.append()
# tickets self.ticekts.append()


# We designed this for parking garages of any size: default is 11 spaces. 
"""
    parkingSpaces is a list that records all of the remaining available spaces in the lot.
    It is empty by default.
    
    currentTicket is a dictionary that records the parking spots taken and their payment respective
    payment status. This is primarily for custodial purposes.

    occSpaces is a list that also stores the spaces taken; it allowed us to easily tell the user
    how many spaces are remaining in the lot, and whether the lot was full.

"""
from IPython.display import clear_output

class ParkingGarage():
    def __init__(self, tickets=list(range(1, 11)), parkingSpaces=list(range(1, 11)), currentTicket={}, occSpaces=[]):
        self.tickets = tickets  # define a number of tickets for the garage, default 10
        # define number of parking spaces, should equal tickets, default 10
        self.parkingSpaces = parkingSpaces
        # status of current ticket payment, either true or false, when taken, changes to false and then to true when paid
        self.currentTicket = currentTicket
        self.occSpaces = occSpaces

    def takeTicket(self):
        clear_output()
        if len(self.parkingSpaces) == 0:
            print('Sorry, the lot is full.')
        else:
            print(f'Available spaces: {self.parkingSpaces}')
            spot = int(input('What spot are you going to park in?'))
            if isinstance(spot, str) and spot not in self.parkingSpaces:
                print("Please enter a valid number")
            else:
                print("Welcome to the Garage!")
                self.currentTicket[spot] = 'unpaid'
                self.parkingSpaces.remove(spot)
                self.occSpaces.append(spot)
                self.tickets.remove(spot)

    """
        takeTicket first checks to see if the lot is full, then asks the user to 
        indicate WHICH SPOT in the parking lot they would like to occupy.
        If anything besides a number in the self.parkingSpaces list is entered,
        the terminal will ask again for a valid input. It will during this time 
        also display the spaces available.   
    """

    def availableSpaces(self):
        # return integer number of count of number of parking spaces available
        clear_output
        print(
            f'There are {len(self.parkingSpaces)} spaces available: {self.parkingSpaces}')

    def timetoleave(self):
        clear_output
        takenspot = int(input("Please enter your ticket number here: "))
        if len(self.occSpaces) == 0:
            print('The lot is empty. Please contact an attendant.')
        elif isinstance(takenspot, str) or takenspot not in self.occSpaces:
            print("Please enter a valid number")
        else:
            print("Your cost is $5.25. Please pay your ticket ")
            payticket = input("(press any key to continue)")
            if isinstance(payticket, str):
                self.currentTicket[takenspot] = 'paid'
                self.parkingSpaces.append(takenspot)
                self.tickets.append(takenspot)
                self.occSpaces.remove(takenspot)
                print("Thank you for parking here, please come again!")

    """
        timetoleave first asks the user for their ticket number. If a number is entered,
        and the lot is 'empty', some kind samaritan has payed their ticket! Here they must
        ask an attendant for help. If the number is in the list, the program will return a 
        generic cost request. From the program's standpoint, we assume that the user will pay
        the ticket using some other system, and upon any keystroke will consider the spot to be
        paid and free. NOTE: the currentTicket dictionary will record previously occupied spots 
        as 'paid' until they are occupied again. 

    """
    

    def custodian(self):
        clear_output
        passcode = input('Please enter your passcode.')
        if passcode == '1234':
            print(self.currentTicket)

    """
        'custodian' is a SECRET command (not listed in the input string) that is designed 
        for the parking attendant to use to check to see if the person who is leaving has paid
        the ticket. If the dictionary says 'unpaid', which it will as soon as a ticket is 
        purchased for the spot in question until payment, this means someone is trying to escape
        without paying! 
    """

    def ParkingLot(self):
        while True:
            print(
                f'Welcome to the parking garage: there are {len(self.parkingSpaces)} spaces available. Are you entering or exiting?')
            starterput = input("Please type 'Enter' or 'Exit'. ")
            if starterput.lower() == 'enter':
                self.takeTicket()
            elif starterput.lower() == 'exit':
                self.timetoleave()
            elif starterput.lower() == 'custodian':
                self.custodian()
            else:
                print(
                    "Please select 'Enter' or 'Exit' or ask an attendant for assistance")

    """
        the ParkingLot method runs on top of everything else, and allows the user to indicate
        what they would like to do. NOTE: it runs ALL THE TIME. We thought this would be running
        either in a simple computer that would be turned off and on, or by an app within an
        operating system, that would keep running until turned off. Mostly we didn't want a 
        customer to be able to turn it off.
    """


lot = ParkingGarage()
lot.ParkingLot()
