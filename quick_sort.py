from random import choice


def quick_sort(array: list):
	if len(array) > 1:
		pivot = choice(array)                     # random center element

		less = [x for x in array if x < pivot]    # numbers less that random element
		equal = [x for x in array if x == pivot]  # numbers equal random element
		greater = [x for x in array if x > pivot] # numbers greater that random element

		return quick_sort(less) + equal + quick_sort(greater)

	else:
		return array


if __name__ == '__main__':
	array = [100, -3, 8, 2, 0, 31, 3.5, 0, 10, -4]
	sorted_array = quick_sort(array)
	print(sorted_array)
