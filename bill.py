import pandas as pd
import matplotlib.pyplot as plt

#After completing the whole program, remove the comment on the next 2 lines and move the whole code after that 1 tab space right
#a = 0
#while a != 0:

df = pd.read_csv("E:\\New folder(3)\\database.csv")
no_of_items = int(input('Enter the no of items: '))

for i in range(no_of_items):
	print(i)
