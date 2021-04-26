#!/usr/bin/env python3

import numpy as np 
import csv

class HandVolume():
	def __init__(self, hand_name):
		self.hand_name = hand_name
		# Placeholder dictionary for holding grasp measurements
		self.precision = {"abs_span": 0, "abs_depth":0, "max_span": 0, "max_depth": 0, 
"int_span": 0, "int_depth": 0, "min_span": 0, "min_depth": 0}
		self.power = {"max_span_distal": 0, "max_depth_distal": 0, "max_span_mid": 0, "max_depth_mid": 0,
"max_span_base" : 0, "max_span_depth" : 0, "int_span_distal" :0, "int_depth_distal": 0, "int_span_mid" : 0,
"int_span_base": 0, "int_depth_base": 0, "min_span_distal": 0, "min_depth_distal": 0, "min_span_mid" :0, 
"min_depth_mid": 0, "min_span_base": 0, "min_span_depth": 0}
	

	def update_precision(self, table):
		"""Update the precision grasp measurements
		:param: The precision measurement table in a 2X4 matrix form"""
		self.precision["abs_span"] = table[0,0]
		self.precision["abs_depth"] = table[0, 1]
		self.precision["max_span"] = table[1, 0]
		self.precision["max_depth"] = table[1, 1]
		self.precision["int_span"] = table[2, 0]
		self.precision["int_depth"] = table[2, 1]
		self.precision["min_span"] = table[3, 0]
		self.precision["min_depth"] = table[3, 1]
		

	def update_power(self, table_matrix):
		"""Update the power grasp measurements"""
		pass


if __name__ == '__main__':
	# Model O Cylindrical Precision measurements

	precision_table = np.zeros((4, 2))
	precision_table[0, 0] = 25.3
	precision_table[0, 1] = 2.3
	precision_table[1, 0] = 20.5
	precision_table[1, 1] = 4.2 
	precision_table[2, 0] = 10.25
	precision_table[2, 1] = 10.3
	precision_table[3, 0] = 0
	precision_table[3, 1] = 9.8

	# Fill in values

	print("precision: ", precision_table)

	power_table = np.zeros((3,6))

	power_table[0, 0] = 16.2
	power_table[0, 1] = 4.6
	power_table[0, 2] = 16.7
	power_table[0, 3] = 3
	power_table[0, 4] = 5.2
	power_table[0, 5] = 1.1
	power_table[1, 0] = 6.3
	power_table[1, 1] = 9.9
	power_table[1, 2] = 7.8
	power_table[1, 3] = 7.7
	power_table[1, 4] = 5.2
	power_table[1, 5] = 1.1
	power_table[2, 0] = 0
	power_table[2, 1] = 5.8
	power_table[2, 2] = 3.6
	power_table[2, 3] = 5.6
	power_table[2, 4] = 5.2
	power_table[2, 5] = 1.1

	print("Power: ", power_table)

	# Save matrices for importing later

	# Create hand volume object
	model_o_cyl = HandVolume("Model_O_Cylindrical")

	model_o_cyl.update_precision(precision_table)

	print(model_o_cyl.precision)








