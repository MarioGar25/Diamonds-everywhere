# Diamonds-everywhere


![Diamond](http://admin.acceleratingscience.com/mining/wp-content/uploads/sites/3/2018/04/diamond.jpg)

## Introduction  
In the world, diamonds have been among the most coveted objects by people for their beauty and properties. Their costly procurement and scarcity make diamonds objects that have a high value in the market. But can this value be calculated according to the diamond's properties?

In this project, we intend to use supervised learning to create predictive models using a series of diamond variables to predict the market value of other diamonds.

## Objetive

Predicting diamond prices using Machine Learning models.

## Variables

### Target Variable

`price`: Diamond price.

The target variable is the price of the diamond. 
It has the following distribution:

![TargetDistribution](output\TargetDistribution.jpg)


### Numerical Variables

The numerical variables are as follows:

 `id`: Input ID.
 
 `carat`: diamond weight.
 
 `table`: Flat part of the upper part.
 
 `x`: Length in mm.

 `y`: Width in mm.
 
 `z`: Depth in mm. 

 `depht`:  Total depth percentage = z / mean(x, y) = 2 * z / (x + y).


The numerical variables have the following distributions:

![Numerical_Distribution](output\NumericalDistribution.jpg)

### Categorical Variables
The categorical variables are as follows:

`cut`: The way in which the diamond facets interact with light.
 
`clarity`: Purity or transparency of a diamond.
 
`color`: Color of a diamond.

The categorical variables have the following distributions:

![Categorical_Distribution](output\CategoricalDistribution.jpg)

## Data 

The data data used for this project were obtained from the following [url](https://www.kaggle.com/c/diamonds-datamad0121/)
## Process


### Preprocessing

The cleaning process starts by checking the dataset. Where it is discovered that there are categorical and numerical variables. It is also observed that there are no null values.  The useless columns are eliminated and the categorical variables are encoded, we have chosen to classify them in ordinal form, because there is an order of classification, therefore the categorical values are replaced by numerical ones taking into account the order. 

### Modeling
The models used are:

    · Random Forest Reggresor using HyperOpt to select the hyperparameters
    · Using Pycaret to select the best model, in this case  is Light Gradient Boosting Machine.

The metric used is `root_mean_square_error`.

## Results

After comparing the models we can affirm that in this case the best option has turned out to be the `LightGradientBoostingMachine` tuned model, model selected by the `Pycaret` library, followed by the same default model.

Here is a graphical comparison of the `RMSE` models:

![Comparative_RMSE](output\Comparative_errors.jpg)

## Libraries

The main libraries used:

[PyCaret](https://pycaret.org/)

[Hyperopt](http://hyperopt.github.io/hyperopt/)

[Sklearn](https://scikit-learn.org/stable/)

[Pandas](https://pandas.pydata.org/docs/)

[Matplotlib](https://matplotlib.org/)
