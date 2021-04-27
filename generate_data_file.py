#!/usr/bin.env python3

"""Fill in/ Edit the variables and run to save the hand measurement tables as a numpy
array that can be easily imported to generate volumes

Author: Nuha Nishat"""


import numpy as np

"""Only change the variables within the dashed lines below"""

#--------------------------------------------------------------------------#

# Enter the hand model here
hand_model = "Model_O_Cylindrical"

# Enter/edit all the precision grasp measurements here
prec_abs_span = 25.3
prec_abs_depth = 2.3
prec_max_span = 20.5
prec_max_depth = 4.2
prec_int_span = 10.25
prec_int_depth = 10.3
prec_min_span = 0
prec_min_depth = 9.8


# Enter/edit all the power measurements here
pow_max_span_distal = 16.2
pow_max_depth_distal = 4.6
pow_int_span_distal = 6.3
pow_int_depth_distal = 9.9
pow_min_span_distal = 0
pow_min_depth_distal = 5.8

pow_max_span_mid = 16.7
pow_max_depth_mid = 3
pow_int_span_mid = 7.8
pow_int_depth_mid = 7.7
pow_min_span_mid = 3.6
pow_min_depth_mid = 5.6

pow_max_span_base = 5.2
pow_max_depth_base = 1.1
pow_int_span_base = 5.2
pow_int_depth_base = 1.1
pow_min_span_base = 5.2
pow_min_depth_base = 1.1

#-----------------------------------------------------------------------------#


"""Create numpy arrays and fill them in. The have the exact same format as the
tables in the results section. Only edit the variables over the line. """


precision = np.zeros((4, 2))

power = np.zeros((3, 6))


precision[0, 0] = prec_abs_span
precision[1, 0] = prec_max_span
precision[2, 0] = prec_int_span
precision[3, 0] = prec_min_span


precision[0, 1] = prec_abs_depth
precision[1, 1] = prec_max_depth
precision[2, 1] = prec_int_depth
precision[3, 1] = prec_min_depth


power[0, 0] = pow_max_span_distal
power[0, 1] = pow_max_depth_distal
power[0, 2] = pow_max_span_mid 
power[0, 3] = pow_max_depth_mid
power[0, 4] = pow_max_span_base
power[0, 5] = pow_max_depth_base
power[1, 0] = pow_int_span_distal
power[1, 1] = pow_int_depth_distal
power[1, 2] = pow_int_span_mid
power[1, 3] = pow_int_depth_mid
power[1, 4] = pow_max_span_base
power[1, 5] = pow_max_depth_base
power[2, 0] = pow_min_span_distal
power[2, 1] = pow_min_depth_distal
power[2, 2] = pow_min_span_mid
power[2, 3] = pow_min_depth_mid
power[2, 4] = pow_min_span_base
power[2, 5] = pow_min_depth_base

print("Power: ", power)
print("Precision: ", precision)

# Save in the Data folder

np.save("Data/"+hand_model+"_precision.npy", precision)
np.save("Data/"+hand_model+"_power.npy", power)

print(".npy files written!")


