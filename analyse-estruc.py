# This is a Jupyter Notebook command to install Biopython

from Bio.PDB import PDBParser

parser = PDBParser()

structure = parser.get_structure("My_Protein", "8WJG.pdb")

for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                print(atom.name, atom.coord)

import pymol
from pymol import cmd

pymol.finish_launching()

cmd.load("example.pdb", "my_protein")
cmd.show("cartoon", "my_protein")
cmd.color("red", "my_protein and name C*")
cmd.zoom("my_protein")
cmd.png("my_protein_view.png")