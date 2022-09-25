import matplotlib.pyplot as plt
data = open('1hz3_T310.run.25000000.energy.xvg').read()
data = data.split('\n')
Path = '/Users/shihchianglo/coding/comp-lab-class/Week2/Data/datasetof1hz3.txt'
f = open(Path, 'w')
for i in data:
    f.write(i+'\n')
f.close()