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
    all_protein = df.loc[df['Protein'].idxmax()]
    print(f'type(all_protein is {type(all_protein)}')
    # print(all_protein)
    all_calories = df.loc[df['Calories'].idxmax()]
    # print(all_calories)
    # print(f'this is {df[df['Calories'] != 0]} \n')  # this doesn't work

    non_z = df[df['Calories'] != 0]
    print(f'type of non_z is {type(non_z)}')

    non_z['Quotients'] = non_z['Protein'] / non_z['Calories']
    print(f'type of non_z["Quotients"] is {type(non_z["Quotients"])}')
    good_food = non_z.loc[non_z['Quotients'].idxmax()]['Item']
    print(good_food)
    return good_food


if __name__ == '__main__':
    # print(df.columns)
    get_bodybuilder_friendly_foods()