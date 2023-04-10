"""
Priya Hariharan, Alia Yusaini
Final Project Test

Contains the test function for function clean_data
in Vogue.py.
"""
import Vogue
import pandas as pd


def test_clean_data(f, m):
    """
    A test function for function clean_data
    """
    data_ret = Vogue.clean_data(f, m)

    # check if the column names is changed accordingly
    needed_columns = ['l_model', 'l_cover', 'n_covers', 'model']
    for col in needed_columns:
        if col not in data_ret.columns:
            print('Test clean_data not passed: columns name not true')

    # check if index is set as date in ISO format by checking
    # one random sample point
    mask = data_ret['model'] == 'Lupita Nyongo'
    date_ISO = pd.Timestamp('2018-01-01')
    if date_ISO not in list(data_ret.loc[mask].index):
        print('Test clean_data not passed: date not true')


def test_filter_4_more(f, m):
    """
    Test function for filter_4_more
    """
    merged_data = Vogue.clean_data(f, m)
    filtered = Vogue.filter_4_more(merged_data)

    # check if n_covers for all the models if at
    # least 4
    if filtered['n_covers'].min() < 4:
        print('Test filter_4_more not passed: min cover less\
              than 4')


def main():
    f = 'faces.csv'
    m = 'models.csv'
    test_clean_data(f, m)
    test_filter_4_more(f, m)


if __name__ == "__main__":
    main()
