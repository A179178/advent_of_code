## Day 4 Solution
### Part 1

### Import packages
import numpy as np
import pandas as pd

### Import input file
input_file = np.loadtxt('U:\Test\Input_day4.txt', dtype='str', delimiter = ",", unpack=True)
elf1, elf2 = input_file[::]
print(elf1[0:5], elf2[0:5])

### Obtain lower bound and upper bound for each elf
elf1_min = []
elf1_max = []
elf2_min = []
elf2_max = []
for i in range(len(elf1)):
    elf1_min.append(elf1[i].split('-')[0])
    elf1_max.append(elf1[i].split('-')[1])
    elf2_min.append(elf2[i].split('-')[0])
    elf2_max.append(elf2[i].split('-')[1])
print(elf1_min[0:5], elf1_max[0:5], elf2_min[0:5], elf2_max[0:5])

elf1_min_num = list(map(int,elf1_min))
elf1_max_num = list(map(int,elf1_max))
elf2_min_num = list(map(int,elf2_min))
elf2_max_num = list(map(int,elf2_max))
print(elf1_min_num[0:5],elf1_max_num[0:5],elf2_min_num[0:5],elf2_max_num[0:5])

elf1_min_df = pd.DataFrame(data = elf1_min_num, columns = ['elf1_min'])
elf1_max_df = pd.DataFrame(data = elf1_max_num, columns = ['elf1_max'])
elf2_min_df = pd.DataFrame(data = elf2_min_num, columns = ['elf2_min'])
elf2_max_df = pd.DataFrame(data = elf2_max_num, columns = ['elf2_max'])
df = pd.concat([elf1_min_df,elf1_max_df,elf2_min_df,elf2_max_df],axis=1)
df.head()

### write down the rule of fully contain
conditionlist = [
    (
        ((df['elf1_min'] <= df['elf2_min']) & (df['elf1_max'] >= df['elf2_max']))
        |
        ((df['elf1_min'] >= df['elf2_min']) & (df['elf1_max'] <= df['elf2_max']))
        
    )
]

resultlist = [1]

df['fully_contain'] = np.select(conditionlist, resultlist, default=0)
df['fully_contain'].sum()

### Part 2
### write down the rule of no overlap at atll
conditionlist2 = [
    (
        (df['elf1_max'] < df['elf2_min'])
        |
        (df['elf1_min'] > df['elf2_max'])
        
    )
]

resultlist2 = [1]
df['non_overlap'] = np.select(conditionlist2, resultlist2, default=0)
sum(df['non_overlap'] == 0)