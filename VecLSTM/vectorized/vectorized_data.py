;==========================================
; Title: Create a vector representation
; Author: anonymous 
;========================================== 

# This function takes the latitude (lat), longitude (lon), and time (time) columns 
# transforms them into a format suitable for further processing
# input into a machine learning model
# The resulting vectorized_data variable holds these transformed vector representations of the original geographical and temporal data points

vectorized_data = create_vector_representation(dfv['lat'], dfv['lon'], dfv['time'])
