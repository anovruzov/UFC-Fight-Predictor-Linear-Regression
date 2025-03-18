import pandas as pd
from sklearn.linear_model import LinearRegression

# Extended data including Khabib, Gaethje, and others
data = {
    'Fighter_Name': ['Dricus Du Plessis', 'Robert Whittaker', 'Israel Adesanya', 'Islam Makhachev', 'Charles Oliveira', 'Khabib Nurmagomedov', 'Justin Gaethje'],
    'Fight_Win_Percentage': [91.3, 78.1, 88.9, 96.2, 79.1, 100, 86.2],
    'Takedown_Defense_Rate': [40, 83, 78, 90, 56, 84, 75],
    'Takedowns_Per_Fight': [3.0, 0.85, 0.05, 3.17, 2.32, 5.32, 0.13],
    'Amount_of_Submissions': [10, 5, 0, 0, 21, 11, 1],
    'Strikes_Per_Minute': [6.49, 4.47, 3.93, 2.46, 3.54, 4.1, 7.35],
    'Knockouts': [9, 10, 16, 0, 10, 8, 19],
    'Fighter_Reach': [72, 73, 80, 70, 74, 70, 70],
    'Fighter_Age': [32, 30, 31, 29, 33, 30, 35],
    'Weight_Class': ['Middleweight', 'Middleweight', 'Middleweight', 'Lightweight', 'Lightweight', 'Lightweight', 'Lightweight'],
    'Win_Streak': [5, 2, 9, 7, 4, 12, 3]
}
df = pd.DataFrame(data)

# Selecting features and target
features = df[['Takedown_Defense_Rate', 'Takedowns_Per_Fight', 'Amount_of_Submissions', 'Strikes_Per_Minute', 'Knockouts', 'Fighter_Reach', 'Fighter_Age']]
target = df['Fight_Win_Percentage']

# Training the Linear Regression model
model = LinearRegression()
model.fit(features, target)

# Function to get fighter stats
def get_fighter_stats(name, dataframe):
    fighter_stats = dataframe[dataframe['Fighter_Name'] == name].iloc[0]
    return [fighter_stats['Fight_Win_Percentage'], fighter_stats['Takedown_Defense_Rate'], fighter_stats['Takedowns_Per_Fight'], fighter_stats['Amount_of_Submissions'], fighter_stats['Strikes_Per_Minute'], fighter_stats['Knockouts'], fighter_stats['Fighter_Reach'], fighter_stats['Fighter_Age']]

# Group fighters by weight class and compare within each group
for weight_class in df['Weight_Class'].unique():
    wc_df = df[df['Weight_Class'] == weight_class]

    for i in range(len(wc_df)):
        for j in range(i+1, len(wc_df)):
            fighter1_name = wc_df.iloc[i]['Fighter_Name']
            fighter2_name = wc_df.iloc[j]['Fighter_Name']

            # Getting stats for fighters
            fighter1_stats = get_fighter_stats(fighter1_name, wc_df)
            fighter2_stats = get_fighter_stats(fighter2_name, wc_df)

            # Predicting Performance Scores
            fighter1_score = model.predict([fighter1_stats])[0]
            fighter2_score = model.predict([fighter2_stats])[0]

            # Determining the predicted winner
            winner = fighter1_name if fighter1_score > fighter2_score else fighter2_name
            print(f"Predicted Winner between {fighter1_name} and {fighter2_name} in {weight_class}: {winner}")
