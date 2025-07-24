#innner join with merge metho
'''here we can consider dataframe = table and merging = joining 
we have two dataset withb taxi_own and taxi_veh --> vid column is common on both table,
so we can merge using vid table by following code '''

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on = "vid")

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

#-----------------------------------------------------
# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the column names of taxi_own_veh
print(taxi_own_veh.columns)

'''This code will Set the left and right table suffixes for overlapping columns of the merge to _own and _veh, respectively.'''
#-----------------------------------------------------