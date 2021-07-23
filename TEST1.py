import pandas as pd
from tqdm import tqdm
from matplotlib import pyplot as plt
import os
import numpy as np
import datetime
if not os.path.isfile('Seconds.txt'):
    file = pd.read_csv('файл 1.txt', '\t')
    assesor_0 = file[['login', 'Microtasks', 'assigned_ts', 'closed_ts']]
    file['Seconds'] = pd.to_datetime(assesor_0['closed_ts']) - pd.to_datetime(assesor_0['assigned_ts'])
    delta = file['Seconds']
    delta = delta / pd.to_numeric(assesor_0['Microtasks'])
    for i in tqdm(range(0, len(delta)), leave=False):
        delta[i] = delta[i].seconds
    file['Seconds'] = delta
    assesor = file[['login', 'Seconds']]
    assesor.to_csv('Seconds.txt', sep='\t', header=True)
else:
    file1 = pd.read_csv('Seconds.txt', '\t')
    file1 = file1[['login', 'Seconds']]
f = file1.groupby('login')
f = f.get_group('login130')
print(f.head)
print(file1[file1.Seconds == file1.Seconds.max()])
f = file1.groupby('login')
f = f.get_group('login657')
if not os.path.isfile('mydf.txt'):
    a = file1.login.unique()
    listik = []
    for i in tqdm(a):
        assesor = file1.groupby('login')
        assesor = assesor.get_group(i)
        assesor = assesor.median()
        listik.append(float(assesor))

    data = {'login': a, 'medianSec': listik}
    mydf = pd.DataFrame(data)
    mydf.to_csv('mydf.txt', sep='\t', header=True)
else:
    file2 = pd.read_csv('mydf.txt', '\t')
    file2 = file2[['login', 'medianSec']]
    print(file2['medianSec'].head)
print(file2[file2.medianSec == file2.medianSec.min()])
print(file2[file2.medianSec == file2.medianSec.max()])
'''histogram = file1.plot(kind='hist', bins=767)
plt.show()'''





















