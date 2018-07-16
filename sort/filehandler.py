def parse_file(filename):
	with open(filename, 'r') as data:
		header = data.readline()
		parsed_data = list()
		for line in data:
			parsed_data.append(__parse_line(line))
		return (header, parsed_data)

def __parse_line(line):
	return line.replace('\n', '').split(',')

def write_file(filename, header, data):
	with open(filename, 'w') as output:
		output.write(header)
		for line in data:
			output.write(__format_line(line))

def __format_line(line):
	return ','.join(line) + '\n'
