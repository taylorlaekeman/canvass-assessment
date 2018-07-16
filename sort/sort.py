from compare import compare_dates, compare_ids
from filehandler import parse_file, write_file
from quicksort import QuickSort

(header, data) = parse_file('random_data.csv')
sorted_data = QuickSort(data, compare_ids, compare_dates).sort()
write_file('random_data_sorted.csv', header, sorted_data)
