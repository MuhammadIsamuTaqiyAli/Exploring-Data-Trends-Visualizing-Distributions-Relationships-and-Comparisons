#Task 1: Visualizing Data Distributions

import matplotlib.pyplot as plt
import seaborn as sns

# Clean and prepare data for visualizations
# Convert 'ConvertedCompYearly' to numeric, dropping NaN values for the histogram
compensation_data = pd.to_numeric(data['ConvertedCompYearly'], errors='coerce').dropna()

# Convert 'Age' categories into numerical values for the box plot
age_mapping = {
    "Under 18 years old": 17,
    "18-24 years old": 21,
    "25-34 years old": 29.5,
    "35-44 years old": 39.5,
    "45-54 years old": 49.5,
    "55-64 years old": 59.5,
    "65 years or older": 65
}
data['Age_Numeric'] = data['Age'].map(age_mapping).dropna()

# Plotting
plt.figure(figsize=(14, 6))

# 1. Histogram for 'ConvertedCompYearly'
plt.subplot(1, 2, 1)
sns.histplot(compensation_data, bins=30, kde=True, color='blue')
plt.title('Histogram of ConvertedCompYearly')
plt.xlabel('Yearly Compensation')
plt.ylabel('Frequency')

# 2. Box Plot for 'Age'
plt.subplot(1, 2, 2)
sns.boxplot(data=data, x='Age_Numeric', color='green')
plt.title('Box Plot of Age')
plt.xlabel('Age (Converted to Numeric)')

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('MultipleFiles/survey_data (2).csv')

# Plotting the histogram for ConvertedCompYearly
plt.figure(figsize=(10, 6))
plt.hist(data['ConvertedCompYearly'].dropna(), bins=30, color='blue', alpha=0.7)
plt.title('Histogram of Yearly Compensation (ConvertedCompYearly)')
plt.xlabel('Yearly Compensation')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

import seaborn as sns

# Convert Age to a categorical type if not already
data['Age'] = pd.Categorical(data['Age'], ordered=True)

# Plotting the box plot for Age
plt.figure(figsize=(10, 6))
sns.boxplot(x='Age', y='ConvertedCompYearly', data=data)
plt.title('Box Plot of Yearly Compensation by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Yearly Compensation')
plt.grid(axis='y', alpha=0.75)
plt.show()



#Task 2: Visualizing Relationships in Data

# Reload the dataset to ensure integrity and update the data handling
data = pd.read_csv(file_path)

# Convert necessary columns to numeric types
data['ConvertedCompYearly'] = pd.to_numeric(data['ConvertedCompYearly'], errors='coerce')
data['JobSatPoints_6'] = pd.to_numeric(data['JobSatPoints_6'], errors='coerce')
data['Age_Numeric'] = data['Age'].map(age_mapping).dropna()

# Filter the dataset for valid numeric values in relevant columns
filtered_data = data.dropna(subset=['Age_Numeric', 'ConvertedCompYearly', 'JobSatPoints_6'])

# Plotting
plt.figure(figsize=(14, 6))

# 1. Scatter Plot of Age and ConvertedCompYearly
plt.subplot(1, 2, 1)
sns.scatterplot(data=filtered_data, x='Age_Numeric', y='ConvertedCompYearly', color='purple', alpha=0.6)
plt.title('Scatter Plot of Age vs ConvertedCompYearly')
plt.xlabel('Age (Numeric)')
plt.ylabel('Yearly Compensation')

# 2. Bubble Plot of ConvertedCompYearly and JobSatPoints_6 with Age as Bubble Size
plt.subplot(1, 2, 2)
bubble_sizes = filtered_data['Age_Numeric'] * 10  # Scale bubble size for better visibility
plt.scatter(
    filtered_data['ConvertedCompYearly'],
    filtered_data['JobSatPoints_6'],
    s=bubble_sizes,
    alpha=0.5,
    color='orange',
    edgecolors='w',
    linewidth=0.5
)
plt.title('Bubble Plot of Compensation and Job Satisfaction')
plt.xlabel('Yearly Compensation')
plt.ylabel('Job Satisfaction Points')
plt.grid(True)

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('MultipleFiles/survey_data (2).csv')

# Convert Age to numeric values for plotting
age_mapping = {
    'Under 18 years old': 17,
    '18-24 years old': 21,
    '25-34 years old': 29,
    '35-44 years old': 39,
    '45-54 years old': 49,
    '55-64 years old': 59,
    '65 years or older': 65,
    'Prefer not to say': None
}
data['Age_numeric'] = data['Age'].map(age_mapping)

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Age_numeric', y='ConvertedCompYearly', alpha=0.6)
plt.title('Scatter Plot of Age vs. Converted Compensation Yearly')
plt.xlabel('Age (Numeric)')
plt.ylabel('Converted Compensation Yearly')
plt.grid(True)
plt.show()

# Bubble plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='ConvertedCompYearly', y='JobSatPoints_6', 
                size='Age_numeric', sizes=(20, 500), alpha=0.5, legend=False)
plt.title('Bubble Plot of Compensation vs. Job Satisfaction with Age as Bubble Size')
plt.xlabel('Converted Compensation Yearly')
plt.ylabel('Job Satisfaction Points (6)')
plt.grid(True)
plt.show()



#Task 3: Visualizing Composition of Data with Bar Charts
    
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('MultipleFiles/survey_data (2).csv')

# 1. Horizontal Bar Chart of MainBranch Distribution
main_branch_counts = data['MainBranch'].value_counts()
plt.figure(figsize=(10, 6))
main_branch_counts.plot(kind='barh')
plt.xlabel('Number of Respondents')
plt.ylabel('Main Branch')
plt.title('Distribution of Respondents\' Primary Roles')
plt.show()

# 2. Vertical Bar Chart of Top 5 Programming Languages Respondents Want to Work With
language_counts = data['LanguageWantToWorkWith'].str.split(';', expand=True).stack().value_counts().head(5)
plt.figure(figsize=(10, 6))
language_counts.plot(kind='bar')
plt.xlabel('Programming Languages')
plt.ylabel('Number of Respondents')
plt.title('Top 5 Programming Languages Respondents Want to Work With')
plt.show()

# 3. Stacked Bar Chart of Median JobSatPoints_6 and JobSatPoints_7 by Age Group
age_groups = data.groupby('Age')['JobSatPoints_6', 'JobSatPoints_7'].median().reset_index()
age_groups.set_index('Age').plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xlabel('Age Group')
plt.ylabel('Median Job Satisfaction Points')
plt.title('Median Job Satisfaction Points by Age Group')
plt.show()

# 4. Bar Chart of Database Popularity
database_counts = data['DatabaseHaveWorkedWith'].str.split(';', expand=True).stack().value_counts()
plt.figure(figsize=(10, 6))
database_counts.plot(kind='bar')
plt.xlabel('Databases')
plt.ylabel('Number of Respondents')
plt.title('Popularity of Databases Used by Respondents')
plt.show()



#Task 4: Visualizing Comparison of Data with Bar Charts 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the survey data
data = pd.read_csv('MultipleFiles/survey_data (2).csv')

# Group by Age and calculate the median of ConvertedCompYearly
median_compensation = data.groupby('Age')['ConvertedCompYearly'].median().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Age', y='ConvertedCompYearly', data=median_compensation, palette='viridis')
plt.title('Median Converted Compensation Yearly by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Median Compensation (Yearly)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Count the number of respondents by country
country_counts = data['Country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Count']

plt.figure(figsize=(12, 8))
sns.barplot(x='Count', y='Country', data=country_counts.head(20), palette='magma')  # Show top 20 countries
plt.title('Top 20 Countries by Respondent Count')
plt.xlabel('Number of Respondents')
plt.ylabel('Country')
plt.tight_layout()
plt.show()
