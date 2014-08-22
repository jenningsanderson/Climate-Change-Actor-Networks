
import excel_parser as ep
import networkx as nx
import matplotlib.pyplot as plt



file_path = r'/Users/jenningsanderson/Desktop/climate comms network august 8th.xlsx'

[nodes, edges] = ep.parse_spreadsheet(file_path)


g = nx.DiGraph()

for node in nodes[0:10]:
	g.add_node( node, attr_dict = node.__dict__ )



# Preview:

# nx.draw(g)
# plt.show()

#Write the GML?
nx.write_gml(g,"test.gml")