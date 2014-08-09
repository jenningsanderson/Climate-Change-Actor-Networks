'''
This module will read the excel document and create instances of nodes, edges to be passed to NetworkX
'''


import openpyxl as px
import numpy as np


'''
Nodes will be instances of this class, specific metrics and methods can be defined 
here to create node attributes.

Hopefully NetworkX will accept nodes as instances of these classes? Hopefully...
'''

class ClimateChangeActor:

	def __init__(self, name):
		self.id = 
		self.name = name


class ActorRelation:

	def __init__(self, from_id, to_id):

		self.from_id = from_id
		self.to_id = to_id

