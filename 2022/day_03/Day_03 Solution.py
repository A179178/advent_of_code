## Day 3 Solution

### Import packages
import pandas as pd
import numpy as np

### Import input file
with open ('U:\Test\input_day3.txt', 'r') as input_file:
        input_raw = input_file.read().splitlines()

### Part 1:
### Split input to half and half
len_list=[]
first = []
second = []
for i in range(len(input_raw)):
    len_list.append(len(input_raw[i]))
    first.append(input_raw[i][0:int(len_list[i]/2)])
    second.append(input_raw[i][int(len_list[i]/2):len_list[i]])

### Find the overlap between first part and second part
inter_list = []
for i in range(len(input_raw)):
    inter_list.append(list(set(first[i]) & set(second[i])))

### Create a data frame for input and overlap
input_df = pd.DataFrame(data = input_raw, columns = ['input'])
inter_df = pd.DataFrame(data = inter_list, columns = ['inter'])
df = pd.concat([input_df,inter_df],axis=1)

### Create a list of lower & upper alphabat and corresponding values
### Then create a map 
alpha_list = []
value_list = []
for i in range(97,123):
    alpha_list.append(chr(i))
    value_list.append(i - 96)
    
for i in range(65,91):
    alpha_list.append(chr(i))
    value_list.append(i - 38)

alpha_map = dict(zip(alpha_list,value_list))

### Apply the map on overlaps to append corresponding values
inter_value = []
for inter in df['inter']:
    inter_value.append(alpha_map[inter])

### Merge the overlap values to df and calculate the sum of the priorities
inter_value_df = pd.DataFrame(data = inter_value, columns = ['value'])
df = pd.concat([input_df,inter_df,inter_value_df],axis=1)
df['value'].sum()

### Part 2:
### Create three list to store rucksack of each group
list1 = []
list2 = []
list3 = []

for i in range(2,len(input_raw),3):
    list1.append(input_raw[i-2])
    list2.append(input_raw[i-1])
    list3.append(input_raw[i])

### Find overlap between three elves of each group
inter_list2 = []
for i in range(len(list1)):
    inter_list2.append(list(set(list1[i]) & set(list2[i]) & set(list3[i])))
list1_df = pd.DataFrame(data = list1, columns = ['elf1'])
list2_df = pd.DataFrame(data = list2, columns = ['elf2'])
list3_df = pd.DataFrame(data = list3, columns = ['elf3'])
inter_df2 = pd.DataFrame(data = inter_list2, columns = ['inter'])
df2 = pd.concat([list1_df,list2_df,list3_df,inter_df2],axis=1)

### Apply the map on overlaps to append corresponding values
inter_value2 = []
for inter in df2['inter']:
    inter_value2.append(alpha_map[inter])

### Merge the overlap values to df and calculate the sum of the priorities
inter_value2_df = pd.DataFrame(data = inter_value2, columns = ['value'])
df2 = pd.concat([list1_df,list2_df,list3_df,inter_df2,inter_value2_df],axis=1)
df2['value'].sum()