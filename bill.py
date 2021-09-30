import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("E:\\New folder(3)\\database.csv",index_col='id')

#After completing the whole program, remove the comment on the next 2 lines and move the whole code after that 1 tab space right
#a = 0
#while a != 0:

no_of_items = int(input('Enter the no of items: '))
df1 = pd.DataFrame()


for i in range(no_of_items):
	a = int(input('Enter item code: '))
	df.loc[a,'no_needed'] = int(input('Number needed: '))
	
print(df)
