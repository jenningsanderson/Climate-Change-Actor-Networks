'''
A generic functions module
'''

import random

#Define the coordinates
def create_coord_array():
	coord_array = [[0 for i in range(10)] for j in range(10)]
	alphabet = ['a','b','c','d','e','f','g','h','i','j']

	for i in range(0,10):
		for j in range(0,10):
			coord_array[i][j] = str(i+1)+alphabet[j]

	return coord_array

def noise(i):
	return random.random()*i