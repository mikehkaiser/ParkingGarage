# ParkingGarage
OOP Parking Garage exercise

### Ian and Mike's ParkingApp, designed to operate within the parking terminal at the entrance/exit of a parking garage.

We came to the project with ideas already commented out from Nate's instruction and were quickly able to setup the init 
and initial methods of takeTicket() and availableSpaces()

### Mike as driver
With Mike driving the coding, __init__, takeTicket(), and availableSpaces() were quickly set up and troubleshot until
a first draft was satisfactory.

### Ian as driver
With Ian driving, timetoleave() was established. Ian also set up the final method of ParkingLot, which is essentially the program.

### After a short lunch break

With Mike as driver again, we got back to it to troubleshoot and think of anything else we wanted to add. This is when Ian thought
of the 'custodian' method, which prints out the dictionary of the days tickets, showing 'unpaid' if the space is currently occupied,
'paid' if the spot had been occupied and is supposed to be empty, and nothing if the spot had not been used that day.

To run the program, a variable is instantiated and assigned class ParkingGarage. In the testing, we used 'lot'. Defaults
are set up for all attributes as available spaces of 10, tickets of 10, an empty dictionary of ticket payment status, and
an empty list of occupied spaces.

Once instantiated, you can run the program with lot.ParkingLot(). We did our best to work out edge cases in case 
the lot is full or empty or to see if we could exit without paying.

Once again, the most difficult part was github, but considering it was just two of us, and the scope of the project
was not as vast as the CRM mockup, we had fewer issues overall and were able to traverse terminal/github to find answers
to the few sticking points we had (like adding DS_store to .gitignore).

In all, we believe the project was a success, and we had fun working together.
