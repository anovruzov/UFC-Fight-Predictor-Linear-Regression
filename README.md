# Fighter Stats Predictor

## Overview

This Python script leverages the power of Pandas for data manipulation and Scikit-learn's Linear Regression model to predict outcomes of fights based on various fighter statistics.
The dataset includes extended data on fighters such as Dricus Du Plessis, Robert Whittaker, Israel Adesanya, Islam Makhachev, Charles Oliveira, Khabib Nurmagomedov, and Justin Gaethje.

## Features

- **Data Manipulation**: Utilizes Pandas for organizing fighter data into a structured format.
- **Linear Regression Model**: Employs a linear regression model from Scikit-learn to predict fight win percentages based on fighter statistics.
- **Statistical Analysis**: Analyzes fighters' performance metrics such as win percentage, takedown defense rate, takedowns per fight, submission amounts, strikes per minute, knockouts, reach, age, and current win streak.
- **Prediction**: Compares fighters within their weight class to predict the winner based on their stats.

## Requirements

- Python 3.x
- pandas
- scikit-learn

To install the required libraries, run:

```bash
pip install pandas scikit-learn
