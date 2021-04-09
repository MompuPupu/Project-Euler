# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
# sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

abundant_numbers = []


def sum_proper_divisors(num):
	"""
	Return sum of all proper divisors (divisors except the number itself)
	"""
	total = 0

	for i in range(1, num):
		if num % i == 0:
			total += i
	return total


def is_abundant_number(num):
	return sum_proper_divisors(num) > num


def is_sum_of_two_abundant_numbers(num):
	global abundant_numbers

	for abundant_number in abundant_numbers:
		if num - abundant_number in abundant_numbers:
			print(num)
			return True
	return False


if __name__ == "__main__":
	answer = 0

	for i in range(28124):
		if is_abundant_number(i):
			abundant_numbers.append(i)
		if not is_sum_of_two_abundant_numbers(i):
			answer += i
	print(answer)