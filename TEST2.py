import pandas as pd
import os
import tqdm
from matplotlib import pyplot as plt
file = pd.read_csv('файл 2.csv', '\t')
file['check'] = file[['jud', 'cjud']].apply(lambda x: ''.join(map(str, x)), axis= 1)
file = file[['uid', 'docid', 'check']]
uniAssesor = file.uid.unique()
print(len(uniAssesor))
if not os.path.isfile('dftst2.txt'):
    uniAssesor = file.uid.unique()
    listcount = []
    listprcnt = []
    listSuccess = []
    for i in uniAssesor:
        count = 0
        porcent = file.groupby('uid')
        porcent = porcent.get_group(i)
        countt = len(porcent.index)
        listcount.append(countt)
        a = porcent.groupby(porcent.check.tolist()).size().reset_index().rename(columns={0:'count'})
        summ = a.at[0, 'count']+a.at[3, 'count']
        listSuccess.append(summ)
        summ = summ / len(porcent.index)
        summ = f"%.3f" % summ
        listprcnt.append(summ)
    data = {'uid': uniAssesor, 'amountTasks': listcount, 'successAnsw': listSuccess, 'rightAnswers': listprcnt}
    dftst2 = pd.DataFrame(data)
    dftst2.to_csv('dftst2.txt', sep='\t', header=True)

file2 = pd.read_csv('dftst2.txt', '\t')
file2 = file2[['uid', 'amountTasks', 'successAnsw', 'rightAnswers']]
print(file2.head)
print(file2[file2.rightAnswers == file2.rightAnswers.min()])
print(file2[file2.amountTasks == file2.amountTasks.min()])
print(file2[file2.successAnsw == file2.successAnsw.min()])
histogram = file2['rightAnswers'].plot(kind='hist', bins=600)
plt.show()
histogram2 = file2['amountTasks'].plot(kind='hist', bins=600)
plt.show()
histogram3 = file2['successAnsw'].plot(kind='hist', bins=600)
plt.show()
'''Худшие исполнители: ассесор 56 и ассесор 234'''








