import math

def is_even(number):
	return number % 2 == 0

def parse_thousands(number):
	return math.floor((i / 1000) % 10)

def parse_hundreds(number):
	return math.floor((i / 100) % 10)

def parse_tens(number):
	return math.floor((i / 10) % 10)

evens = list()
for i in range(1000, 3001, 2):
	if (not is_even(parse_tens(i))):
		i += 10
		continue
	if (not is_even(parse_hundreds(i))):
		i += 100
		continue
	if (not is_even(parse_thousands(i))):
		i += 1000
		continue
	evens.append("{}".format(i))
print(",".join(evens))
