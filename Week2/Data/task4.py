import matplotlib.pyplot as plt

data = open('1hz3_T310.run.25000000.energy.xvg').read()
data = data.split('\n')
'''
with open(r'dataofxvg.txt', 'w') as fp:
    for item in data:
        fp.write('%s\n' %item)
fp.close()
'''
newdata = data[data.index('@ s5 legend "Volume"')+1:]
newdata.pop()

time = []
potential = []
kinetic = []
total = []
temp = []
pressure = []
volume = []



for i in newdata:
    a = i.strip().split(' ')
    b = list(filter(None,a))
    
    time.append(float(b[0])/1000)
    potential.append(float(b[1]))
    kinetic.append(float(b[2]))
    total.append(float(b[3]))
    temp.append(float(b[4]))
    pressure.append(float(b[5]))
    volume.append(float(b[6]))

save_results_to = '/Users/shihchianglo/coding/comp-lab-class/Week2/assignments'
'''
plt.figure(1, figsize=(9, 6))
plt.plot(time,potential,label = 'Potential energy',color = 'red')
plt.xlabel('time (ns)')
plt.ylabel('Potential energy (kJ/mol)')
plt.savefig(save_results_to + '/potential energy.png')

plt.figure(2, figsize=(9, 6))
plt.plot(time,kinetic, label = 'Kinetic Energy',color = 'blue')
plt.xlabel('time (ns)')
plt.ylabel('Kinetic energy (kJ/mol)')
plt.savefig(save_results_to + '/kinetic energy.png')

plt.figure(3, figsize=(9, 6))
plt.plot(time,total, label = 'Total Energy',color = 'green')
#plt.ylim([-200000, 50000])
plt.xlabel('time (ns)')
plt.ylabel('Total energy (kJ/mol)')
#plt.legend(loc=(3/5,3/5))
#plt.title('Energy versus Time')
plt.savefig(save_results_to + '/total energy.png')

plt.figure(4, figsize=(9, 6))
plt.plot(time,temp, label = 'Temperature',color = 'orange')
plt.xlabel('time (ns)')
plt.ylabel('Temperature (K)')
plt.savefig(save_results_to + '/temperature.png')

plt.figure(5, figsize=(9, 6))
plt.plot(time,pressure, label = 'Pressure',color = 'purple')
plt.xlabel('time (ns)')
plt.ylabel('Pressure (bar)')
plt.savefig(save_results_to + '/pressure.png')

plt.figure(6, figsize=(9, 6))
plt.plot(time,volume, label = 'Volume',color = 'black')
plt.xlabel('time (ns)')
plt.ylabel('Volume (nm^3)')
plt.savefig(save_results_to + '/volume.png')
#plt.show()
'''
fig, ax = plt.subplots()

ax.plot(time, temp, label = 'Temperature',color = 'blue', alpha = 0.5)
plt.ylim([300, 330])
ax.set_xlabel('time (ns)')
ax.set_ylabel('Temperature (K)',color = 'blue')

ax2 = ax.twinx()
ax2.plot(time,kinetic,label = 'Kinetic energy',color = 'red', alpha = 0.5)
plt.ylim([34200, 36500])
ax2.set_ylabel('Kinetic energy (kJ/mol)',color = 'red')
plt.show()
