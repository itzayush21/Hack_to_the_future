from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

df = pd.read_csv("data/synthetic_symptom_data_robust2 (1).csv")
y = df['Disease']
x = df.drop('Disease', axis=1)
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)
# Initialize the RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
# Fit the model to the training data
clf.fit(X_train, y_train)
# Make predictions on the test data
y_pred = clf.predict(X_test)


def predict1(data):
    x = np.array(data)
    x = x.reshape(1, -1)
    print(x)
    res = clf.predict(x)
    my_dict = {'Arthritis': 0, 'Cold': 1, 'Fatigue': 2, 'Flu': 3,
               'Heart Disease': 4, 'None': 5, 'Respiratory Issue': 6}

    def get_key(val, my_dict):
        for key, value in my_dict.items():
            if val == value:
                return key
    disease = get_key(res, my_dict)
    return disease
