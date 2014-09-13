'''
The models module

'''

from math import *
from functions import *

class ClimateChangeActor:

	def __init__(self, name, location):
		self.name = name
		self.location = location
		self.lat = 0
		self.long = 0

	def add_attributes(self, type_no="NA", size="0", position=None):
		self.type_no  = str(type_no).encode('utf-8')
		self.size      = 11 - size
		self.position = position#.encode('utf-8')

	def set_label(self):
		if self.location != None:
			self.label = self.name + " - " + self.location
		else:
			self.label = self.name
		
	def process_positions(self, positions):
		self.raw_coords = self.find(positions,self.position)
		print "Raw Coords", self.raw_coords
		#Longitude Increase
		self.long = float((self.raw_coords[1])*18.8)
		self.long += noise(10)
		
		#Latitude Increase
		self.lat = float((self.raw_coords[0])*8.8)
		self.lat += noise(10)
		self.lat *= -1


	def find(self, l, elem):
		#http://stackoverflow.com/questions/6518291/using-index-on-multidimensional-lists
   		for row, i in enumerate(l):
			try:
				column = i.index(elem)
			except ValueError:
				continue
			return [row, column]
		return -1

	def cleanup(self):
		del self.position
		del self.name
		del self.location
		del self.raw_coords


class ActorRelation:

	def __init__(self, from_id, to_id):
		self.from_id = from_id
		self.to_id = to_id