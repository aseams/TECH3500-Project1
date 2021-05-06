import random
import sys

"""
Run a single trial of the Monty Hall problem, with or without switching
doors. (switch is True or False). The car is behind door number 1
and the gameshow host knows that.
"""
def run_trial(switch, ndoors=3):
	# Pick a random door out of the ndoors available
	yourDoor = random.randint(1, ndoors)
	if switch:
		# Reveal goat
		doorShown = 3 if yourDoor==2 else 2
		# Make the switch
		availDoors = [dnum for dnum in range(1,ndoors+1)
								if dnum not in (yourDoor, doorShown)]
		yourDoor = random.choice(availDoors)

	# If picked door 1, you win.
	return yourDoor == 1

"""
Run ntrials iterations of the Monty Hall problem with ndoors doors, with
and without switching (switch = True or False). Returns the number
of trials which resulted in winning the car by picking door number 1.
"""
def run_trials(ntrials, switch, ndoors=3):
	nwins = 0
	for i in range(ntrials):
		if run_trial(switch, ndoors):
			nwins += 1
	return nwins

# ProTip: Don't run a billion trials. It takes > 1388 hours
# 1 million trials ~= 5 seconds
if __name__ == "__main__":

	# Grab args from CLI. If not correct, show usage.
	args = sys.argv[1:]
	if len(args) != 2:
		print('Usage: python montyHall.py (# doors) (# trials)')
		sys.exit()

	# Set # of doors and # of trials
	ndoors = int(args[0])
	ntrials = int(args[1])

	# Run program through 5 separate executions
	for i in range(5):
		# Grab number of wins. False/True refers to no switch/switch
		nWinsNoSwitch = run_trials(ntrials, False, ndoors)
		nWinsWithSwitch = run_trials(ntrials, True, ndoors)

		# Mostly formatting to make CLI output look pretty
		if i == 0:
			print()
			print('Monty Hall Problem with {} doors over {} trials'.format(ndoors, "{:,}".format(ntrials)),'\n')
		print('Proportion of wins without switching: {:.4f}'
					.format(nWinsNoSwitch/ntrials))
		print('Proportion of wins with switching: {:.4f}'
					.format(nWinsWithSwitch/ntrials))
		if i != 4:
			print('=============')