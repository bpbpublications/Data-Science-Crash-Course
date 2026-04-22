#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np

# Load data
data = pd.read_csv("/Users/pramuditkhurana/Downloads/hospital.csv")

print("Dataset Shape:", data.shape)
print(data.head())

# -----------------------------
# Target Encoding
# -----------------------------
data['readmitted'] = data['readmitted'].map({'no': 0, 'yes': 1})

# Check class distribution
print("\nTarget Distribution:")
print(data['readmitted'].value_counts())

# -----------------------------
# Handle Missing Values
# -----------------------------
data['time_in_hospital'] = data['time_in_hospital'].fillna(
    data['time_in_hospital'].median()
)

# -----------------------------
# One-Hot Encoding
# -----------------------------
categorical_cols = [
    'age', 'medical_specialty', 'diag_1', 'diag_2', 'diag_3',
    'glucose_test', 'A1Ctest', 'change', 'diabetes_med'
]

existing_cat_cols = [col for col in categorical_cols if col in data.columns]
data = pd.get_dummies(data, columns=existing_cat_cols, drop_first=True)

# -----------------------------
# Feature / Target Split
# -----------------------------
X = data.drop('readmitted', axis=1)
y = data['readmitted']

# Keep numeric only
X = X.select_dtypes(include=[np.number])

# -----------------------------
# Train Test Split
# -----------------------------
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# Train Model
# -----------------------------
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)

# -----------------------------
# Evaluation
# -----------------------------
y_pred = rf.predict(X_test)

# Safe AUC calculation
if len(rf.classes_) > 1:
    y_prob = rf.predict_proba(X_test)[:, 1]
    print("AUC Score:", roc_auc_score(y_test, y_prob))
else:
    print("Only one class predicted. Cannot compute AUC.")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# In[ ]:




