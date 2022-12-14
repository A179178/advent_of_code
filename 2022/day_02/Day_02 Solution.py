
## Day 2 Solution

### Import packages
import pandas as pd
import numpy as np

### Import Input file 
input_file = np.loadtxt('U:\Test\Input_day2.txt', dtype='str', delimiter = " ", unpack=True)
opponent, response = input_file[::]

## Part 1

### create dataframe for opponent and my response
opponent_df = pd.DataFrame(data = opponent, columns = ['opponent'])
response_df = pd.DataFrame(data = response, columns = ['response'])
df = pd.concat([opponent_df,response_df],axis=1)


### create a column to indicate the score I could get based on the shape I choose
response_score_map = {'X' : 1, 'Y' : 2, 'Z' : 3}
df['response_score'] = df['response'].map(response_score_map)


### write down the game rule and socres I could get of each result
conditionlist = [
    (
        ((df['opponent'] == 'A') & (df['response'] == 'Y'))
        |
        ((df['opponent'] == 'B') & (df['response'] == 'Z'))
        |
        ((df['opponent'] == 'C') & (df['response'] == 'X'))
    ),
    (
        ((df['opponent'] == 'A') & (df['response'] =='X'))
        |
        ((df['opponent'] == 'B') & (df['response'] == 'Y'))
        |
        ((df['opponent'] == 'C') & (df['response'] == 'Z'))
    ),
    (
        ((df['opponent'] == 'A') & (df['response'] == 'Z'))
        |
        ((df['opponent'] == 'B') & (df['response'] == 'X'))
        |
        ((df['opponent'] == 'C') & (df['response'] == 'Y'))
    )
]

resultlist = [6,3,0]


### create a column to indicate the socre I could get based on the results
df['result_score'] = np.select(conditionlist, resultlist, default=0)


### create a column to get add up scores of shape and scores from results
df['total_score'] = df['response_score'] + df['result_score']


### get final total score
final_score = df['total_score'].sum()
print('If everything goes exactly according to the strategy guide, my total score would be', +final_score)

## Part 2
result_df = pd.DataFrame(data = response, columns = ['result'])
df2 = pd.concat([opponent_df,result_df],axis=1)

### create a column to indicate the score I could get based on results
result_score_map = {'X' : 0, 'Y' : 3, 'Z' : 6}
df2['result_score'] = df2['result'].map(result_score_map)


### write down the game rule and socres I could get of each shape
conditionlist2 = [
    (
        ((df2['opponent'] == 'A') & (df2['result'] == 'Y'))
        |
        ((df2['opponent'] == 'B') & (df2['result'] == 'X'))
        |
        ((df2['opponent'] == 'C') & (df2['result'] == 'Z'))
    ),
    (
        ((df2['opponent'] == 'A') & (df2['result'] =='Z'))
        |
        ((df2['opponent'] == 'B') & (df2['result'] == 'Y'))
        |
        ((df2['opponent'] == 'C') & (df2['result'] == 'X'))
    ),
    (
        ((df2['opponent'] == 'A') & (df2['result'] == 'X'))
        |
        ((df2['opponent'] == 'B') & (df2['result'] == 'Z'))
        |
        ((df2['opponent'] == 'C') & (df2['result'] == 'Y'))
    )
]

responselist = [1,2,3]

### create a column to indicate the socre I could get based on the response
df2['response_score'] = np.select(conditionlist2, responselist, default=0)


### create a column to get add up scores of shape and scores from results
df2['total_score'] = df2['response_score'] + df2['result_score']

### get final total score
final_score2 = df2['total_score'].sum()
print('If everything goes exactly according to the strategy guide, my total score would be', +final_score2)

