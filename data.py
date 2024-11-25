import pandas as pd

# Read CSV with correct parameters
df = pd.read_csv('data/Reviews.csv', 
                 skiprows=1,  # Skip the "Reviews" row
                 low_memory=False,
                 dtype={
                     'Id': str,
                     'ProductId': str,
                     'UserId': str,
                     'ProfileName': str,
                     'HelpfulnessNumerator': int,
                     'HelpfulnessDenominator': int,
                     'Score': int,
                     'Time': int,
                     'Summary': str,
                     'Text': str
                 })

print("\nFirst few rows:")
print(df.head())
print("\nColumns:", df.columns.tolist())