import pandas as pd

# Load the dataset
data = pd.read_csv('survey_data.csv')

# Question 1: Are people with higher education (Bachelor’s Degree and up) more likely to work remotely?
print("Question 1: Remote Work Likelihood based on Education Level")

# Filter the data to only include employed individuals
employed = data[data['Employment'] == 'Employed full-time']

# Group education levels into categories
higher_ed = employed[employed['EdLevel'].isin([
    "Bachelor’s degree", "Master’s degree", "Professional degree", "Other doctoral degree"])]

lower_ed = employed[~employed['EdLevel'].isin([
    "Bachelor’s degree", "Master’s degree", "Professional degree", "Other doctoral degree"])]

# Aggregate data to calculate the percentage of remote workers in each education level
remote_higher_ed = higher_ed[higher_ed['RemoteWork'] == 'Fully remote']['ResponseId'].count() / higher_ed['ResponseId'].count() * 100
remote_lower_ed = lower_ed[lower_ed['RemoteWork'] == 'Fully remote']['ResponseId'].count() / lower_ed['ResponseId'].count() * 100

# Print the results
print(f"Percentage of fully remote workers with higher education: {remote_higher_ed:.2f}%")
print(f"Percentage of fully remote workers with lower education: {remote_lower_ed:.2f}%")

# Question 2: Is education in Computer Science more needed in the general workforce?
print("\nQuestion 2: Need for Computer Science Education in General Workforce")

# Define computer science related jobs
cs_jobs = ['Software developer', 'Web developer', 'Data scientist', 'Systems administrator', 'DevOps specialist']

# Filter individuals with non-CS jobs and who have Computer Science education
general_workforce = employed[~employed['MainBranch'].isin(cs_jobs)]
cs_education = general_workforce[general_workforce['EdLevel'].str.contains('Computer science', case=False, na=False)]

# Calculate the percentage of general workforce with CS education
cs_education_percentage = cs_education['ResponseId'].count() / general_workforce['ResponseId'].count() * 100

# Print the results
print(f"Percentage of non-CS jobs filled by people with Computer Science education: {cs_education_percentage:.2f}%")

# Question 3: What is the language most used by employed individuals?
print("\nQuestion 3: Most Used Language by Employed Individuals")

# Filter the data to only include individuals who are employed
employed_people = data[data['Employment'].isin(['Employed full-time', 'Employed part-time'])]

# Split multiple languages into individual rows
languages_used = employed_people['CodingActivities'].str.split(';', expand=True).stack().reset_index(drop=True)

# Get the most frequent programming language
most_used_language = languages_used.value_counts().idxmax()
language_usage_count = languages_used.value_counts().max()

# Print the result
print(f"The most used language is {most_used_language} with {language_usage_count} people using it.")

# Bonus (optional): Analyze job satisfaction by education level and remote work
print("\nBonus: Job Satisfaction based on Education and Remote Work")

# Filter by higher education and remote work
remote_higher_ed_job_sat = higher_ed[higher_ed['RemoteWork'] == 'Fully remote']['JobSat'].mean()
non_remote_higher_ed_job_sat = higher_ed[higher_ed['RemoteWork'] != 'Fully remote']['JobSat'].mean()

print(f"Average job satisfaction for higher education (Fully remote): {remote_higher_ed_job_sat:.2f}")
print(f"Average job satisfaction for higher education (Not fully remote): {non_remote_higher_ed_job_sat:.2f}")

# Summary Analysis for Low Education Group
remote_lower_ed_job_sat = lower_ed[lower_ed['RemoteWork'] == 'Fully remote']['JobSat'].mean()
non_remote_lower_ed_job_sat = lower_ed[lower_ed['RemoteWork'] != 'Fully remote']['JobSat'].mean()

print(f"Average job satisfaction for lower education (Fully remote): {remote_lower_ed_job_sat:.2f}")
print(f"Average job satisfaction for lower education (Not fully remote): {non_remote_lower_ed_job_sat:.2f}")
