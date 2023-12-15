def print_multiplication_table(m):
    for i in range(1,11):
        x = i*m
        print(i, 'x', m, '=', x)


for z in range(1, 4):
    print(f"The multiplication table of {z}:, \n")
    print_multiplication_table(z)
    print('')


import numpy as np

# Replace 'prova.npz' with the actual filename you want to open
file_name = 'glm_hmm_raw_parameters_itr_0.npz'

# Load the npz file
data = np.load(file_name)

# Access the contents of the npz file
# For example, if the file contains arrays 'array1' and 'array2':
array1 = data['array1']
array2 = data['array2']

# Do something with the loaded data
# ...

# Close the npz file (optional, but recommended)
data.close()
