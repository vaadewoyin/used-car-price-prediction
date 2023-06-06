# Used Car Price Prediction
## Project Details
The goal of this project is to predict the prices of used cars based on specific features such as brand, model, year, body type, maximum power, maximum/top speed, etc. The project was completed following these key steps:

1. Data Collection: The data was collected by scraping the Autotrader South Africa's website using Python and the Selenium framework. The scraping process was carried out in multiple sessions or batches between 23/04/23 and 24/04/23. In total, over 19,000 cars were scraped, with each session contributing a specific number of cars.

2. Data Cleaning: To prepare the scraped car data for analysis and modeling, a thorough cleaning process was conducted. This involved addressing issues such as correcting inappropriate data types, removing units from various features, eliminating duplicate entries, removing unnecessary whitespaces, and correcting any erroneous inputs.

3. Exploratory Data Analysis and Modeling: Exploratory data analysis (EDA) was performed to gain insights into the dataset. Additionally, five different regression models were utilized for modeling: SVR regressor, KNeighborsRegressor, RandomForestRegressor, XGBRegressor, and LGBMRegressor. A 10-fold cross-validation was conducted, and the best-performing model (XGBRegressor) was selected. Hyperparameter tuning was performed using the Optuna library. Finally, the model was evaluated on a separate test set.

4. Flask Web App: A simple Flask web application was developed to showcase the results and provide a user-friendly interface. The web app allows users to input relevant car details and obtain predicted prices based on the trained model.


## Some insights from EDA
1. Toyota is the most frequent used car brand in the dataset. this is true since the most popular car brand in South Africa is Toyota. After Toyota is Volkswagen and the rest.
2. SUV dominates as the most popular used car brand sold on Autotrader South Africa. With regards to color, the top 3 colors of used cars on the website are white,silver and grey.
3. There are more used cars with automatic transmission compared to the manual. with respect to fuel type, cars with petrol fuel type are most frequent, a very small number of cars have hybrid or electric fuel type
4. The median prices of used cars manufactured in 2018 were the lowest compared to other years
5. Cars with all-wheel drive have higher median price compared to other driven wheels type. 
6. Cars with v12 cylinder layout have significant higher median price compared to the rest. This is expected as cars with V12 cylinders are typically high-end, luxury vehicles that are known for their exceptional performance and high price tags


## Modelling
Modelling was done with and without outliers to access the impact of outliers on our models. The result of the modelling is given below:

| Metric                                     | SVR        | Knn        | RandomForest | XGB        | LightGBM   |
|--------------------------------------------|------------|------------|--------------|------------|------------|
| 10-fold CV MAE with outliers               | 75438.58   | 59005.82   | 46184.26     | 43848.64   | 46477.99   |
| 10-fold CV MAE without outliers            | 48081.16   | 38410.10   | 30860.36     | 29980.96   | 30659.60   |
| Difference (with outliers - without outliers) | 27357.42   | 20595.72   | 15323.90     | 13867.67   | 15818.40   |

The table above shows the result of modelling with and without outliers. overall, all the models performed much better after outliers were removed. The best model over all is XGBRegressor model.


## Evaluation on separate test set
After hyperparameter tunning, the XGBRegressor model was evaluated using a separete test set. the resut obtained is show below:

| Metric          | Value    |
|-----------------|----------|
| MAE on test set | 29908.83 |
| R2 score        | 0.94     |


## Flask web app
The screenshot of the web app is given below:

![web-app](https://github.com/vaadewoyin/used-car-price-prediction/blob/main/flask-web-app-screenshot.png)
