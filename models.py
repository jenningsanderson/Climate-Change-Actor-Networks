
'''
Nodes will be instances of this class, specific metrics and methods can be defined 
here to create node attributes.
'''

import networkx as nx

class ClimateChangeActor:

	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.label = name

	def add_attributes(self, discourse="NA", location="NA", type=None, type_no=-1):
		self.discourse = discourse
		self.location = location
		self.type = type
		self.type_no = type_no


	# def as_node(self):
	# 	return self.__dict__


class ActorRelation:

	def __init__(self, from_id, to_id):

		self.from_id = from_id
		self.to_id = to_id

