## Day 6 Solution
### Part 1

### Import packages
import numpy as np
import pandas as pd

### Import input file
with open ('U:\Test\Input_day6.txt', 'r') as input_file:
        input_raw = input_file.read().splitlines()

### Put letters into individual elements
input_ls = list(''.join(input_raw))

### Put four letters into individual elements
input_ls2 = []
for i in range(0,(len(input_ls)-3)):
    input_ls2[i:i+4] = [''.join(input_ls[i:i+4])]
    
letter1 = []
letter2 = []
letter3 = []
letter4 = []
for i in range(0,(len(input_ls)-3)):
    letter1.append(input_ls[i])
    letter2.append(input_ls[i+1])
    letter3.append(input_ls[i+2])
    letter4.append(input_ls[i+3])

letter1_df = pd.DataFrame(data = letter1, columns = ['letter1'])
letter2_df = pd.DataFrame(data = letter2, columns = ['letter2'])
letter3_df = pd.DataFrame(data = letter3, columns = ['letter3'])
letter4_df = pd.DataFrame(data = letter4, columns = ['letter4'])
df = pd.concat([letter1_df,letter2_df,letter3_df,letter4_df],axis=1)

conditionlist = [
    (
        (df['letter1'] == df['letter2']) 
        |
        (df['letter1'] == df['letter3']) 
        |
        (df['letter1'] == df['letter4']) 
        |
        (df['letter2'] == df['letter3']) 
        |
        (df['letter2'] == df['letter4']) 
        |
        (df['letter3'] == df['letter4']) 
        
    )
]

resultlist = [1]
df['same'] = np.select(conditionlist, resultlist, default=0)

first_diff = df.index[df.same==0].min() +3
first_diff_letter = input_raw[0][first_diff]
print('The first marker after character')
print(first_diff)
print(first_diff_letter)

## Part 2
n = 14
lists = [[] for _ in range(n)]
for i in range(0,(len(input_ls)-13)):
    for j in range(n):
        lists[j].append(input_ls[i])
        i = i+1

letter1_df2 = pd.DataFrame(data = lists[0], columns = ['letter1'])
letter2_df2 = pd.DataFrame(data = lists[1], columns = ['letter2'])
letter3_df2 = pd.DataFrame(data = lists[2], columns = ['letter3'])
letter4_df2 = pd.DataFrame(data = lists[3], columns = ['letter4'])
letter5_df2 = pd.DataFrame(data = lists[4], columns = ['letter5'])
letter6_df2 = pd.DataFrame(data = lists[5], columns = ['letter6'])
letter7_df2 = pd.DataFrame(data = lists[6], columns = ['letter7'])
letter8_df2 = pd.DataFrame(data = lists[7], columns = ['letter8'])
letter9_df2 = pd.DataFrame(data = lists[8], columns = ['letter9'])
letter10_df2 = pd.DataFrame(data = lists[9], columns = ['letter10'])
letter11_df2 = pd.DataFrame(data = lists[10], columns = ['letter11'])
letter12_df2 = pd.DataFrame(data = lists[11], columns = ['letter12'])
letter13_df2 = pd.DataFrame(data = lists[12], columns = ['letter13'])
letter14_df2 = pd.DataFrame(data = lists[13], columns = ['letter14'])
df2 = pd.concat([letter1_df2,letter2_df2,letter3_df2,letter4_df2,
               letter5_df2,letter6_df2,letter7_df2,letter8_df2,
               letter9_df2,letter10_df2,letter11_df2,letter12_df2,
               letter13_df2,letter14_df2],axis=1)

# Find unique letter of each row
df2['same'] = df2.stack().groupby(level=0).apply(lambda x: x.unique().tolist())
# Find how many unique letters 
df2['length'] = df2['same'].str.len()

# The first marker will be the row where number of unique letters is 14
first_diff2 = df2.index[df2['length']==14].min() +13
first_diff_letter2 = input_raw[0][first_diff2]
print('The first marker after character')
print(first_diff2)
print(first_diff_letter2)

