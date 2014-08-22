'''
Main runtime


'''

import excel_parser as ep
import networkx as nx
import matplotlib.pyplot as plt


#Point to the spreadsheet
file_path = r'/Users/jenningsanderson/Desktop/climate comms network august 8th.xlsx'

#Parse spreadsheet and return nodes, edges
[nodes, edges] = ep.parse_spreadsheet(file_path)

#Create the graph -- What type of graph should it be?
g = nx.DiGraph()

#Add nodes
for node in nodes[0:10]:
	g.add_node( node, attr_dict = node.__dict__ )


#Add edges
# for edge in edges:
	#unimplemented at this point


# Preview:

# nx.draw(g)
# plt.show()

#Write the GML?
nx.write_gml(g,"test.gml")