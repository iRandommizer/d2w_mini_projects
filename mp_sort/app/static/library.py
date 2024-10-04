from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number:int, seed:int) ->list[int]:
	# 1. Set the seed for psuodo random functionality
	random.seed(seed)
	myarray = []
	# 2. Produce a whole list of numbers depending on "number" arguement
	for k in range(number):
		myarray.append(k)
	# 3. Shuffle the array so that it is disordered 
	random.shuffle(myarray)
	return myarray		

def generate():
	number = 10
	seed = 200

	array = []
	array_str = ""

	# Produce disorded array of numbers
	array = gen_random_int(number, seed)
	
	# Turns the numbers into string and joins them together for the string ouput
	for i in array:	
		if array.index(i) == 0:
			array_str = array_str + str(i)
		else:
			array_str = array_str + "," + str(i)
	array_str = array_str + "."
	# Displays the string output of the randomly shuffled array of numbers
	document.getElementById("generate").innerHTML = array_str

def sortnumber1():
	# Get's the data from the html element
	initial_array = document.getElementById("generate").innerHTML
	int_array = []
	array_str = ""


	for i in range(20):
		if i%2 == 0:
			int_array.append(int(initial_array[i]))

	# Bubble Sort
	n = len(int_array)
	swapped = True
	while swapped == True:
		swapped = False
		new_n = 0 
		for small_index in range(1,n):
			if int_array[small_index-1] > int_array[small_index]:
				int_array[small_index-1], int_array[small_index] = int_array[small_index],int_array[small_index-1]
				new_n = small_index
				swapped = True
		n = new_n

	# Turns the numbers into string and joins them together for the string ouput
	for i in int_array:	
		if int_array.index(i) == 0:
			array_str = array_str + str(i)
		else:
			array_str = array_str + "," + str(i)
	array_str = array_str + "."
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	#1. Get the string from the text input stored in the variable value
	value = document.getElementsByName("Numbers")[0].value
	array_str = ""
	#1.a. Consider if no value is given
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
		n = len(array)
		for outer_index in range(1,n):
			inner_index = outer_index
			temp = array[inner_index] # This is so that it doesn't have keep swapping until it finally reaches it's right order in the array 
			while inner_index > 0 and temp < array[inner_index - 1]:        
				array[inner_index] = array[inner_index - 1]
				inner_index -= 1
			array[inner_index] = temp

		# 5. Create a single string containing the sorted numbers and store it to array_str
		# map runs the str() function for every iteration of numbers, hence 1 -> "1"
		# join() concatinates the separate string results in map() into a single string
		# ", " ensures that there is a comma and a space between each string results as it's being joined
		array_str = ", ".join(map(str, numbers))

    # Show the sorting process
	print("Sorting process: " + array_str)

	document.getElementById("sorted").innerHTML = array_str


