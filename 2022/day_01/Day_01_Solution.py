
# coding: utf-8

# In[7]:


## Day 1 Solution


# In[12]:


### Import packages
import pandas as pd
import numpy as np


# In[255]:


### Import Input file 
with open ('U:\Test\Input.txt', 'r') as input_file:
        input_raw = input_file.read().splitlines()


# In[256]:


input_raw[0:20]


# In[257]:


## Replace '' with '0'
for i in range(len(input_raw)):
    if input_raw[i]=='':
        input_raw[i]='0'


# In[258]:


## Change elements datatype to int
input_raw2 = list(map(int, input_raw))
input_raw2[0:20]


# In[184]:


##breaks_ind = [i for i in range(len(input_raw)) if input_raw[i] == '0']


# In[145]:


## Another way to find ind of breaks
## breaks_ind=[]
## for i in range(len(input_raw)):
    ## if input_raw[i]=='':
        ## breaks_ind.append(i)   


# In[275]:


## Assign group, one group represent one elf
elf = []
n = 1
for i in range(len(input_raw2)):
    if input_raw2[i] !=0:
        elf.append('Elf' + str(n))
    else:
        elf.append('Break')
        n = n +1       


# In[260]:


elf[0:20]
print(len(input_raw2),len(group))


# In[336]:


input_raw_df = pd.DataFrame(data = input_raw2, columns = ['calories'])
elf_df = pd.DataFrame(data = elf, columns = ['elf'])
df = pd.concat([input_raw_df,elf_df],axis=1)


# In[337]:


df['tot_calories'] = df.groupby(['elf'])['calories'].transform('sum')


# In[357]:


df_max = df['tot_calories'].max()


# In[358]:


print(df_max)


# In[373]:


max_elf = df['elf'][df['tot_calories']==74394].unique()


# In[374]:


print(max_elf)


# In[375]:


max_elf_calories = df['calories'][df['tot_calories']==74394].unique()


# In[376]:


print(max_elf_calories)


# In[377]:


print('The', +max_elf, 'carries the most calories. \n This elf carries', +max_elf_calories, '.\n', 'Total calories is', +df_max)

