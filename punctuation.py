import pandas as pd
# removing punctuation
df_table = {'Name':['meysam','ainaz','ronika'],
            'Text':['Hi Dear, Sir,I hope. ever ,thing going on well','Hi dear, Mr.kevin,I wish the. best for you','the flight, will do .10 min ,later']}
df = pd.DataFrame(df_table)
df['Text'] = df['Text'].apply(lambda x:''.join(x.upper() for x in x.split()))
df['Text'] = df['Text'].str.replace('[^\w\s]','')