import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("Plotting/cancer.csv")
print(df.columns)

# Display first few rows (to confirm it's loaded properly)
print(df.head())

# Plot 1: Quarter vs Overall Survival
plt.figure()
plt.plot(df["Quarter_from_2018"], df["Overall_survival_rate"])
plt.xlabel("Quarter")
plt.ylabel("Overall Survival (%)")
plt.title("Quarter vs Overall Survival")
plt.show()
plt.savefig("survival_plot.png")