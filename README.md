# Diamonds-everywhere


![Diamond](http://admin.acceleratingscience.com/mining/wp-content/uploads/sites/3/2018/04/diamond.jpg)

## Introduction  
In the world, diamonds have been among the most coveted objects by people for their beauty and properties. Their costly procurement and scarcity make diamonds objects that have a high value in the market. But can this value be calculated according to the diamond's properties?

In this project, we intend to use supervised learning to create predictive models using a series of diamond variables to predict the market value of other diamonds.

## Process


![Diamonds](images\diamonds-everywhere.jpg)


### Cleaning

The cleaning process starts by checking the dataset. Where it is discovered that there are categorical and numerical variables. It is also observed that there are no null values.  The useless columns are eliminated and the categorical variables are encoded, we have chosen to classify them in ordinal form, because there is an order of classification, therefore the categorical values are replaced by numerical ones taking into account the order.

### Modeling
The models used are Linear Regression, Random Forest and Gradient Boosting Reregression.
All of them, with standardized data.

The metric used is "mean_square_error".


## Data 

The data data used for this project were obtained from the following [url](https://www.kaggle.com/c/diamonds-datamad0121/)


