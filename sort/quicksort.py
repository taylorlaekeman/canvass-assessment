from compare import EQUAL, HIGHER, LOWER
from random import randint

class QuickSort:
	def __init__(self, data, primary_compare, secondary_compare):
		self.data = data.copy()
		if len(self.data) > 0:
			self.primary_compare = primary_compare
			self.secondary_compare = secondary_compare
			self.pivot = self.__select_pivot()
			self.__initialize_sublists()

	def __initialize_sublists(self):
		self.sublists = {
			LOWER: list(),
			EQUAL: list(),
			HIGHER: list()
		}

	def __select_pivot(self):
		return self.data[randint(0, len(self.data) - 1)]

	def sort(self):
		if self.__is_base_case():
			return self.data
		self.__populate_sublists()
		self.__sort_sublists()
		return self.sublists[LOWER] + self.sublists[EQUAL] + self.sublists[HIGHER]

	def __is_base_case(self):
		length = len(self.data)
		return length is 0 or length is 1

	def __populate_sublists(self):
		for item in self.data:
			relationship = self.primary_compare(item, self.pivot)
			self.sublists[relationship].append(item)

	def __sort_sublists(self):
		self.sublists[LOWER] = QuickSort(self.sublists[LOWER], self.primary_compare, self.secondary_compare).sort()
		if self.secondary_compare is not None:
			self.sublists[EQUAL] = QuickSort(self.sublists[EQUAL], self.secondary_compare, None).sort()
		self.sublists[HIGHER] = QuickSort(self.sublists[HIGHER], self.primary_compare, self.secondary_compare).sort()
