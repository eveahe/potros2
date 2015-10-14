#These modules take raw input and then transform it. 
#Figure out how to turn these into classes.
def scan_input(raw):
	lowered = raw.lower()
	scanned_input = lowered.split(' ')
	print scanned_input 

print scan_input("This is a Test SenTence")


def match_input(scanned_input, key):
	if set(scanned_input) & set(key) == set([]):
		print "Did not find a match."
	else:
		print "Found a match"


match_input(['this', 'is', 'a', 'test', 'sentence'], ['test','pray'])