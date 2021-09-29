import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:\\New folder(3)\\database.csv")
no_of_items = int(input('Enter the no of items: '))

for i in range(no_of_items):
	print(i)
