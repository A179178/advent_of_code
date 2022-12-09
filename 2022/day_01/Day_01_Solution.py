
# coding: utf-8
## Day 1 Solution

### Import packages
import pandas as pd
import numpy as np


### Import Input file 
with open ('U:\Test\Input.txt', 'r') as input_file:
        input_raw = input_file.read().splitlines()

input_raw[0:20]


## Replace '' with '0'
for i in range(len(input_raw)):
    if input_raw[i]=='':
        input_raw[i]='0'


## Change elements datatype to int
input_raw2 = list(map(int, input_raw))
input_raw2[0:20]

##breaks_ind = [i for i in range(len(input_raw)) if input_raw[i] == '0']

## Another way to find ind of breaks
## breaks_ind=[]
## for i in range(len(input_raw)):
    ## if input_raw[i]=='':
        ## breaks_ind.append(i)   

## Assign elf
elf = []
n = 1
for i in range(len(input_raw2)):
    if input_raw2[i] !=0:
        elf.append('Elf' + str(n))
    else:
        elf.append('Break')
        n = n +1       

elf[0:20]
print(len(input_raw2),len(elf))

## Merge calories and elf together
input_raw_df = pd.DataFrame(data = input_raw2, columns = ['calories'])
elf_df = pd.DataFrame(data = elf, columns = ['elf'])
df = pd.concat([input_raw_df,elf_df],axis=1)

## Calculate total calories of each elf
df['tot_calories'] = df.groupby(['elf'])['calories'].transform('sum')

## Calculate the max total calories 
df_max = df['tot_calories'].max()

## Find which elf carries the most calories
max_elf = df['elf'][df['tot_calories']==74394].unique()

## This elf carries how many calories respectively 
max_elf_calories = df['calories'][df['tot_calories']==df_max].unique()

## Print results
print('The', +max_elf, 'carries the most calories. \n This elf carries', +max_elf_calories, '.\n', 'Total calories is', +df_max)

