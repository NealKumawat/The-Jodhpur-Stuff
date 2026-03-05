import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Naive_Bayes_Theorem/data.csv")

x = df.iloc[:, 0:4]
y = df.iloc[:, 5]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)


#Feature Scaling- it scales and makes everything come under a specific range
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)


# Logistic Regression Model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# Train the model
model.fit(x_train, y_train)

# Predict results
y_pred = model.predict(x_test)

# Accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)

print("Predictions:", y_pred)
print("Accuracy:", accuracy)


hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance: "))
assignment = float(input("Enter assignment score: "))
sleep = float(input("Enter sleep hours: "))

data = [[hours, attendance, assignment, sleep]]

data = sc.transform(data)

result = model.predict(data)

if result[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")