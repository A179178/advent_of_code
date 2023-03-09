## Day 8 Solution
### Part 1

### Import packages
import numpy as np
import pandas as pd
from itertools import islice
### Import input file
with open ('U:\Test\Input_day8.txt', 'r') as input_file:
        input_raw0 = input_file.read().splitlines()
edge = len(input_raw0[0])*2 + len(input_raw0)*2 -4

### Create a list with indicators that indicate if tree is visible at row level
horizon_temp = []
for i in range(len(input_raw0)):
    for j in range(len(input_raw0)):
        if j==0 or j==len(input_raw0)-1:
            horizon_temp.append(1)
        elif j>0 and j<len(input_raw0)-2 and (max(input_raw0[i][0:j])<input_raw0[i][j] or max(input_raw0[i][j+1:len(input_raw0)-1])<input_raw0[i][j]):
            horizon_temp.append(1)
        elif j == len(input_raw0)-2 and (max(input_raw0[i][0:j])<input_raw0[i][j] or max(input_raw0[i][j+1])<input_raw0[i][j]):
            horizon_temp.append(1)
        else:
            horizon_temp.append(0)
length =[]
for i in range(len(input_raw0)):
    length.append(len(input_raw0))
    
horizon_temp_2 = iter(horizon_temp)
horizon_temp_3 = [list(islice(horizon_temp_2,el)) for el in length]
horizon_final = [i[0:] for i in horizon_temp_3]

### Transpose row to column and column to row
input_raw_t = [list(x) for x in zip(*input_raw0)]
input_raw_split = [sub.split() for sub1 in input_raw0 for sub in sub1]
input_raw_split_2 = iter(input_raw_split)
input_raw_split_3 = [list(islice(input_raw_split_2,el)) for el in length]
input_raw_split_final = [i[0:] for i in input_raw_split_3]
input_raw_t = [list(x) for x in zip(*input_raw_split_final)]


### Create a list with indicators that indicate if tree is visible at column level
vertical_temp = []
for i in range(len(input_raw_t)):
    for j in range(len(input_raw_t)):
        if j==0 or j==len(input_raw_t)-1:
            vertical_temp.append(1)
        elif j>0 and j<len(input_raw_t)-2 and (max(input_raw_t[i][0:j])<input_raw_t[i][j] or max(input_raw_t[i][j+1:len(input_raw_t)-1])<input_raw_t[i][j]):
            vertical_temp.append(1)
        elif j == len(input_raw_t)-2 and (max(input_raw_t[i][0:j])<input_raw_t[i][j] or input_raw_t[i][j+1]<input_raw_t[i][j]):
            vertical_temp.append(1)
        else:
            vertical_temp.append(0)
            
vertical_temp_2 = iter(vertical_temp)
vertical_temp_3 = [list(islice(vertical_temp_2,el)) for el in length]
vertical_temp_4 = [i[0:] for i in vertical_temp_3]

vertical_final = [list(x) for x in zip(*vertical_temp_4)]

visible_tree_cnt = 0
for i in range(len(input_raw0)):
    for j in range(len(input_raw0)):
        if horizon_final[i][j]==1 or vertical_final[i][j] ==1:
            visible_tree_cnt = visible_tree_cnt+1
print(visible_tree_cnt)