'''
This module will read the excel document and create instances of nodes, edges to be passed to NetworkX
'''


import openpyxl as px
import numpy as np
import sys, os

from models import *

format = {
	'name' 		: 2,
	'id'		: 1,
	'discourse'	: 3,
	'type'		: 4,
	'type_no'	: 5,
	'location'	: 8
}


def parse_spreadsheet(file_path):
	#Open the file for reading
	wb = px.load_workbook(filename = file_path)
	ws = wb.get_sheet_by_name(wb.get_sheet_names()[0])

	#Iterate through the first sheet:
	# for row in 

	nodes = []

	for sheet_row in range(2,ws.max_row):
	# for sheet_row in range(1,10):	
		
		if ws.cell(row=sheet_row, column=1) != None: #If no id, don't parse

			#Collect values
			name = ws.cell(row=sheet_row, column=format['name']).value
			obj_id   = ws.cell(row=sheet_row, column=format['id']).value
			obj_type = ws.cell(row=sheet_row, column=format['type']).value
			type_no  = ws.cell(row=sheet_row, column=format['type_no']).value
			discourse= ws.cell(row=sheet_row, column=format['discourse']).value
			location = ws.cell(row=sheet_row, column=format['location']).value
			
			obj = ClimateChangeActor(id=obj_id, name=name)


			obj.add_attributes(	type   		= obj_type, 
								type_no		= type_no, 
								discourse	= discourse,
								location 	= location)


			#Conditionally set other values such as Alexa Web Ranking

		nodes.append( obj )

	edges = []

	return nodes, edges



