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
            df.loc[a,'Quantity'] = int(input('Number needed:   '))


    #Modifying the dataframe according to our needs
    df['Cost'] = (df['Price']+(df['Price']*(df['GST %']/100)))*df['Quantity']#GST
    df = df.dropna()
    #df['Quantity'] = (df.Quantity).astype('int') #--> Print Quantity as int
    s = df.loc[:,'Cost']
    for i in range(s.shape[0]):
        total_cost = total_cost + df.iloc[i,4]
    total_cost = int(total_cost//1) #Rounds off the value

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
    print('Balance to be given:       ₹',amount-total_cost)

    #Rerun the program?
    print('\n\n\n')
    x = input("Proceed to next bill? (Type 'y' for yes and 'n' for no): ")
    print('\n\n\n')
