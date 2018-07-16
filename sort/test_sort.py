import sort # executes sort.py
from filehandler import parse_file as parse_file_into_list
from compare import compare_dates, compare_ids, LOWER, EQUAL, HIGHER

def parse_file_into_dictionary(filename):
	with open(filename, 'r') as data:
		parsed_data = dict()
		for num, line in enumerate(data):
			line = line.replace('\n', '')
			if line in parsed_data:
				parsed_data[line] += 1
			else: 
				parsed_data[line] = 1
		return parsed_data

def are_permutations(pre, post):
	for line, count in pre.items():
		if not post[line] == count:
			return False
	return True

def is_ordered(post):
	for i in range(1, len(post) - 1):
		previous = post[i - 1]
		current = post[i]
		id_relationship = compare_ids(previous, current)
		date_relationship = compare_dates(previous, current)
		if id_relationship is HIGHER or (id_relationship is EQUAL and date_relationship is HIGHER):
			return False
	return True

pre = parse_file_into_dictionary('random_data.csv')
post = parse_file_into_dictionary('random_data_sorted.csv')
print('are permutations: {}'.format(are_permutations(pre, post)))
post_list = parse_file_into_list('random_data_sorted.csv')
print('is ordered: {}'.format(is_ordered(post_list)))
