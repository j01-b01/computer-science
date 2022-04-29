#Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed. To do this, we will need the following steps:

#Define our function to accept a single input parameter lst which is a list of numbers
#Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
#Within the loop, if the first number in the list is even, then remove the first number of the list
#Once we hit an odd number or we run out of numbers, return the modified list

def delete_starting_evens(lst):
	while len(lst) >= 0:
		if lst[0] % 2 == 0:
			lst.remove(lst[0])
			if lst == []:
				return []
		else:
			return lst
	return lst




print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

