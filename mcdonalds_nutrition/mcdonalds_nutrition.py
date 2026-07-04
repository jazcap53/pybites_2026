import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    return df.loc[df['Calories'].idxmax()]['Item']


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    non_z = df[(df['Calories'] != 0) & ((excl_drinks is False) |
               (~df['Category'].isin(['Beverages', 'Coffee & Tea'])))]
    print(f'type of non_z is {type(non_z)}')  # a DataFrame
    non_z['Quotients'] = non_z['Protein'] / non_z['Calories']
    print(f'type of non_z["Quotients"] is {type(non_z["Quotients"])}')  # a Series
    non_z_sorted = non_z.sort_values(by='Quotients', ascending=False)
    good_food = list(non_z_sorted[0:5]['Item'])
    print(f'type of good_food is {type(good_food)}')
    print(good_food)
    return good_food


if __name__ == '__main__':
    # print(df.columns)
    get_bodybuilder_friendly_foods()