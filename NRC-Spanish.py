import pandas as pd
import numpy as np
from googletrans import Translator


df = pd.read_csv("NRC-Lexicon.txt", 
	error_bad_lines=False, sep='\t')

count_row = df.shape[0]  # gives number of row count
count_col = df.shape[1]  # gives number of col count

print(count_row)

for col in df.columns:
	print(col)

df['term_count'] = df['term'].str.len()
df['affec_count'] = df['AffectDimension'].str.len()
df['score_count'] = 5
df['total_count'] = df['term_count'] + df['score_count'] + df['affec_count']




total = df['total_count'].sum()
print(total)

#for item in df['term']:
#    print(item)

#make new column with translated info

translator = Translator()
traducciones = []

for item in df['term']:

	translations = translator.translate(str(item), dest='es')
	
	traducciones.append(translations)

df['terminos'] = traducciones


traducciones_1 = []

for item in df['AffectDimension']:

	translations = translator.translate(str(item), dest='es')
	
	traducciones_1.append(translations)

df['sentimientos'] = traducciones_1



data_top = df.head()
	
# display
print(data_top)

df.to_csv(r'NRC-Lexicon-Spanich.csv', index = None, header = True)



