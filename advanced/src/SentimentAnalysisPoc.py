# Each review is marked with a score of 0 for a negative sentiment or 1 for a positive sentiment.
# A model to predict the sentiment of a sentence.

import pandas as pd

filepath_dict = {'yelp': '/root/Documents/python_project_files/yelp_labelled.txt',
                 'amazon': '/root/Documents/python_project_files/amazon_cells_labelled.txt',
                 'imdb': '/root/Documents/python_project_files/imdb_labelled.txt'}

df_list = []
# print(filepath_dict.items())
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
    df['source'] = source  # Add another column filled with the source name
    # print(df)
    df_list.append(df)
    # print(df_list)
df = pd.concat(df_list)
print(df.iloc[0])
