'''
This module will read the excel document and create instances of nodes, edges to be passed to NetworkX
'''


import openpyxl as px
import numpy as np
import sys, os

from models import *


def parse_spreadsheet(file_path):
	#Open the file for reading
	wb = px.load_workbook(filename = file_path)
	ws = wb.get_sheet_by_name(wb.get_sheet_names()[0])

	#Iterate through the first sheet:
	# for row in 

	nodes = []

	# for sheet_row in range(0,ws.max_row):
	for sheet_row in range(1,10):	
		
		if ws.cell(row=sheet_row, column=1) != None:
			obj = ClimateChangeActor(name=ws.cell(row=sheet_row, column=1), id=0)

		#print obj

		nodes.append( obj )

	edges = []

	return nodes, edges



