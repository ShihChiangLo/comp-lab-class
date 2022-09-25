import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt

t = md.load('1UBQ_processed.pdb')

hydrobondcount = 0
hbonds = md.baker_hubbard(t, periodic=False)
print(hbonds)
label = lambda hbond : '%s -- %s' % (t.topology.atom(hbond[0]), t.topology.atom(hbond[2]))
print(label)
for hbond in hbonds:
    print(label(hbond))
    hydrobondcount += 1
print('Number of Hydrogen Bonds: ', hydrobondcount)

protein_sell = t.topology.select('protein')
t2 = t.atom_slice(protein_sell)
print("Number of atoms in the protein: ", t2.n_atoms)
print("Number of residues in the protein: ", t2.n_residues)
toplogy = t2.topology
print(toplogy)
print('all residues in the protein:%s' %[ residue for residue in t2.topology.residues])

res = toplogy.residue(0)
print('residue 0: %s' %res.name)
resnumber = 0
for i in toplogy.residues:
    if i.name == 'GLU' or i.name == 'ALA' or i.name =="LEU" or i.name == 'MET':
        resnumber = resnumber + 1
    
print('number of GLU,ALA,LEU,MET residues: %s' %resnumber)

Path = '/Users/shihchianglo/coding/comp-lab-class/Week2/assignments/Q5/outputforQ5.txt'
f = open(Path, 'w')
f.write('Number of Hydrogen Bonds: '+ str(hydrobondcount)+'\n')
f.write('Number of helical amino acids(Glu, Ala, Leu, Met) in the protein: '+ str(resnumber))
f.close()
