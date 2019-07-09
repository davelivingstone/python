# I created this function because I wanted something more out of fizzbuzz

def not_fizzbuzz(n):
	three = 0
	five = 0
	fifteen = 0
	for i in range(1, n+1):
		if i % 15 == 0:
			fifteen += 1
		elif i % 3 == 0:
			three += 1
		elif i % 5 == 0:
			five += 1
	return f'Count of numbers divisible by three, in range({n}): {three}, by five: {five}, by fifteen: {fifteen}'

if __name__ == '__main__':
	for i in range(100, 1000, 100):
		print(not_fizzbuzz(i))
