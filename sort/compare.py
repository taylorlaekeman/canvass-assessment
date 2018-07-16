DEVICE_ID_INDEX = 0
DATE_INDEX = 5
LOWER = 'lower'
EQUAL = 'equal'
HIGHER = 'higher'

def compare_ids(other, pivot):
	other_id = __parse_id(other)
	pivot_id = __parse_id(pivot)
	return __compare_nums(other_id, pivot_id)

def __parse_id(item):
	return item[DEVICE_ID_INDEX]

def compare_dates(other, pivot):
	(other_year, other_month, other_day) = __parse_date(other)
	(pivot_year, pivot_month, pivot_day) = __parse_date(pivot)
	year_relationship = __compare_nums(other_year, pivot_year)
	month_relationship = __compare_nums(other_month, pivot_month)
	day_relationship = __compare_nums(other_day, pivot_day)
	if year_relationship is not EQUAL:
		return year_relationship
	elif month_relationship is not EQUAL:
		return month_relationship
	return day_relationship

def __parse_date(item):
	return item[DATE_INDEX].split('/')

def __compare_nums(other, pivot):
	if int(other) < int(pivot):
		return LOWER
	elif int(other) is int(pivot):
		return EQUAL
	return HIGHER
