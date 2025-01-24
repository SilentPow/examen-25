import pandas as pd

def get_dataframe(name):
    return pd.read_csv(name)


if __name__ == '__main__':
    customers = get_dataframe('customers.csv')
    orders = get_dataframe('orders.csv')
    products = get_dataframe('products.csv')

    customers.head()