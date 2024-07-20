from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

df = pd.read_csv("data/synthetic_health_data2.csv")
X = df.loc[:, 'Age':'BMI']
y = df.loc[:, 'Obesity':'No_issue']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Initialize the RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the model to the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


def predict(data):
    x = np.array(data)
    x = np.array(x)
    x = x.reshape(1, -1)
    print(x)
    res = clf.predict(x)
    return res


# The data creation process is present in github
'''A Prediction recommendation will be sent to the user 
in form of pdf which will be downloadable during full 
development'''

'''symptoms based diagonsis analysis will be also availabe
the data is already loaded'''
