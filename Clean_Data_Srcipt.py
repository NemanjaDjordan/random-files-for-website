import pandas as pd

# Load the dataset from the given URL
url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
data = pd.read_csv(url)  # Read the dataset into a DataFrame

# Display the first few rows of the dataset to understand its structure and initial content
print("Initial Data:")
print(data.head())  # Print the first 5 rows of the DataFrame

# Display the column names to verify which columns are present and their names
print("\nColumn Names:")
print(data.columns)  # Print the names of the columns in the DataFrame

# 1. Handle Missing Values
# Check if the 'Age' column exists in the dataset
if 'Age' in data.columns:
    # Fill missing values in the 'Age' column with the median value of 'Age'
    data['Age'] = data['Age'].fillna(data['Age'].median())

# Check if the 'Embarked' column exists in the dataset
if 'Embarked' in data.columns:
    # Drop rows where 'Embarked' column has missing values
    data = data.dropna(subset=['Embarked'])

# 2. Remove Duplicates
# Remove duplicate rows from the dataset
data = data.drop_duplicates()

# 3. Convert Data Types
# Check if the 'PassengerId' column exists in the dataset
if 'PassengerId' in data.columns:
    # Convert 'PassengerId' column to string type
    data['PassengerId'] = data['PassengerId'].astype(str)

# 4. Create New Features
# Check if both 'SibSp' (number of siblings/spouses aboard) and 'Parch' (number of parents/children aboard) columns exist
if 'SibSp' in data.columns and 'Parch' in data.columns:
    # Create a new feature 'FamilySize' by summing 'SibSp' and 'Parch'
    data['FamilySize'] = data['SibSp'] + data['Parch']

# Display the cleaned data to verify changes and see the new features
print("\nCleaned Data:")
print(data.head())  # Print the first 5 rows of the cleaned DataFrame

# Save the cleaned dataset to a new CSV file for further use
data.to_csv('cleaned_titanic_data.csv', index=False)  # Save the DataFrame to a CSV file without including row indices
