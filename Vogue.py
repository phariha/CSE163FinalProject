"""
Priya Hariharan, Alia Yusaini
Final Project

This file contains functions that plots data from the file faces.csv
and model.csv.
"""
import pandas as pd
import plotly.express as px


def clean_data(faces, models):
    """
    Returned dataframe is merged faces and model dataframe by the model
    column, having the columns renamed as l_cover and l_model for the l
    values from faces and model respectively and have the ISO formatted
    date as index.
    """
    # processing faces and model as csv file
    f = pd.read_csv(faces)
    m = pd.read_csv(models)
    # merge f and m by the model column
    fm = f.merge(m, left_on='model', right_on='model')
    # change date in fm to date_time format and set the date as
    fm['date'] = pd.to_datetime(fm['date'])
    fm = fm.set_index('date')
    # renaming l_x as l_model since it indicates the lightness value for the
    # skin of models
    # renaming l_y as l_cover since it indicates the lightness value for the
    # model on the particular cover
    fm = fm.rename(columns={'l_x': 'l_cover', 'l_y': 'l_model'})
    return fm


def plot_monthly(merged_data):
    """
    Returns a plot of time (month) vs l_model (lightness value of model)
    """
    # resample the data by month
    monthly_fm = merged_data.resample('M').mean()
    # plot for average l_model value against months
    q1 = px.scatter(monthly_fm, x=monthly_fm.index, y='l_model',
                    trendline="lowess",
                    title='All Lightness Values of Vogue Models over Time\
                    (Monthly)')
    q1.update_layout(xaxis_title="Lightness Value", yaxis_title="Date")
    q1.show()


def plot_yearly(merged_data):
    """
    Returns a plot of time (year) vs l_model (lightness value of model)
    """
    # resample the data by year
    # gives only numerical values, l_model, l_cover, and n_covers averaged
    yearly_fm = merged_data.resample('Y').mean()
    # plot for average l_model value against year
    q2 = px.line(yearly_fm, x=yearly_fm.index, y='l_model',
                 title='Average Lightness Value (per Month) of Vogue\
                         Models over Time')
    q2.update_layout(xaxis_title="Lightness Value", yaxis_title="Date")
    q2.show()


def plot_lvalue_num_cov(merged_data):
    """
    Returns a plot of the lightness value against the number of covers
    """
    q1 = px.scatter(merged_data, x='n_covers', y='l_model',
                    title='Number of Covers vs. Corresponding \
                        Lightness Values')
    q1.update_layout(xaxis_title="Number of Covers",
                     yaxis_title="Lightness Value")
    q1.show()


def filter_4_more(merged_data):
    """
    Returns a filtered data frame of models with 4 or more
    Vogue covers
    """
    # create a new column to indicate the year that the cover got out
    merged_data['Year'] = pd.DatetimeIndex(merged_data.index).year
    # only take into account the models that have 4 or more Vogue covers
    mask1 = merged_data['n_covers'] >= 4
    more_4_cov = merged_data.loc[mask1]
    return more_4_cov


def plot_lvalue_model(merged_data):
    """
    Returns a plot of the lightness value from each cover for
    the models that have done 4 or more covers
    """
    more_4_cov = filter_4_more(merged_data)

    q3 = px.scatter(more_4_cov, y='l_cover', x='model',
                    labels=dict(y="Lightness Value for Each Cover", x='Model'),
                    title='Model vs. Corresponding Lightness Values on Each \
                        Cover',
                    color='Year')
    q3.update_layout(xaxis_title="Number of Covers",
                     yaxis_title="Lightness Value for Each Cover")
    q3.show()


def main():
    faces = 'faces.csv'
    models = 'models.csv'

    fm = clean_data(faces, models)
    plot_monthly(fm)
    plot_yearly(fm)
    plot_lvalue_num_cov(fm)
    plot_lvalue_model(fm)


if __name__ == "__main__":
    main()
