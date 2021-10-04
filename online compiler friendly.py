import pandas as pd
#df_main = pd.read_csv("E:\\New folder(3)\\database.csv",index_col='id')
#instead of of importing data as csv we are creating a dataframe directly here
df_main = pd.DataFrame([['Pencil',10],['Eraser',3],['Stapler',20],['Black Stick',10],['Blue Gel',12]], index = [1,2,3,4,5], columns = ['name','price'])
df_main.index.name = 'id'

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
