import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Dataset
data = {
    'tenth_cgpa': [9.8, 8.2, 9.0, 7.5, 6.5, 8.0, 5.9, 7.0, 6.0, 9.5],
    'puc_cgpa':   [9.7, 8.5, 8.8, 7.0, 6.0, 8.2, 5.5, 7.2, 6.3, 9.4],
    'caste':      ['General', 'OBC', 'SC', 'ST', 'OBC', 'General', 'SC', 'ST', 'OBC', 'General'],
    'branch':     ['CSE', 'ECE', 'EEE', 'Civil', 'ECE', 'CSE', 'Mech', 'Civil', 'Mech', 'CSE']
}

df = pd.DataFrame(data)

# Manual encoding based on priority
caste_priority = {'General': 0, 'OBC': 1, 'SC': 2, 'ST': 3}
branch_priority = {'CSE': 0, 'ECE': 1, 'EEE': 2, 'Civil': 3, 'Mech': 4}

df['caste_encoded'] = df['caste'].map(caste_priority)
df['branch_encoded'] = df['branch'].map(branch_priority)

# Features and labels
X = df[['tenth_cgpa', 'puc_cgpa', 'caste_encoded']]
y = df['branch_encoded']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model and mappings
os.makedirs("backend/model", exist_ok=True)

with open("backend/model/branch_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("backend/model/caste_priority.pkl", "wb") as f:
    pickle.dump(caste_priority, f)

with open("backend/model/branch_priority.pkl", "wb") as f:
    pickle.dump(branch_priority, f)

print("✅ Model and encoders saved with correct priorities.")
