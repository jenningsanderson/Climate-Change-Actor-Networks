'''
This module will read the excel document and create instances of nodes, edges to be passed to NetworkX
'''


import openpyxl as px
import numpy as np
import sys, os

from models import *

#
node_format = {
	'name' 		: 2,
	'id'		: 1,
	'discourse'	: 3,
	'type'		: 4,
	'type_no'	: 5,
	'location'	: 8
}

edge_format = {
	'from_id'	: 1,
	'to_id'		: 2,
	'weight'	: 3,
}


def parse_spreadsheet(file_path):
	#Open the file for reading
	wb = px.load_workbook(filename = file_path)
	
	#This is the node sheet
	ws1 = wb.get_sheet_by_name(wb.get_sheet_names()[0])

	nodes = []

	for sheet_row in range(2,ws1.max_row):
	# for sheet_row in range(1,10):	
		
		if ws1.cell(row=sheet_row, column=1) != None: #If no id, don't parse

			#Collect values
			name 	 = ws1.cell(row=sheet_row, column=node_format['name']).value
			obj_id   = ws1.cell(row=sheet_row, column=node_format['id']).value
			obj_type = ws1.cell(row=sheet_row, column=node_format['type']).value
			type_no  = ws1.cell(row=sheet_row, column=node_format['type_no']).value
			discourse= ws1.cell(row=sheet_row, column=node_format['discourse']).value
			location = ws1.cell(row=sheet_row, column=node_format['location']).value
			
			obj = ClimateChangeActor(id=obj_id, name=name)


			obj.add_attributes(	type   		= obj_type, 
								type_no		= type_no, 
								discourse	= discourse,
								location 	= location)

			#Conditionally set other values such as Alexa Web Ranking

		nodes.append( obj )


	#Now add edges

	ws2 = wb.get_sheet_by_name(wb.get_sheet_names()[1])
	
	edges = []

	for sheet_row in range(2,ws2.max_row):
		if ws2.cell(row=sheet_row, column=1) != None: #If no id, don't parse
		
			from_id  = ws2.cell(row=sheet_row, column=edge_format['from_id']).value
			to_id    = ws2.cell(row=sheet_row, column=edge_format['to_id']).value

			edge_obj = ActorRelation(from_id=from_id, to_id=to_id)

			edges.append(edge_obj)

	return nodes, edges



