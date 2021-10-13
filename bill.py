import pandas as pd
import os
df_main = pd.read_csv(os.getcwd()+'\\database.csv',index_col='id')

#Loop the whole program using while loop
x = 'y'
while x == 'y':
    total_cost = 0
    df = df_main.copy()


    #Getting input:
    no_of_items = int(input('Enter the no of items: '))
    for i in range(no_of_items):
            a = int(input('Enter item code: '))
            df.loc[a,'no_needed'] = int(input('Number needed:   '))


    #Modifying the dataframe according to our needs
    df['cost'] = df['price']*df['no_needed']
    df = df.dropna()
    s = df.loc[:,'cost']
    for d in range(s.shape[0]):
        total_cost = total_cost + df.iloc[d,3]


    #Decorations
    print('\n\n\n')
    print('\tAMMAN DEPARTMENTAL STORES')
    print('\t\tBILL')
    print('---------------------------------------')
    print(df)
    print('---------------------------------------')
    print('Total cost:\t\t\t ₹',total_cost)
    print('---------------------------------------')

    #Rerun the program?
    print('\n\n\n')
    x = input("Proceed to next bill? (Type 'y' for yes and 'n' for no): ")
    print('\n\n\n')
