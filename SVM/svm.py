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



# Using SVM now
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(x_train, y_train)


y_pred = classifier.predict(x_test)


# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# print("Accuracy:", accuracy_score(y_test, y_pred))
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))


hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance: "))
assignment = float(input("Enter assignment score: "))
sleep = float(input("Enter sleep hours: "))

data = [[hours, attendance, assignment, sleep]]

data = sc.transform(data)

result = classifier.predict(data)

if result[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")