import csv
import numpy as np
import HSHH_math
import HSHH


def generate_atom_data(num_atoms):
    # Create data for each atom
    atom_data = []
    for _ in range (num_atoms):
        # Use the HSHH_math module to generate the atom vector
        atom_vector = HSHH_math.create_hypervector (HSHH_math.num_dimensions)
        atom_data.append ({
            'vector': atom_vector,
            'norm': np.linalg.norm (atom_vector)
        })

    return atom_data


# Get the number of atoms from the user
num_atoms = int (input ("Enter the number of atoms: "))

# Generate and print the atom data
atom_data = generate_atom_data (num_atoms)
for i, data in enumerate (atom_data):
    print (f"Atom {i + 1}:")
    print (f"  Vector: {data ['vector']}")
    print (f"  Norm: {data ['norm']}")

# Use the HSHH module to visualize the atoms
fig = HSHH.visualize_atoms (atom_data)

# Show the plot
fig.show ()

# Write the atom data to a CSV file
with open ('atom_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Atom', 'Vector', 'Norm']
    writer = csv.DictWriter (csvfile, fieldnames=fieldnames)

    writer.writeheader ()
    for i, data in enumerate (atom_data):
        writer.writerow ({'Atom': f"Atom {i + 1}", 'Vector': data ['vector'], 'Norm': data ['norm']})
