import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker to generate random data
fake = Faker()

# Function to generate random date between two dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# List of sample values for categorical fields
case_types = ['Criminal', 'Civil', 'Family', 'Corporate', 'Property']
court_types = ['High Court', 'Family Court', 'District Court', 'Commercial Court', 'Small Claims Court']
case_outcomes = ['Conviction', 'Acquittal', 'Dismissal', 'Settlement', 'Judgment for Plaintiff', 'Pending']
lawyer_firms = ['Smith & Co', 'Davis Law Firm', 'Lee & Partners', 'Wilson Legal', 'Young & Associates', 'Carter Law', 'Davis Legal Services', 'Clark & Harris', 'Black Legal Solutions']

# List to hold the data
data = []

# Start date for cases
start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 1, 1)

# Generate 5000 rows
for i in range(5000):
    case_id = i + 1
    case_type = random.choice(case_types)
    court_type = random.choice(court_types)
    judge_name = fake.name()
    lawyer_name = fake.name()
    case_start_date = random_date(start_date, end_date)
    case_end_date = random_date(case_start_date, end_date)
    judge_experience = random.randint(5, 40)
    lawyer_experience = random.randint(1, 35)
    case_duration = (case_end_date - case_start_date).days
    case_outcome = random.choice(case_outcomes)
    lawyer_firm = random.choice(lawyer_firms)
    case_complexity = random.choice(['Low', 'Medium', 'High'])
    case_status = random.choice(['Closed', 'Open', 'Pending'])

    # Append the generated row to the data list
    data.append([case_id, case_type, court_type, judge_name, lawyer_name, case_start_date, case_end_date, judge_experience, lawyer_experience, case_duration, case_outcome, lawyer_firm, case_complexity, case_status])

# Create a DataFrame
df = pd.DataFrame(data, columns=[
    'Case ID', 'Case Type', 'Court Type', 'Judge Name', 'Lawyer Name', 'Case Start Date', 
    'Case End Date', 'Judge Experience (Years)', 'Lawyer Experience (Years)', 'Case Duration (Days)', 
    'Case Outcome', 'Lawyer Firm', 'Case Complexity Level', 'Case Status'
])

# Save the DataFrame to a CSV file
df.to_csv('cases_dataset.csv', index=False)

print("CSV file 'cases_dataset.csv' generated successfully with 5000 cases.")