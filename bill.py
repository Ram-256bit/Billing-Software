import pandas as pd
import numpy as np
import os
df_main = pd.read_csv(os.getcwd()+'\\database.csv',index_col='id')

#Loop the whole program using while loop
x = ''
while x == '':
    x = ''                  #for looping the program
    total_cost = 0
    df = df_main.copy()
    df["Quantity"] = np.NaN   #creating a column called Quantity
    df['Quantity'].fillna(value=0,inplace=True)

    #Getting input:
    no_of_items = int(input('Enter the no of items: '))
    
    while no_of_items > 0:
        a = int(input('Enter item code: '))        
        if a == 99:
            no_of_items = no_of_items + 1
            
        elif a == 88:
            no_of_items = no_of_items - 1
            
        elif df.loc[a,'Quantity'] == 0:
            df.loc[a,'Quantity'] = int(input('Number needed:   '))
            no_of_items = no_of_items -1
            
        else:
            df.loc[a,'Quantity'] = int(input('Number needed:   '))+df.loc[a,'Quantity']
            no_of_items = no_of_items
            
        


    #Modifying the dataframe according to our needs
    df['Cost'] = (df['Price']+(df['Price']*(df['GST %']/100)))*df['Quantity']#GST
    df = df.loc[df['Quantity']!=0,:]
    #df['Quantity'] = (df.Quantity).astype('int') #--> Print Quantity as int
    s = df.loc[:,'Cost']
    for i in range(s.shape[0]):                 #Adds the costs
        total_cost = total_cost + df.iloc[i,4]
    total_cost = int(total_cost//1)             #Rounds off the value

    #Decorations
    print('\n\n\n')
    print('\tSELVAPRIYA DEPARTMENTAL STORES')
    print('\t\t   BILL')
    print('-----------------------------------------------')
    print(df)
    print('-----------------------------------------------')
    print('Total cost:\t\t\t\t ₹',total_cost,sep='')
    print('-----------------------------------------------')
    #Printing Balance amount

    amount = int(input('\nEnter the amount received: ₹ '))

    while (amount-total_cost) < 0:
        amount = int(input('Amount recieved not sufficient enter a greater amount: ₹ ')) 

    print('\nBalance to be given:       ₹',amount-total_cost)

    #Rerun the program?
    print('\n\n\n')
    x = input("Proceed to next bill? (Press Enter for yes and 'n' for no): ")
    print('\n\n\n')
