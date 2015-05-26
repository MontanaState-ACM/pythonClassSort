import random

def set():
	arrayLen = 100
	boundary = 10
	i = 0
	numbers = []
	while i < arrayLen:
		numbers = numbers + [random.randrange(-10, boundary)]
		i = i + 1	
	sort(numbers)
	
def sort(array):
	isSorted = False
	j = 0
	counter = 0
	while isSorted == False:
		j = (j + 1) % (len(array) - 1)
		if array[j] > array[j + 1]:
			temp = array[j]
			array[j] = array[j + 1]
			array[j + 1] = temp
			counter = 0
		elif counter == len(array):
			isSorted = True		
		else:
			counter = counter + 1				
	print(array)
	
set()
