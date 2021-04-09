# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1,
# 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


digits1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digits2 = [0, 1, 2, 3, 4, 5]
digits = digits2
length = len(digits)

def swap_positions(index1, index2):
	global digits
	value1 = digits[index1]
	value2 = digits[index2]
	digits[index1] = value2
	digits[index2] = value1


def in_reverse_order(list):
	sorted_list = list.sort(reverse = True)
	return sorted_list == list

def increment(position):
	global digits
	global length

	new_portion[0] = digits[length - 1]
	new_portion[1:] = digits[position -1:]

	digits[-3:] = new_portion


def next_permutation():
	global digits
	global length

	# go <- adding digits (i) and checking for reverse order
	#	if in reverse order, increment the digit in the next sig fig (i + 1) by pushing smallest sig fig to its position and shifting the others right

	for i in range(length):
		if in_reverse_order(digits[-(i+1):]):
			digits = increment(i + 2)
		
		
	#return False


if __name__ == "__main__":
	for i in range(20):
		next_permutation()
		print(digits)