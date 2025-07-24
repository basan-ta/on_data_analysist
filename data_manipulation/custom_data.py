import pandas as pd
import numpy as np
import os
import random

from datetime import date, timedelta

# Create data directory
os.makedirs('data', exist_ok=True)

# Define name-gender pairs as per your specification
male_names = [
    'Aarav', 'Aakash', 'Bikram', 'Chandra', 'Dawa', 'Gopal', 'Hari', 'Indra', 'Keshav', 'Laxman',
    'Manish', 'Niranjan', 'Prakash', 'Ram', 'Sagar', 'Sunil', 'Uday', 'Vijay', 'Yubaraj', 'Bikash',
    'Dipendra', 'Lokendra', 'Mohan', 'Nabin', 'Purna', 'Rabin', 'Rajendra', 'Saroj', 'Tilak', 'Uttam',
    'Binod', 'Devendra', 'Ganesh', 'Jitendra', 'Kishore', 'Lokesh', 'Nitish', 'Pradeep', 'Ramesh', 'Suresh',
    'Umesh', 'Binay', 'Deepak', 'Kamal', 'Loknath', 'Narayan', 'Padam', 'Ranjan', 'Shankar', 'Tekendra'
]

female_names = [
    'Aahana', 'Aarti', 'Bhawana', 'Gita', 'Kamala', 'Laxmi', 'Maya', 'Mina', 'Nisha', 'Prema',
    'Priya', 'Saraswati', 'Sita', 'Smriti', 'Sunita', 'Tara', 'Asha', 'Chandra', 'Deepa', 'Geeta',
    'Jaya', 'Kalpana', 'Manisha', 'Nirmala', 'Priti', 'Radha', 'Sadhana', 'Shanti', 'Sushila', 'Yamuna',
    'Apsara', 'Bimala', 'Dipa', 'Kamala', 'Namrata', 'Pratima', 'Rupa', 'Sarita', 'Tamara', 'Usha',
    'Abha', 'Binita', 'Chhaya', 'Dhanmaya', 'Gauri', 'Jyoti', 'Laxana', 'Mohana', 'Nanda', 'Runa'
]
# Generate 1000 unique random names from a-z
def generate_name():
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    name_length = random.randint(3, 8)
    
    # Create pronounceable names with alternating consonants/vowels
    name = ''
    for i in range(name_length):
        if i % 2 == 0:
            name += random.choice(consonants)
        else:
            name += random.choice(vowels)
    return name.capitalize()

# Generate unique names
all_names = set()
while len(all_names) < 1000:
    all_names.add(generate_name())
all_names = list(all_names)



# Create dataset with 1000 records
records = 1000
data = {
    'id': range(1, records + 1),
    'name': [],
    'gender': [],
    'age': np.random.randint(20, 45, records),
    'salary': np.random.randint(20000, 150000, records),
    'city': np.random.choice(
        ['Kathmandu', 'Pokhara', 'Lalitpur', 'Bharatpur', 'Biratnagar', 
         'Birgunj', 'Butwal', 'Dharan', 'Nepalgunj', 'Hetauda'],
        records,
        p=[0.3, 0.15, 0.1, 0.08, 0.07, 0.07, 0.06, 0.05, 0.05, 0.07]
    ),
    'department': np.random.choice(
        ['Engineering', 'HR', 'Finance', 'Marketing', 'Sales', 'Operations'],
        records,
        p=[0.3, 0.15, 0.15, 0.1, 0.2, 0.1]
    ),
    'join_date': [],
}

# Generate names and genders with specified distribution
genders = np.random.choice(['M', 'F'], records, p=[0.55, 0.45])
for gender in genders:
    if gender == 'M':
        data['name'].append(np.random.choice(male_names))
    else:
        data['name'].append(np.random.choice(female_names))
    data['gender'].append(gender)

# Generate join dates with yearly increments
start_date = date(2010, 1, 1)
for i in range(records):
    join_date = start_date + timedelta(days=np.random.randint(0, 365*10))
    data['join_date'].append(join_date.strftime('%Y-%m-%d'))

# Create DataFrame
df = pd.DataFrame(data)

# Adjust salary based on experience
current_year = 2025  # Since today is 2025-07-20
df['experience'] = current_year - pd.to_datetime(df['join_date']).dt.year
df['salary'] = df['salary'] + (df['experience'] * 2500)

# Save to CSV
df.to_csv('data/employee_data.csv', index=False)
print("Dataset created with 1000 records at data/employee_data.csv")