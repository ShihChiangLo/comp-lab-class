from turtle import distance
import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt

# Load the trajectory
traj = md.load('1hz3_T310.stepid25000000.every100ps.nowater.xtc', top='1hz3_T310.start.nowater.gro')
print(traj)

# Load the topology
top = traj.topology
#print(top.atom(0))
#print(top.atom(407))
#print(md.compute_distances(traj, [[0, 407]]))

distancebetweenatom = []
for i in md.compute_distances(traj, [[0, 407]]):
    distancebetweenatom.append(i[0])
#print(distancebetweenatom)

#print(md.compute_rg(traj))
#plot the radius of gyration and the distance of end2end of the protein
plt.plot(distancebetweenatom, label = 'End to end distance',color = 'orange')
plt.plot(md.compute_rg(traj), label = 'Radius of gyration',color = 'blue')
#plt.plot(distancebetweenatom, label = 'Distance',color = 'orange')
plt.legend()
plt.xlabel('frame')
plt.ylabel('Distance (nm)')

# plot the histogram of the normalized distance of end2end and the radius of gyration
normalized_distancebetweenatom = []
frame=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
plt.figure(2, figsize=(9, 6))
for i in distancebetweenatom:
    normalized_distancebetweenatom.append((i-min(distancebetweenatom))/(max(distancebetweenatom)-min(distancebetweenatom)))
print(normalized_distancebetweenatom)
n, bins, edges =plt.hist(normalized_distancebetweenatom, label = 'End to end distance',color = 'orange')
plt.title('Histogram of the normalized distance of end2end')
plt.xlabel('Normalized distance')
plt.xticks(bins)
plt.ylabel('Counts')

normalized_radiusofgyration = []
plt.figure(3, figsize=(9, 6))
gyration = md.compute_rg(traj)
for i in gyration:
    normalized_radiusofgyration.append((i-min(gyration))/(max(gyration)-min(gyration)))
print(normalized_radiusofgyration)
n2, bins2, edges2 = plt.hist(normalized_radiusofgyration, label = 'Radius of gyration',color = 'blue')
plt.title('Histogram of the normalized radius of gyration')
plt.xlabel('Normalized radius of gyration')
plt.xticks(bins2)
plt.ylabel('Counts')
#plt.bar(frame,normalized_distancebetweenatom, label = 'End to end distance',color = 'orange')
plt.show()




# print all residues
#print('All residues: %s' % [residue for residue in top.residues])





