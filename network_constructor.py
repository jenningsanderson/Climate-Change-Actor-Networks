'''
Main runtime

'''

import excel_parser as ep
import networkx as nx
import matplotlib.pyplot as plt

from functions import *


#Point to the spreadsheet
#file_path = r'/Users/jenningsanderson/Desktop/climate comms network august 8th.xlsx'
file_path = r'climate_change_comms_network_final.xlsx'

limit = 206

#Parse spreadsheet and return nodes, edges
[nodes, edges] = ep.parse_spreadsheet(file_path, limit)

#Create Position Matrix
positions = create_coord_array()

for row in positions:
	for col in row:
		print col,
	print "\n"

#Process the nodes
for node in nodes:
	node.set_label()
	node.process_positions(positions)
	print node.label, node.position, node.long, node.lat
	node.cleanup()


#Create the graph -- What type of graph should it be?
g = nx.Graph()

#Add nodes
for node in nodes:
	g.add_node( node.label, attr_dict = node.__dict__ )



# Quick & dirty Preview:
# nx.draw(g)
# plt.show()

#Write the GML?
nx.write_gml(g,"ClimateChangeActors.gml")