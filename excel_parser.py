'''
This module will read the excel document and create instances of nodes, edges to be passed to NetworkX
'''


import openpyxl as px
import numpy as np
import sys, os

from models import *

spreadsheet_format = {
	"name" : 1,
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
		
		if ws.cell(row=sheet_row, column=1) != None:
			
			obj = ClimateChangeActor(id=1, name=ws.cell(row=sheet_row, column=2).value)

		#print obj

		nodes.append( obj )

	edges = []

	return nodes, edges



