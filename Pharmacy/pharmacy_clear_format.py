import pandas as pd


def format_csv_result(data):
    data = pd.read_csv(data)

    '''
    Iterate over Price column to find if there is a product
    whit more than one price (it means that there is a
    product with a discount price)
    '''

    for price in data['Price']:
        #  Create two new columns to separate the prices.
        data[['Original_price', 'Discount_price']] = data['Price'].str.split(
            ',', expand=True)

    #  If there is not a discount price, fill with a "No discount" text.
    data['Discount_price'] = data['Discount_price'].fillna('No discount')

    #  Drop the "Price" column.
    data = data.drop('Precio', axis=1)

    #  Convert the dataframe to csv with a new name.
    data.to_csv('farmacia_productos_clean.csv', index=False)

    return 'Done'
