from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number:int, seed:int) ->list[int]:
	random.seed(seed)
	myarray = []
	for k in range(number):
		myarray.append(k)
	random.shuffle(myarray)
	return myarray		

def generate():
	console.log("button works!")
	number = 10
	seed = 200

	array = []
	array_str = ""

	array = gen_random_int(number, seed)
	
	for i in array:	
		if array.index(i) == 0:
			array_str = array_str + str(i)
		else:
			array_str = array_str + "," + str(i)
	array_str = array_str + "."
	document.getElementById("generate").innerHTML = array_str

def sortnumber1():
	initial_array = document.getElementById("generate").innerHTML
	int_array = []
	array_str = ""
	for i in range(20):
		if i%2 == 0:
			int_array.append(int(initial_array[i]))
	n = len(int_array)
	swapped = True
	while swapped == True:
		swapped = False
		for small_index in range(1,n):
			if int_array[small_index-1] > int_array[small_index]:
				int_array[small_index-1], int_array[small_index] = int_array[small_index],int_array[small_index-1]
				new_n = small_index
				swapped = True
		n = new_n
	for i in int_array:	
		if int_array.index(i) == 0:
			array_str = array_str + str(i)
		else:
			array_str = array_str + "," + str(i)
	array_str = array_str + "."
	
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	# The following line get the value of the text input called "numbers"
	#1. Get the string from the text input stored in the variable value
	value = document.getElementsByName("Numbers")[0].value
	array_str = ""
	#1.a Consider if no value is given
	if  value == "":
		array_str = "naughty, naughty, better write some numbers in the textbox"
	else:
		# 2. Split the string using comma as a separator
		numbers = value.split(",")

		# 3. Remove all trailing whitespaces and convert them to an array of numbers
		# Example: numbers = ["1 , 2,  3,   4, 5,  6  ,7"], with .strip(), 
		# it becomes ["1,2,3,4,5,6,7"]
		# It's just in a for loop so that .strip runs through every element in numbers
		numbers = [float(num.strip()) for num in numbers]

		# 4. Sort the list of numbers
		n = len(numbers)
		swapped: bool = True
		while swapped:
			swapped = False
			new_n = 0 # Keeps track of how far it swapped last
			for inner_idx in range(1,n):
				if numbers[inner_idx - 1] > numbers[inner_idx]:
					numbers[inner_idx - 1], numbers[inner_idx] = numbers[inner_idx], numbers[inner_idx - 1]
					swapped = True
					new_n = inner_idx #records last swap
			n = new_n # Sets the new iteration limit

		# 5. Create a single string containing the sorted numbers and store it to array_str
		array_str = ", ".join(map(str, numbers))

    # Show the sorting process
	print("Sorting process: " + array_str)

	document.getElementById("sorted").innerHTML = array_str


