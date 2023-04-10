An Analysis of Vogue Models 
By: Priya Hariharan and Alia Yusaini

**Summary of Research Questions and Results:**
1. Is colorism present in the modeling industry? Does Vogue prefer lighter skin color models compared to darker skin-colored models on their magazine covers?
- To some extent, we believe that colorism is still present in the modeling industry seeing as there is a trend for Vogue using lighter skinned models. 

2. How has time changed the preference for skin color in the modeling industry? What is the preference for the skin color of the Vogue magazine models over time? When did this change begin happening?
- Our graph depicts more lighter colored models being used overall, especially in the years 2004 and 2013. 

3. Is the modeling industry diverse, or do they just seem that way?
- Of the most popular Vogue models, what is the most prominent skin tone and how does this compare to the skin tone preference over time? Does this indicate that Vogue is using lighter skin colored models over time and just having models of darker skin tones as a “token” for diversity? 


**Motivation:**
1. Is colorism present in the modeling industry?
- In our society today, there is a vast amount of issues concerning race due to racism that is targeted towards people of color. The modeling industry has had many issues surrounding representation, so by tackling this question we can see whether this statement is unfounded or not. 


2. How has time changed preference for skin color in the modeling industry? 
- As time progresses, our society has been more accepting of diversity and most entertainment industries have taken some steps to promote diversity. These questions look at the trend over time to see if this change took place and whether lighter skinned models are more sought after. 


3. Is the modeling industry diverse, or do they just seem that way?
- Many organizations have issues with using diversity as a tool for their own success. If the modeling industry is the same way, that could give us a lot of insight into what their true motivations are and whether it is ethical or not. By knowing whether diversity is used instrumentally, we can see how people of color are impacted. 


**Dataset:**
- The link we are using is from a GitHub repository called The Pudding Database. The exact link to our dataset is [The Vogue Dataset](https://github.com/the-pudding/data/tree/master/vogue).  
- We’re merging 2 datasets; faces.csv and models.csv. Faces.csv contains the name of the model, the skin tone, the lightness value of the skin tone, and the date that the models appear on the cover. Models.csv contains the name of the model, the skin tone, the lightness value of the skin tone, and the frequency that the model appears on the Vogue cover from January 2000 to December 2018.


**Method:**

1. Install and import pyplot and pandas.

2. Before we started, we created a function called clean_data that used the pd.read_csv function to read the faces and models csv files. First, we merged the datasets using a left and right merge on ‘model.’ To format the date we used the pd.datetime function to change the date into an ISO format. Then, we changed the column names for l_x and l_y to l_cover and l_model respectively since it refers to which part of the dataset this came from.

3. For question 1, we created a function named plot_monthly to just plot all the l values from each month to see what it looks like. In plot_monthly, we created a variable called monthly_fm that had the numerical values of the merged dataset, which is l_model (lightness value from models dataset) and l_cover (lightness values for the model for each cover). For monthly_fm, we used the resample function by ‘M’, which would resample it by month. The graph we created is a scatter plot using plotly.express, and we did this by graphing the ISO formatted dates of monthly_fm (x value) against the l_model value (y value) using the monthly_fm as the data. The x value was calculated by doing monthly_fm.index which was possible because we already set the date as the index when we reformatted it. We added a nonlinear trendline using the trendline option in the graph and we set it to “lowess.” We also created another function called l_value_num_cov to plot the number of covers (n_covers) against the lightness value. In the l_value_num_cov, we used a scatter plot from plotly.express, graphing n_covers (x value) against l_model (y_value) with the merged data as the dataset.

4. For question 2, we created a method called plot_yearly containing a variable called yearly_fm, where we used the resample function by ‘Y’, which would resample it by year. This variable holds the l_model and l_cover values by averaging a value per month to give us a “yearly” dataframe. The graph we created is a line graph using plotly.express, and we did this by graphing the ISO formatted dates of yearly_fm (x value) against the l_model value (y value) using the yearly_fm as the data. The x value was calculated by doing yearly_fm.index which was possible because we already set the date as the index when we reformatted it. We used the kind = ‘line’ function to create a line graph.

5. For question 3, we wanted to look at models who had 4 and above covers. This graph compares the lightness values for each cover and the corresponding model. First, we created a function called filter_4_more that filtered for all rows of data that had n_covers greater than or equal to 4. We also made a new column for the corresponding year of those covers using the DateTime function. In filter_4_more, we made a variable called more_4_cov that used the data.loc function on mask1, which created the dataset we wanted to graph. We created a function that plots the filtered data named plot_l_value_model. This function plots the filtered dataset from filter_4_more with a scatter plot using plotly.express, graphing l_cover (x value) against l_model (y value) using the more_4_cov data as the dataset. We added the hue value by using the color function and assigning it to ‘Year.’

6. We created a test file in which we had the functions test_clean_data and test_filter_4_more. First, we imported pandas and Vogue.py (file with functions) in the test file. Since our project is more graph heavy, we decided to test our functions by using the clean data and the filter for the more_4_cov function. The test_clean_data checks if the columns ‘l_model', 'l_cover', 'n_covers', 'model' are present. The first two columns are listed to see if the column names were changed accordingly and the last two are listed to see if the data was merged properly. We also tested to see if the index column in the cleaned data set is the date column in the ISO format by checking the index of a random row (we used Lupita Nyong'o as our model). The test_filter_4_more is just a method containing a variable to test if all the data of models with 4 or more covers is filtered correctly. The function filter_4_more in the Vogue file will be used when we are creating the graph for the more_4_cov method in the main Vogue.py file. In this test function, we tested to see if the minimum covers (n_covers) is more than or equal to 4.
